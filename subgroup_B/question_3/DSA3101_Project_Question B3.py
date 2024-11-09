# # **Subgroup B Question 3: Linear Programming Optimization**

import pandas as pd
from pyomo.environ import *
from datetime import datetime, date, time
from flask import Flask, request, jsonify
import sqlite3
import csv
import os

print("Current working directory:", os.getcwd())
# In[5]:


app = Flask(__name__)


# ## Importing CSV files
wait_times_df = pd.read_csv('../../data/processed/uss_processed_wait_times.csv')
ride_details_df = pd.read_csv('../../data/raw/uss_ride_details.csv')
#holidays_df = pd.read_csv('holidays_data copy.csv')


sheet_2023 = pd.read_excel('../../data/processed/uss_sg_holidays.xls', sheet_name="2023")
sheet_2024 = pd.read_excel('../../data/processed/uss_sg_holidays.xls', sheet_name="2024")

conn = sqlite3.connect(":memory:")

# Load dataframes into SQL tables
sheet_2023.to_sql("holidays_2023", conn, index=False, if_exists="replace")
sheet_2024.to_sql("holidays_2024", conn, index=False, if_exists="replace")

# Join the tables with SQL and load the result into a new DataFrame
query = """
SELECT * FROM holidays_2023
UNION
SELECT * FROM holidays_2024
"""
holidays_df = pd.read_sql(query, conn)

# Close the connection
conn.close()

holidays_df['date'] = pd.to_datetime(holidays_df['date'])
holidays_df['date'] = holidays_df['date'].dt.date

holidays_df.head()  # Display the first few rows



# In[11]:


ride_details_df['Duration (s)'] = pd.to_numeric(ride_details_df['Duration (s)'], errors='coerce')
ride_details_df['Capacity per launch'] = pd.to_numeric(ride_details_df['Capacity per launch'], errors='coerce')

unique_time_slots = wait_times_df['Date Time'].str.split(' ').str[1].unique().tolist()
unique_dates = wait_times_df['Date Time'].str.split(' ').str[0].unique().tolist()
unique_rides = ride_details_df['Ride'].unique().tolist()


# In[14]:


# Convert date format in holidays_df to match date format in wait_times_df
holidays_df['date'] = holidays_df['date'].apply(lambda x: x.strftime('%y-%m-%d'))
# Convert holiday dates to a set for easy lookup
holidays = set(holidays_df['date'])

# Define a function to check if a date is a holiday
def is_holiday(date):
    return date in holidays

# Create necessary dictionaries for easier data retrieval later

guests_entering_ride = {}
for _, row in ride_details_df.iterrows():
    ride = row['Ride']
    if ride not in guests_entering_ride:
        guests_entering_ride[ride] = {}

    guests_entering_ride[ride] = row['Capacity per launch']

# Contains ride duration for each ride
rj = {}
for _, row in ride_details_df.iterrows():
    ride = row['Ride']
    if ride not in rj:
        rj[ride] = {}

    rj[ride] = row['Duration (s)']/60

# Contains additional time needed for each ride (entry, safety checks, exit etc.)
ej = {}
for _, row in ride_details_df.iterrows():
    ride = row['Ride']
    if ride not in ej:
        ej[ride] = {}

    ej[ride] = row['Additional Time']/60


# Contains minimum staff needed for each ride
min_staff = {}
for _, row in ride_details_df.iterrows():
    ride = row['Ride']
    if ride not in min_staff:
        min_staff[ride] = {}


    min_staff[ride] = row['Min Staff']

# Contains maximum staff needed for each ride
max_staff = {}
for _, row in ride_details_df.iterrows():
    ride = row['Ride']
    if ride not in max_staff:
        max_staff[ride] = {}

    max_staff[ride] = row['Max Staff']



# The demand of each ride at each time slot is calculated by the following formula:

def calculate_demand(row):
    ride = row['Ride']
    wait_time = row['Waittime']
    ride_duration = rj[ride]
    additional_time = ej[ride]
    ride_capacity = guests_entering_ride[ride]  # Ride capacity from ride_details.csv

    # Apply the demand formula
    demand = (wait_time / (ride_duration+additional_time)) * ride_capacity
    return round(demand)

# Add a new column to the wait_times_df to store the calculated demand
wait_times_df['Demand'] = wait_times_df.apply(calculate_demand, axis=1)

#print(wait_times_df)

# Create dictionary for demand and waittime
predicted_demand = {}
for _, row in wait_times_df.iterrows():
    date_time = row['Date Time']
    date, time = date_time.split(' ')
    # Check if the date exists in the dictionary, if not, add it
    if date not in predicted_demand:
        predicted_demand[date] = {}

    # Check if the time exists under the current date, if not, add it
    if time not in predicted_demand[date]:
        predicted_demand[date][time] = {}

    # Add the ride and its demand to the dictionary
    predicted_demand[date][time][row['Ride']] = row['Demand']

waittime = {}
for _, row in wait_times_df.iterrows():
    date_time = row['Date Time']
    date, time = date_time.split(' ')
    if date not in waittime:
        waittime[date] = {}

    if time not in waittime[date]:
        waittime[date][time] = {}

    waittime[date][time][row['Ride']] = row['Waittime']


# ## Defining the Model
# 
# We begin by creating a linear programming problem and setting it as a minimization problem.
# 

# Step 1: Define the model and optimization process for each day
def optimize_for_date(date):
    model = ConcreteModel()

    model.time_slots = Set(initialize= unique_time_slots)
    model.rides = Set(initialize=unique_rides)

    # Decision variables
    model.S = Var(model.time_slots, model.rides, within=NonNegativeReals,
                  bounds=lambda model, time_slot, ride: (min_staff[ride], max_staff[ride]))

    # Ride time function using decision variables directly
    def ride_time(model, time_slot, ride):
        return rj[ride] + ej[ride] - 0.5 * (model.S[time_slot, ride] - min_staff[ride])

    # Objective: Minimize average wait time per day
    def average_wait_time_rule(model):
        total_wait_time = 0
        for ride in model.rides:
            wait_time_for_slot = 0
            for time_slot in model.time_slots:
                ride_wait_time = (predicted_demand[date][time_slot][ride] / guests_entering_ride[ride]) * ride_time(model, time_slot, ride)
                wait_time_for_slot += ride_wait_time
            total_wait_time += wait_time_for_slot
        return total_wait_time / (len(model.time_slots)*len(model.rides))

    #model.average_wait_time = average_wait_time_rule(model)  # Store the average wait time for constraint
    model.obj = Objective(rule=average_wait_time_rule, sense=minimize)

    #model.wait_time_constraint = Constraint(expr=model.average_wait_time >= 31.75)

    def total_staff_constraint_rule(model, time_slot):
        if is_holiday(date):
            return sum(model.S[time_slot, ride] for ride in model.rides) <= 40  # Staff limit 40 for holidays
        else:
            return sum(model.S[time_slot, ride] for ride in model.rides) <= 35  # Staff limit 35 for regular days

    model.total_staff_constraints = Constraint(model.time_slots, rule=total_staff_constraint_rule)

    # Solve the model
    solver = SolverFactory('glpk')
    solver.solve(model)

    # Post-process: Collect results
    staff_allocations = {time_slot: {ride: model.S[time_slot, ride].value for ride in model.rides} for time_slot in model.time_slots}
    wait_times = {}

    for time_slot in model.time_slots:
        wait_times[time_slot] = {}
        for ride in model.rides:
            staff_allocated = model.S[time_slot, ride].value
            #print(rj[ride],ej[ride],staff_allocated,min_staff[ride])
            ride_time_value = rj[ride] + ej[ride] - 0.5 * (staff_allocated - min_staff[ride])
            adjusted_demand = predicted_demand[date][time_slot][ride]
            if adjusted_demand < 0:
                adjusted_demand = 0
            wait_times[time_slot][ride] = (adjusted_demand / guests_entering_ride[ride]) * ride_time_value

    return model, staff_allocations, wait_times

# Flask endpoint for the API
'''
@app.route('/optimize_staff_allocation', methods=['POST'])
def optimize_staff_allocation():
    data = request.get_json()
    date = data.get('date')
    
    if not date:
        return jsonify({"error": "Date parameter is required"}), 400
    
    try:
        # Unpack all three returned values, but ignore `model` in the response
        model, staff_allocations, wait_times = optimize_for_date(date)
        
        # Prepare response with only the necessary parts
        response_data = {
            "date": date,
            "staff_allocations": staff_allocations,
            "wait_times": wait_times
        }
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
'''
    
def save_to_csv(data, date, data_type):
    """Utility function to save dictionary data to a CSV file with a specific filename format."""
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
    filename = os.path.join(output_dir, f"{data_type}_{date}.csv")
    
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        
        # Write headers
        headers = ["Time Slot"] + list(data[next(iter(data))].keys())
        writer.writerow(headers)
        
        # Write data rows
        for time_slot, allocations in data.items():
            row = [time_slot] + list(allocations.values())
            writer.writerow(row)
    
    print(f"{data_type.capitalize()} data saved as '{filename}'")

@app.route('/optimize_staff_allocation', methods=['POST'])
def optimize_staff_allocation():
    data = request.get_json()
    date = data.get('date')
    
    if not date:
        return jsonify({"error": "Date parameter is required"}), 400
    
    try:
        # Get the optimization results
        model, staff_allocations, wait_times = optimize_for_date(date)
        
        # Save outputs to CSV files
        save_to_csv(staff_allocations, date, "staff_allocations")
        save_to_csv(wait_times, date, "wait_times")
        
        # Prepare response
        response_data = {
            "date": date,
            "staff_allocations": staff_allocations,
            "wait_times": wait_times
        }
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask app without threading
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


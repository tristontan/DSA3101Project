import pandas as pd


ride_details_df = pd.read_csv('data/raw/uss_ride_details.csv')
file_path = 'data/raw/uss_wait_times.csv'
df = pd.read_csv(file_path)

### ---------------- Calculate 30min interval average time ---------------- ###
print(df.head())
df.rename(columns={'Ride': 'ride', 'Date/Time': 'datetime', 'Wait Time': 'waittime' }, inplace=True)
print(df.head())
# Convert the 'datetime' column to a proper datetime format
df['datetime'] = pd.to_datetime(df['datetime'])
# Create a new column that rounds the timestamp down to the nearest 30 minutes
df['30min_interval'] = df['datetime'].dt.floor('30T')
# Group by the 30-minute interval and the ride name, then calculate the average wait time
df_30min_avg = df.groupby(['30min_interval', 'ride'], as_index=False)['waittime'].mean()

# Display the processed dataframe
#print(df_30min_avg)

# Optional: Save the processed data to a new CSV file
df_30min_avg.to_csv('data/processed/uss_30min_interval_avg_waittimes.csv', index=False)

### -------------- Fill in missing rides and dates ---------------------- ####

# Step 1: Get the list of all unique rides from ride_details_df
all_rides = ride_details_df['Ride'].unique()

df_30min_avg.rename(columns={'ride': 'Ride', '30min_interval': 'Date Time', 'waittime': 'Waittime' }, inplace=True)
# Step 2: Create a dictionary of rides present per time slot
rides_per_time_slot = df_30min_avg.groupby('Date Time')['Ride'].apply(set).to_dict()

# Step 3: Prepare the list of missing rides entries
missing_entries = []
for time_slot, rides_present in rides_per_time_slot.items():
    missing_rides = set(all_rides) - rides_present
    for missing_ride in missing_rides:
        missing_entries.append({'Date Time': time_slot, 'Ride': missing_ride, 'Waittime': 0.0})

# Convert missing entries to DataFrame and append to original data
missing_rides_df = pd.DataFrame(missing_entries)
updated_wait_times_df = pd.concat([df_30min_avg, missing_rides_df], ignore_index=True)

# Sort the DataFrame by time and ride name for better readability
#updated_wait_times_df = updated_wait_times_df.sort_values(by=['Date Time', 'Ride'])

updated_wait_times_df['Date Time'] = pd.to_datetime(updated_wait_times_df['Date Time'], format='%d/%m/%y %H:%M', errors='coerce')

# Generate all possible 30-minute timeslots based on the range of your data
min_time = updated_wait_times_df['Date Time'].min()
max_time = updated_wait_times_df['Date Time'].max()
print(min_time)
print(max_time)
all_timeslots = pd.date_range(start=min_time, end=max_time, freq='30min')
print(all_timeslots)

# Get all unique rides
all_rides = updated_wait_times_df['Ride'].unique()

# Create a DataFrame with all combinations of timeslots and rides
full_timeslot_ride_df = pd.MultiIndex.from_product([all_timeslots, all_rides], names=['Date Time', 'Ride']).to_frame(index=False)

# Merge with original data to find missing entries
merged_df = pd.merge(full_timeslot_ride_df, updated_wait_times_df, on=['Date Time', 'Ride'], how='left')

# Fill missing wait times with 0
merged_df['Waittime'] = merged_df['Waittime'].fillna(0)


# Extract the time from the 'Date Time' column
merged_df['Time'] = merged_df['Date Time'].dt.time

# Define the time range
start_time = pd.to_datetime("10:00", format="%H:%M").time()
end_time = pd.to_datetime("17:00", format="%H:%M").time()

# Remove rows where the time is before 10:00 or after 17:00
filtered_df = merged_df[(merged_df['Time'] >= start_time) & 
                                (merged_df['Time'] <= end_time)]
#print(filtered_df)


output_file_path = 'data/processed/uss_processed_wait_times.csv'
filtered_df.to_csv(output_file_path, index=False)

# Provide the output file path
print(f"The updated data is saved to: {output_file_path}")

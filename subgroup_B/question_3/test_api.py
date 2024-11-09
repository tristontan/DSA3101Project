
import requests
import pandas as pd

# Adjust Pandas display options to show all columns
pd.set_option("display.max_columns", None)  # Show all columns
pd.set_option("display.width", 1000)  

# API request
url = "http://127.0.0.1:5001/optimize_staff_allocation"
payload = {"date": "2024-05-13"}
response = requests.post(url, json=payload)

# Check if the response is successful
if response.status_code == 200:
    data = response.json()
    
    # Extract 'staff_allocations' and 'wait_times' from the response
    staff_allocations = data.get("staff_allocations", {})
    wait_times = data.get("wait_times", {})

    # Convert 'staff_allocations' and 'wait_times' to DataFrames for better visualization
    staff_allocations_df = pd.DataFrame.from_dict(staff_allocations, orient="index")
    wait_times_df = pd.DataFrame.from_dict(wait_times, orient="index")

    # Display DataFrames
    print("Staff Allocations:")
    print(staff_allocations_df)

    print("\nWait Times:")
    print(wait_times_df)
else:
    print(f"Request failed with status code: {response.status_code}")
    print("Error:", response.json())


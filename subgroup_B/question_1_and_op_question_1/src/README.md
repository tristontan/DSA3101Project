# USS Wait Time Predictor

This Streamlit app estimates wait times at Universal Studios Singapore (USS) based on key factors that influence guest demand. Designed for **Subgroup B Question 1**, the model uses wait time as a **proxy** for guest demand.

## Features

The demand forecasting model uses the following input features to generate predictions:

- **is_raining**: Indicates if there is thunder or rain in the weather forecast.
- **mean_temperature**: The average of the low and high temperatures within the specified time.
- **is_weekend**: Specifies if the day falls on a weekend.
- **is_special_event**: Denotes if there is a special event occurring at USS, such as themed celebrations or pop-up events.
- **is_holiday**: Marks if the day is a public or school holiday.
- **international_tourists**: Represents the estimated number of international tourists visiting Singapore on that day.

## How to Use

1. Enter the values for each feature.
2. Click **Predict Wait Time** to display the estimated wait time.

## Setup Instructions

### Local Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the app using:
   ```bash
   streamlit run main.py
### Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t uss-wait-time-predictor .
2. Run the Docker container:
   ```bash
   docker run -p 8501:8501 uss-wait-time-predictor
3. Visit http://localhost:8501 to access the app.


# Data Sources (Raw Data)

1. `uss_wait_times.csv`
- Description: This dataset is a compilation of waiting times for each of the 14 attractions in USS. The waiting time for each attraction is recorded in intervals of 5 minutes. All waiting times are recorded between 10am to 10pm, apart from the period of Halloween Horror Nights 2023 (29 Sept to 4 Nov 2023) where ride operating hours were extended beyond regular park operating hours. This dataset consists of 642513 entries, spanning Q1 2023 to Q2 2024.   
- [Source](https://www.thrill-data.com/waits/park/unit/universal-studios-singapore/)
- Structure

| Column Name      | Description     | Type    |
|----------------|----------------|----------------|
| ride  | The name of the ride  | object  |
| datetime  | The date and time of the waittime recorded  | datetime64  |
| waittime  | The waiting time (in minutes) for the ride at the given time  | int64  |

2. `uss_tripadvisor_reviews.xlsx`
- Description: This dataset contains reviews of Universal Studio Singapore scraped from Tripadvisor.com. This dataset consists of 6,361 reviews, with publication dates ranging from 2017-05-22 to 2024-09-27.  
- [Source](https://www.tripadvisor.com.sg/Attraction_Review-g294264-d2439664-Reviews-Universal_Studios_Singapore-Sentosa_Island.html)
- Due to anti-bot measures implemented by Tripadvisor, the dataset was obtained using the 'Tripadvisor Reviews Scraper' from [Apify.com](https://apify.com/maxcopell/tripadvisor-reviews).
The dataset includes only public information that users have chosen to share, in accordance with Apify’s commitment to ethical scraping practices. Apify states:
"Our Tripadvisor scrapers are ethical and do not extract any private user data. They only extract what users have chosen to share publicly on the website..."
- Structure

| Column Name         | Description                                                                 | Type        |
|---------------------|-----------------------------------------------------------------------------|-------------|
| helpfulVotes        | The number of "helpful" votes the review has received from other users.     | int64       |
| id                  | A unique identifier for each review.                                        | int64       |
| reviewDate          | The date on which the review was published on Tripadvisor in yyyy-mm-dd form.| datetime64  |
| publishedPlatform   | The platform or medium through which the review was posted on Tripadvisor (e.g., MOBILE, OTHER). | object |
| rating              | The overall rating given by the reviewer, on a scale of 1 to 5.            | int64       |
| text                | The body of the review.                                                     | object      |
| title               | The title or headline of the review.                                        | object      |
| travelDate          | The date when the reviewer visited Universal Studio Singapore in yyyy-mm-dd form. | datetime64 |
| tripType            | The type of trip the reviewer took, such as FAMILY, FRIENDS, SOLO, COUPLES. | object      |
| username            | The username of the reviewer on Tripadvisor.                                | object      |
| userLocation        | The location (state and country) of the reviewer, as indicated on their Tripadvisor profile. | object |
| state               | The state extracted from the user's location.                               | object      |
| country             | The country extracted from the user's location.                             | object      |



3. `sentosa_region_weather_data.csv`
- Description: This dataset is a compilation of weather data in Sentosa Island from January 2023 to August 2024. There are 609 entries in total.
- [Source](https://www.weather.gov.sg/climate-historical-daily/)
- Structure

| Column Name                | Description                                                 | Type    |
|----------------------------|-------------------------------------------------------------|---------|
| Station                     | The ID of the weather station collecting the data.          | int64   |
| Year                        | The year of data collection.                                | int64   |
| Month                       | The month of data collection.                               | int64   |
| Day                         | The day of data collection.                                 | float64 |
| Daily Rainfall Total (mm)   | Total rainfall for the day in millimeters.                  | float64 |
| Highest 30 min Rainfall (mm)| Maximum rainfall recorded in a 30-minute period (mm).      | float64 |
| Highest 60 min Rainfall (mm)| Maximum rainfall recorded in a 60-minute period (mm).      | float64 |
| Highest 120 min Rainfall (mm)| Maximum rainfall recorded in a 120-minute period (mm).    | float64 |
| Mean Temperature (°C)       | Average temperature recorded for the day in degrees Celsius.| float64 |

4. uss_ride_details.csv
- Description:
- Source: Wikipedia, Youtube Videos, Blogs, former USS Staff
- Structure

| Column Name         | Description                                                               | Type    |
|---------------------|---------------------------------------------------------------------------|---------|
| Ride                | The name of the attraction or ride.                                       | object  |
| Duration (s)        | The duration of the ride in seconds.                                      | int64     |
| Additional Time (s) | Additional time for each ride in seconds (e.g., time for entry, seatbelt check, exit). | int64     |
| Capacity per launch | The number of guests that can be accommodated per ride launch.            | int64     |
| Launch type         | The type of ride launch: continuous or delayed.                           | object  |
| Min Staff           | Minimum number of staff required to operate the ride safely.              | int64     |
| Max Staff           | Maximum number of staff allowed for optimal operation.                    | int64     |


5. `uss_attractions_locations.csv`
- Description: This dataset contains information about various attractions and food & beverage (F&B) locations within USS.
- Source: Extracted using Distancematrix API
- Structure

| Column Name  | Description                                                               | Type    |
|--------------|---------------------------------------------------------------------------|---------|
| name         | The name of the attraction or location.                                   | object  |
| coordinates  | The latitude and longitude coordinates of the location in the format `lat,long`. | object  |
| lat          | The latitude coordinate of the location.                                  | float64   |
| long         | The longitude coordinate of the location.                                 | float64   |
| type         | The type of location, indicating whether it is a ride or an F&B (food and beverage) establishment. | object  |


6. (survey)
- Description: 
- Source: Details about how we conduct our survey can be found [here](https://github.com/tristontan/StatSmith/wiki/USS-Guest-Experience-Survey)
- Structure

# Data Sources (Processed Data)
1. uss_international_tourist_arrival.xlsx
- Description:
- Source:
- Structure

2. uss_sg_holidays.xls
- Description:
- Source:
- Structure

3. uss_special_events.xlsx
- Description:
- Source:
- Structure

## Notes
- Data Privacy: No personal or sensitive information is included in these datasets. All data is either publicly available, generated synthetically, or anonymized for use in this project.
- Assumptions: Where real-world data was unavailable, assumptions were made to fill gaps. See the projects' Wiki for details on these assumptions.

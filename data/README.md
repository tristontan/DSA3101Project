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


6. `raw_survey_data.csv`
- Description: This dataset contains the raw data obtained from our survey and was hosted on Google Forms.
- Source: Details about how we conduct our survey can be found [here](https://github.com/tristontan/StatSmith/wiki/USS-Guest-Experience-Survey)
- Structure

Column Name | Description  | Type
---  | --- | ---
Timestamp | Time of survey submission  | object
What is your age? | Age of respondent |  object
What is your gender? | Gender of respondent |  object
Are you a tourist or a local? | Whether respondent is a local or tourist | object
Who do you usually go to USS with? | Respondents' USS companions | object
How often do you visit USS? | Respondents' visiting frequency | object
On what occasion(s) would you visit USS? | Respondents' visitng occasion |  object
On a scale from 1 to 5, how important are the following factors in making USS attractive to you? [Food options] | Importance of food options in making USS attractive |  object
On a scale from 1 to 5, how important are the following factors in making USS attractive to you? [Types of rides available] | Importance of types of rides available in making USS attractive |  object
On a scale from 1 to 5, how important are the following factors in making USS attractive to you? [Gift shops] |  Importance of gift shops in making USS attractive |  object
On a scale from 1 to 5, how important are the following factors in making USS attractive to you? [Special events (e.g. Halloween Horror Night)] |  Importance of special events in making USS attractive |  object
On a scale from 1 to 5, how important are the following factors in making USS attractive to you? [Accessibility] |  Importance of accessibility in making USS attractive |  object
On a scale from 1 to 5, how influential are the following factors in encouraging you to purchase a seasonal pass? [Frequent visitor to USS] | Importance of frequency of visit to USS in encouraging the purchase of a seasonal pass | object
On a scale from 1 to 5, how influential are the following factors in encouraging you to purchase a seasonal pass? [Bundle price] | Importance of bundle price in encouraging the purchase of a seasonal pass | object
On a scale from 1 to 5, how influential are the following factors in encouraging you to purchase a seasonal pass? [Eligibility during a holiday period] | Importance of pass's eligibility during holiday period in encouraging the purchase of a seasonal pass | object
What time are you most likely to visit USS? | Respondents' likely time of entry |  object
What time are you most likely to leave USS? | Respondents' likely time of exit |  object
In general, how would you rate your experience at USS? | Respondents' USS experience rating |  int64
On a scale from 1 to 5, how influential were the following factors in improving your past experience at USS? [Short wait times] | Importance of short wait times improving past experiences | object
On a scale from 1 to 5, how influential were the following factors in improving your past experience at USS? [Lack of crowds] | Importance of lack of crowds improving past experiences | object
On a scale from 1 to 5, how influential were the following factors in improving your past experience at USS? [Fun attractions] | Importance of fun attractions improving past experiences | object
On a scale from 1 to 5, how influential were the following factors in improving your past experience at USS? [Affordable food options] | Importance of affordable food options improving past experiences | object
On a scale from 1 to 5, how influential were the following factors in improving your past experience at USS? [Accessibility (Ramps, even ground, easy to find seats etc)] | Importance of accessibility improving past experiences | object
On a scale from 1 to 5, how influential were the following factors in improving your past experience at USS? [Cooling Weather] | Importance of cooling weather improving past experiences | object
On a scale from 1 to 5, how influential were the following factors in improving your past experience at USS? [Presence of Shaded Rest Areas] | Importance of shaded rest areas improving past experiences | object
On a scale from 1 to 5, how influential were the following factors in improving your past experience at USS? [Usability of the Universal Studios Singapore App] | Importance of USS App usability improving past experiences | object
On a scale from 1 to 5, how influential were the following factors in worsening your past experience at USS? [Long wait time] | Importance of long wait time worsening past experience | object
On a scale from 1 to 5, how influential were the following factors in worsening your past experience at USS? [Crowds] | Importance of crowds worsening past experience | object
On a scale from 1 to 5, how influential were the following factors in worsening your past experience at USS? [Attractions not being fun enough] | Importance of attractions not being fun enough worsening past experience | object
On a scale from 1 to 5, how influential were the following factors in worsening your past experience at USS? [Expensive food options] | Importance of expensive food options worsening past experience | object
On a scale from 1 to 5, how influential were the following factors in worsening your past experience at USS? [Inaccessibility (Lack of ramps, Uneven ground, lack of seats etc)] | Importance of inaccessibility worsening past experience | object
On a scale from 1 to 5, how influential were the following factors in worsening your past experience at USS? [Hot weather] | Importance of hot weather worsening past experience | object
On a scale from 1 to 5, how influential were the following factors in worsening your past experience at USS? [Lack of Shaded Rest Areas] | Importance of lack of shaded rest areas worsening past experience | object
On a scale from 1 to 5, how influential were the following factors in worsening your past experience at USS? [Usability of the Universal Studios Singapore App] | Importance of USS App usability worsening past experience | object
On a scale from 1 to 5, in wet weather, how likely are you to choose the following activities at USS? [Seek shelter in a restaurant] | Likelihood of seeking shelter in a restaurant in wet weather | object
On a scale from 1 to 5, in wet weather, how likely are you to choose the following activities at USS? [Go home] | Likelihood of going home in wet weather | object
| On a scale from 1 to 5, in wet weather, how likely are you to choose the following activities at USS? [Visit indoor attractions] | Likelihood of visiting indoor attractions in wet weather | object |
| On a scale from 1 to 5, in wet weather, how likely are you to choose the following activities at USS? [Visit outdoor attractions (I don't mind getting wet)] | Likelihood of visiting outdoor attractions in wet weather | object |
| On a scale from 1 to 5, in wet weather, how likely are you to choose the following activities at USS? [Visit gift shops/retail areas] | Likelihood of visiting gift shops in wet weather | object |
| If majority of the rides are closed due to the weather, how long are you willing to wait for the weather to clear up before continuing your activities? | Maximum waiting tolerance in wet weather | object |
| On a scale from 1 to 5, how important are the following factors when planning your route in USS? [Expected wait time] | Importance of expected wait time when planning route | object |
| On a scale from 1 to 5, how important are the following factors when planning your route in USS? [Enjoyment of the ride] | Importance of enjoyment when planning route | object |
| On a scale from 1 to 5, how important are the following factors when planning your route in USS? [Closeness of ride to current location] | Importance of ride proximity when planning route | object |
| On a scale from 1 to 5, how important are the following factors when planning your route in USS? [Prioritisation of Group's Preferences (e.g. going with your family and choosing to go to the rides that your younger siblings prefer)] | Importance of prioritizing group preferences when planning route | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Battlestar Galactica: Human vs. Cylon] | Likelihood of visiting Battlestar Galactica on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Transformers The Ride: The Ultimate 3D Battle] | Likelihood of visiting Transformers on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Revenge of the Mummy] | Likelihood of visiting Revenge of the Mummy on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Jurassic Park Rapids Adventure] | Likelihood of visiting Jurassic Park on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Sesame Street Spaghetti Space Chase] | Likelihood of visiting Sesame Street on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Canopy Flyer] | Likelihood of visiting Canopy Flyer on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Puss In Boots' Giant Journey] | Likelihood of visiting Puss In Boots on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Dino-Soarin'] | Likelihood of visiting Dino-Soarin' on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Enchanted Airways] | Likelihood of visiting Enchanted Airways on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Treasure Hunters (Vintage Car Attraction)] | Likelihood of visiting Treasure Hunters on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Accelerator (Spinning Ride)] | Likelihood of visiting Accelerator on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Magic Potion Spin (Far Far Away Ferris Wheel)] | Likelihood of visiting Magic Potion Spin on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Lights, Camera, Action!] | Likelihood of visiting Lights, Camera, Action! on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [The Dance for the Magic Beans (Interactive show with Puss in Boots and Kitty Softpaws)] | Likelihood of attending Dance for the Magic Beans on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Shrek 4-D Adventure] | Likelihood of visiting Shrek 4-D on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Donkey Live] | Likelihood of visiting Donkey Live on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [Rhythm Truck 2.0] | Likelihood of visiting Rhythm Truck on a busy day | object |
| On a scale from 1 to 5, how likely are you to visit the following attractions on a busy day? [WaterWorld] | Likelihood of visiting WaterWorld on a busy day | object |
| How long are you willing to queue and wait for a ride? | Maximum tolerable waiting time on a normal day | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Battlestar Galactica: Human vs. Cylon] | Willingness to wait for Battlestar Galactica | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Transformers The Ride: The Ultimate 3D Battle] | Willingness to wait for Transformers | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Revenge of the Mummy] | Willingness to wait for Revenge of the Mummy | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Jurassic Park Rapids Adventure] | Willingness to wait for Jurassic Park Rapids Adventure | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Sesame Street Spaghetti Space Chase] | Willingness to wait for Sesame Street Spaghetti Space Chase | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Canopy Flyer] | Willingness to wait for Canopy Flyer | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Puss In Boots' Giant Journey] | Willingness to wait for Puss In Boots' Giant Journey | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Dino-Soarin'] | Willingness to wait for Dino-Soarin' | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Enchanted Airways] | Willingness to wait for Enchanted Airways | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Treasure Hunters (Vintage Car Attraction)] | Willingness to wait for Treasure Hunters | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Accelerator (Spinning Ride)] | Willingness to wait for Accelerator | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Magic Potion Spin (Far Far Away Ferris Wheel)] | Willingness to wait for Magic Potion Spin | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Lights, Camera, Action!] | Willingness to wait for Lights, Camera, Action! | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [The Dance for the Magic Beans (Interactive show with Puss in Boots and Kitty Softpaws)] | Willingness to wait for Dance for the Magic Beans | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Shrek 4-D Adventure] | Willingness to wait for Shrek 4-D Adventure | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Donkey Live] | Willingness to wait for Donkey Live | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [Rhythm Truck 2.0] | Willingness to wait for Rhythm Truck 2.0 | object |
| On a scale from 1 to 5, how willing would you be to wait for the following rides? [WaterWorld] | Willingness to wait for WaterWorld | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Battlestar Galactica: Human vs. Cylon] | Level of appeal of Battlestar Galactica | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Transformers The Ride: The Ultimate 3D Battle] | Level of appeal of Transformers The Ride | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Revenge of the Mummy] | Level of appeal of Revenge of the Mummy | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Jurassic Park Rapids Adventure] | Level of appeal of Jurassic Park Rapids Adventure | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Sesame Street Spaghetti Space Chase] | Level of appeal of Sesame Street Spaghetti Space Chase | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Canopy Flyer] | Level of appeal of Canopy Flyer | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Puss In Boots' Giant Journey] | Level of appeal of Puss In Boots' Giant Journey | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Dino-Soarin'] | Level of appeal of Dino-Soarin' | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Enchanted Airways] | Level of appeal of Enchanted Airways | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Treasure Hunters (Vintage Car Attraction)] | Level of appeal of Treasure Hunters (Vintage Car Attraction) | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Accelerator (Spinning Ride)] | Level of appeal of Accelerator (Spinning Ride) | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Magic Potion Spin (Far Far Away Ferris Wheel)] | Level of appeal of Magic Potion Spin | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Lights, Camera, Action!] | Level of appeal of Lights, Camera, Action! | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [The Dance for the Magic Beans (Interactive show with Puss in Boots and Kitty Softpaws)] | Level of appeal of The Dance for the Magic Beans | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Shrek 4-D Adventure] | Level of appeal of Shrek 4-D Adventure | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Donkey Live] | Level of appeal of Donkey Live | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [Rhythm Truck 2.0] | Level of appeal of Rhythm Truck 2.0 | object |
| On a scale from 1 to 5, how appealing do you find each attraction? [WaterWorld] | Level of appeal of WaterWorld | object |
| On a scale from 1 to 5, how important are these factors in making the queuing process more tolerable/pleasant? [Entertainment in Queuing Area (e.g. Videos, Interactive Elements)] | Importance of entertainment in queueing area | object |
| On a scale from 1 to 5, how important are these factors in making the queuing process more tolerable/pleasant? [Anticipation of Ride] | Importance of anticipation of ride | object |
| On a scale from 1 to 5, how important are these factors in making the queuing process more tolerable/pleasant? [Shaded/Cooling Queuing Area] | Importance of shaded/cooling queuing area | object |
| On a scale from 1 to 5, how important are these factors in making the queuing process more tolerable/pleasant? [Comfortable Seating along Queuing Area] | Importance of comfortable seating in queuing area | object |
| On a scale from 1 to 5, how important are these factors in making the queuing process more tolerable/pleasant? [Music in the Queuing Area] | Importance of music in queuing area | object |
| On a scale from 1 to 5, how important are these factors in making the queuing process more tolerable/pleasant? [Line moving at a Consistent Pace] | Importance of line moving consistently | object |
| On a scale from 1 to 5, how important are these factors in making the queuing process more tolerable/pleasant? [Restrooms Nearby/Accessible during the Queue] | Importance of accessible restrooms during queue | object |
| On a scale from 1 to 5, how important are these factors in making the queuing process more tolerable/pleasant? [Positive Prior Experience with Ride] | Importance of prior positive experience with ride | object |
| "What is the maximum amount you are willing to pay for a ticket (in SGD) during peak periods? For reference, the current ticket pricings are: Non-local pricing Adult Ticket (Ages 13 and above): $83 Child Ticket (Ages 4 to 12 years old): $62 Singapore Resident pricing Adult Ticket (Ages 13 and above): $74 Child Ticket (Ages 4 to 12 years old): $59" | Maximum tolerable price ticket during peak periods | object |
| "What is the maximum amount you are willing to pay for a ticket (in SGD) during off-peak periods? For reference, the current ticket pricings are: Non-local pricing Adult Ticket (Ages 13 and above): $83 Child Ticket (Ages 4 to 12 years old): $62 Singapore Resident pricing Adult Ticket (Ages 13 and above): $74 Child Ticket (Ages 4 to 12 years old): $59" | Maximum tolerable price ticket during off-peak periods | object |
| Do you usually buy an express pass when you visit USS? | Prior experience of purchasing express pass | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Variety of Rides and Attractions] | Rating variety of rides and attractions | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Entertainment and Shows (e.g. Rollercoasters, WaterWorld Performance)] | Rating entertainment and shows | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Waiting Time] | Rating of waiting time | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Cleanliness of Park and Amenities] | Rating cleanliness of park and amenities | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Staff Friendliness] | Rating staff friendliness | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Availability of Rest Areas] | Rating availability of rest areas | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Quality and Variety of Food/Beverage Options] | Rating quality and variety of food/beverages | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Crowdedness] | Rating of crowdedness | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Value for Money (Entrance Fee, Food, etc)] | Rating value for money | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Variety and Quality of Souvenir Shops] | Rating variety and quality of souvenir shops | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Theme and Atmosphere] | Rating theme and atmosphere | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Special Events and Performances (E.g. Halloween Horror Night)] | Rating special events and performances | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Presence of Shaded Rest Areas] | Rating presence of shaded rest areas | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Weather on the Day of Visit] | Rating weather on the day of visit | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Park Layout and Navigation] | Rating park layout and navigation | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Accessibility (Wheelchair friendly, etc)] | Rating accessibility | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Parking Convenience and Accessibility] | Rating parking convenience and accessibility | object |
| On a scale from 1 to 5, how would you rate each aspect of the USS experience? [Queue Management] | Rating of queue management in USS experience | object |
| How likely are you to come back again? | Likelihood of return to USS | object |
| On a scale from 1 to 5, how influential are these factors in encouraging you to come back to USS again? [Enjoyed the overall experience] | Importance of enjoying the overall experience in encouraging return | object |
| On a scale from 1 to 5, how influential are these factors in encouraging you to come back to USS again? [Staying at a Sentosa resort (E.g. RWS)] | Influence of staying at a Sentosa resort on return likelihood | object |
| On a scale from 1 to 5, how influential are these factors in encouraging you to come back to USS again? [New Rides, Shows and Attractions] | Influence of new rides, shows, and attractions on return likelihood | object |
| On a scale from 1 to 5, how influential are these factors in encouraging you to come back to USS again? [Good Food and Dining Options] | Influence of food and dining options on return likelihood | object |
| On a scale from 1 to 5, how influential are these factors in encouraging you to come back to USS again? [Good Customer Service] | Influence of good customer service on return likelihood | object |
| On a scale from 1 to 5, how influential are these factors in encouraging you to come back to USS again? [Special Occasions (E.g. Halloween Horror Night)] | Influence of special occasions on return likelihood | object |
| On a scale from 1 to 5, how influential are these factors in encouraging you to come back to USS again? [Ticket Discounts and Promotions] | Influence of ticket discounts and promotions on return likelihood | object |
| On a scale from 1 to 5, how influential are these factors in encouraging you to come back to USS again? [School/work Activity] | Influence of school/work activity on return likelihood | object |
| On a scale from 1 to 5, how influential are these factors in encouraging you to come back to USS again? [Souvenirs] | Influence of souvenirs on return likelihood | object |
| "How likely are you to visit USS again if the Annual/Season Pass and Express Unlimited Pass were reintroduced?<br> Season/Annual Pass: Enjoy six OR 12 months of unlimited entry to USS<br> Express Unlimited: The pass allows you to skip the line as many times as you like, even for the same ride. (The current Express Pass only allows you to skip the line once per ride/attraction.)" | Likelihood of visiting USS with season/annual pass reintroduction | int64 |
| How likely are you to recommend your family/friends to come? | Likelihood of recommendation to family/friends | int64 |
| What suggestions do you have to improve the overall USS Experience? (If you do not have any suggestions, please enter NIL) | Suggestions for improving overall USS Experience | object |
| Which avenues have you previously purchased USS tickets from? | Ticket purchase avenue | object |
| "On a scale from 1 to 5, please rate your experience purchasing tickets from the USS Website. (If you have not previously purchased tickets from the USS Website, please select 0.)" | Rating prior experience purchasing tickets from the USS website | int64 |
| On a scale from 1 to 5, how important are the following factors in influencing your experience when purchasing your USS ticket(s)? [Ease of Navigate USS Website/Booking Platform] | Importance of ease of navigating USS Website/Booking Platform | object |
| On a scale from 1 to 5, how important are the following factors in influencing your experience when purchasing your USS ticket(s)? [Mobile App Integration] | Importance of mobile app integration in purchasing tickets | object |
| On a scale from 1 to 5, how important are the following factors in influencing your experience when purchasing your USS ticket(s)? [Option for Digital Tickets (No printing Required)] | Importance of digital tickets in purchasing experience | object |
| On a scale from 1 to 5, how important are the following factors in influencing your experience when purchasing your USS ticket(s)? [Access to Exclusive Perks (E.g. Fast Pass, VIP Access)] | Importance of exclusive perks in purchasing experience | object |
| On a scale from 1 to 5, how important are the following factors in influencing your experience when purchasing your USS ticket(s)? [Deals for Tickets (E.g. Multi-Day Ticket Discounts, Family Bundles, Credit Card Offers)] | Importance of ticket deals in purchasing experience | object |
| On a scale from 1 to 5, how important are the following factors in influencing your experience when purchasing your USS ticket(s)? [Loyalty Points] | Importance of loyalty points in purchasing experience | object |
| On a scale from 1 to 5, how important are the following factors in influencing your experience when purchasing your USS ticket(s)? [Clear Pricing Information] | Importance of clear pricing in purchasing experience | object |
| On a scale from 1 to 5, how important are the following factors in influencing your experience when purchasing your USS ticket(s)? [Multiple Payment Options (E.g. Credit Card, PayPal)] | Importance of multiple payment options in purchasing experience | object |
| On a scale from 1 to 5, how important are the following factors in influencing your experience when purchasing your USS ticket(s)? [Clear Refund and Exchange Policies] | Importance of clear refund and exchange policies | object |
| On a scale from 1 to 5, how important are the following factors in influencing your experience when purchasing your USS ticket(s)? [Fast Checkout Process] | Importance of fast checkout process in purchasing experience | object |
| On a scale from 1 to 5, how important are the following factors in influencing your experience when purchasing your USS ticket(s)? [Personalised Recommendations based on Visitor Preferences] | Importance of personalized recommendations in purchasing experience | object |
| On a scale from 1 to 5, how important are the following factors in influencing your experience when purchasing your USS ticket(s)? [Live Chat/Support for Booking Assistance] | Importance of live chat/support for booking assistance | object |
| On a scale from 1 to 5, how important are the following factors in influencing your experience when purchasing your USS ticket(s)? [Option to Add-On Parking Passes during Purchase] | Importance of parking pass option during purchase | object |
| What suggestions do you have to improve the process of purchasing tickets from the USS website? (If you have not previously purchased tickets from the USS Website, please enter NIL) | Suggestions for improving USS Website purchasing experience | object |

# Data Sources (Processed Data)
1. uss_international_tourist_arrival.xlsx
- Description: Contains number of Singapore's monthly international tourists arrival from Jan 1978 - Sep 2024
- [Source](https://tablebuilder.singstat.gov.sg/table/TS/M550001#)
- Structure:

| Column Name  | Description                                                               | Type    |
|--------------|---------------------------------------------------------------------------|---------|
| Data Series         | Year and Month of data collection                                  | date  |
| Total International Visitor Arrivals By Inbound Tourism Markets  | Total Number of International Visitor Arrivals  | int64  |

2. uss_sg_holidays.xls
- Description: Contains dates of Singapore's public holidays and school holidays (primary school, secondary school and JC) in 2023 and 2024
- Source: data.gov.sg and moe.gov.sg
- Structure

| Column Name  | Description                                                               | Type    |
|--------------|---------------------------------------------------------------------------|---------|
| date         | Date of the holiday                                  | date  |
| day  | Day of the holiday  | object  |
| holiday  | Type of holiday  | object  |

3. uss_special_events.xlsx
- Description: Contains date of USS's special events from 2023 - 2024.
- Source: Extracted from USS Instagram and Website
- Structure

| Column Name  | Description                                                               | Type    |
|--------------|---------------------------------------------------------------------------|---------|
| date         | Date of the event                                 | date  |
| special_event  | Name of event  | object  |

4. `v2_cleaned_imbalanced_survey_data.xlsx`
- Description: Cleaned and Imbalanced version 2 of the survey data. Version 2 indicates that this version of the cleaned data had more columns regrouped and dropped.
- Source: Details about how we conduct our survey can be found [here](https://github.com/tristontan/StatSmith/wiki/USS-Guest-Experience-Survey)

| Column Name                                                                                           | Description |   Data Type   |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------|
| Survey_ID                                                                                             | Unique identifier for each survey respondent.                                                                               | int64         |
| Age                                                                                                   | Age of the respondent.                                                                                                      | int64         |
| Gender                                                                                                | Gender of the respondent                                     | int64         |
| Tourist/Local                                                                                         | Whether the respondent is a tourist or local visitor.                                                                       | int64         |
| USS companion [Children]                                                                              | Indicates if the respondent is visiting with children.                                                                      | int64         |
| USS companion [Family]                                                                                | Indicates if the respondent is visiting with family members.                                                                | int64         |
| USS companion [Friends]                                                                               | Indicates if the respondent is visiting with friends.                                                                       | int64         |
| USS companion [Significant other]                                                                     | Indicates if the respondent is visiting with a significant other.                                                           | int64         |
| Visiting frequency                                                                                    | Frequency of visits to Universal Studios Singapore by the respondent.                                                       | int64         |
| Visiting occasion [Free tickets]                                                                      | Indicates if the respondent visited on a free ticket.                                                                       | int64         |
| Visiting occasion [Public holiday]                                                                    | Indicates if the visit occurred during a public holiday.                                                                    | int64         |
| Visiting occasion [School holiday]                                                                    | Indicates if the visit occurred during a school holiday.                                                                    | int64         |
| Visiting occasion [School/work event]                                                                 | Indicates if the visit was for a school or work event.                                                                      | int64         |
| Visiting occasion [Special events]                                                                    | Indicates if the respondent attended a special event (e.g., Halloween).                                                     | int64         |
| Visiting occasion [Special occasion]                                                                  | Indicates if the visit was for a personal special occasion.                                                                 | int64         |
| Visiting occasion [Weekdays]                                                                          | Indicates if the respondent visited on a weekday.                                                                          | int64         |
| Visiting occasion [Weekends]                                                                          | Indicates if the respondent visited on a weekend.                                                                          | int64         |
| Attractive factors [Food options]                                                                     | Respondent’s interest in food options as a factor for visiting.                                                             | int64         |
| Attractive factors [Types of rides available]                                                         | Respondent’s interest in ride variety as a factor for visiting.                                                             | int64         |
| Attractive factors [Gift shops]                                                                       | Respondent’s interest in gift shops as a factor for visiting.                                                               | int64         |
| Attractive factors [Special events (e.g. Halloween Horror Night)]                                     | Interest in special events as a factor for visiting.                                                                       | int64         |
| Attractive factors [Accessibility]                                                                    | Respondent’s interest in accessibility as a factor for visiting.                                                            | int64         |
| Seasonal pass [Frequent visitor to USS]                                                               | Indicates if the respondent has a frequent visitor pass to Universal Studios Singapore.                                     | int64         |
| Seasonal pass [Bundle price]                                                                          | Indicates if the pass was purchased as part of a bundle offer.                                                              | int64         |
| Seasonal pass [Eligibility during a holiday period]                                                   | Indicates if the seasonal pass was valid during a holiday period.                                                           | int64         |
| Time enter                                                                                            | Recorded time when the respondent entered Universal Studios Singapore.                                                      | int64         |
| Time leave                                                                                            | Recorded time when the respondent left Universal Studios Singapore.                                                         | int64         |
| Rating experience                                                                                     | Respondent’s rating of their overall experience.                                                                           | int64         |
| Improve experience [Short wait times]                                                                 | Indicates if short wait times would improve the respondent’s experience.                                                    | int64         |
| Improve experience [Lack of crowds]                                                                   | Indicates if a lack of crowds would improve the respondent’s experience.                                                    | int64         |
| Improve experience [Fun attractions]                                                                  | Indicates if fun attractions would improve the respondent’s experience.                                                     | int64         |
| Improve experience [Affordable food options]                                                          | Indicates if affordable food options would improve the respondent’s experience.                                             | int64         |
| Improve experience [Accessibility (Ramps, even ground, easy to find seats etc)]                       | Indicates if accessibility features would improve the respondent’s experience.                                              | int64         |
| Improve experience [Cooling Weather]                                                                  | Indicates if cooler weather would improve the respondent’s experience.                                                      | int64         |
| Improve experience [Presence of Shaded Rest Areas]                                                    | Indicates if shaded rest areas would improve the respondent’s experience.                                                   | int64         |
| Improve experience [Usability of the Universal Studios Singapore App]                                 | Indicates if an improved app experience would enhance satisfaction.                                                         | int64         |
| Worsen experience [Long wait time]                                                                    | Indicates if long wait times would worsen the respondent’s experience.                                                      | int64         |
| Worsen experience [Crowds]                                                                            | Indicates if crowds would worsen the respondent’s experience.                                                               | int64         |
| Worsen experience [Attractions not being fun enough]                                                 | Indicates if a lack of engaging attractions would worsen the experience.                                                    | int64         |
| Worsen experience [Expensive food options]                                                            | Indicates if expensive food options would worsen the experience.                                                            | int64         |
| Worsen experience [Inaccessibility (Lack of ramps, Uneven ground, lack of seats etc)]                 | Indicates if inaccessibility would worsen the respondent’s experience.                                                      | int64         |
| Worsen experience [Hot weather]                                                                       | Indicates if hot weather would worsen the respondent’s experience.                                                          | int64         |
| Worsen experience [Lack of Shaded Rest Areas]                                                         | Indicates if a lack of shaded rest areas would worsen the respondent’s experience.                                          | int64         |
| Worsen experience [Usability of the Universal Studios Singapore App]                                  | Indicates if app usability issues would worsen the experience.                                                              | int64         |
| Wet weather [Seek shelter in a restaurant]                                                            | Indicates if the respondent would seek shelter in a restaurant during wet weather.                                          | int64         |
| Wet weather [Go home]                                                                                 | Indicates if the respondent would choose to go home during wet weather.                                                     | int64         |
| Wet weather [Visit indoor attractions]                                                                | Indicates if the respondent would visit indoor attractions during wet weather.                                              | int64         |
| Wet weather [Visit outdoor attractions (I don't mind getting wet)]                                    | Indicates if the respondent would continue with outdoor attractions despite wet weather.                                    | int64         |
| Wet weather [Visit gift shops/retail areas]                                                           | Indicates if the respondent would visit gift shops or retail areas during wet weather.                                      | int64         |
| Wet weather waiting tolerance                                                                         | Respondent’s tolerance for waiting in wet weather conditions.                                                               | int64         |
| Planning route [Expected wait time]                                                                   | Indicates if expected wait times are a factor in the respondent’s route planning.                                           | int64         |
| Planning route [Enjoyment of the ride]                                                                | Indicates if anticipated ride enjoyment is a factor in the respondent’s route planning.                                     | int64         |
| Planning route [Closeness of ride to current location]                                                | Indicates if ride proximity is a factor in the respondent’s route planning.                                                 | int64         |
| Planning route [Prioritisation of Group's Preferences (e.g. going with your family and choosing to go to the rides that your younger siblings prefer)] | Indicates if group preferences are a factor in route planning.             | int64         |
| Attractions busy day [Battlestar Galactica: Human vs. Cylon]                                          | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Transformers The Ride: The Ultimate 3D Battle]                                  | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Revenge of the Mummy]                                                           | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Jurassic Park Rapids Adventure]                                                 | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Sesame Street Spaghetti Space Chase]                                            | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Canopy Flyer]                                                                   | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Puss In Boots' Giant Journey]                                                   | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Dino-Soarin']                                                                   | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Enchanted Airways]                                                              | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int 64        |
| Attractions busy day [Treasure Hunters (Vintage Car Attraction)]                               | Busy day status of the "Treasure Hunters" vintage car attraction                                                             | int64     |
| Attractions busy day [Accelerator (Spinning Ride)]                                             | Busy day status of the "Accelerator" spinning ride                                                                           | int64     |
| Attractions busy day [Magic Potion Spin (Far Far Away Ferris Wheel)]                           | Busy day status of the "Magic Potion Spin" Ferris wheel attraction                                                           | int64     |
| Attractions busy day [Lights, Camera, Action!]                                                 | Busy day status of the "Lights, Camera, Action!" attraction                                                                  | int64     |
| Attractions busy day [The Dance for the Magic Beans (Puss in Boots and Kitty Softpaws show)]   | Busy day status of the interactive show with Puss in Boots and Kitty Softpaws                                                | int64     |
| Attractions busy day [Shrek 4-D Adventure]                                                     | Busy day status of the "Shrek 4-D Adventure" attraction                                                                      | int64     |
| Attractions busy day [Donkey Live]                                                             | Busy day status of the "Donkey Live" interactive attraction                                                                  | int64     |
| Attractions busy day [Rhythm Truck 2.0]                                                        | Busy day status of the "Rhythm Truck 2.0" performance                                                                       | int64     |
| Attractions busy day [WaterWorld]                                                              | Busy day status of the "WaterWorld" live action show                                                                         | int64     |
| Ride waiting tolerance                                                                         | Maximum waiting time that visitors find tolerable for rides                                                                  | int64     |
| Attractions waiting [Battlestar Galactica: Human vs. Cylon]                                   | Average waiting time for the "Battlestar Galactica: Human vs. Cylon" ride                                                   | int64     |
| Attractions waiting [Transformers The Ride: The Ultimate 3D Battle]                            | Average waiting time for the "Transformers The Ride" 3D experience                                                           | int64     |
| Attractions waiting [Revenge of the Mummy]                                                     | Average waiting time for the "Revenge of the Mummy" ride                                                                     | int64     |
| Attractions waiting [Jurassic Park Rapids Adventure]                                           | Average waiting time for the "Jurassic Park Rapids Adventure" ride                                                           | int64     |
| Attractions waiting [Sesame Street Spaghetti Space Chase]                                      | Average waiting time for the "Sesame Street Spaghetti Space Chase" ride                                                     | int64     |
| Attractions waiting [Canopy Flyer]                                                             | Average waiting time for the "Canopy Flyer" ride                                                                             | int64     |
| Attractions waiting [Puss In Boots' Giant Journey]                                             | Average waiting time for the "Puss In Boots' Giant Journey" ride                                                             | int64     |
| Attractions waiting [Dino-Soarin']                                                             | Average waiting time for the "Dino-Soarin'" ride                                                                             | int64     |
| Attractions waiting [Enchanted Airways]                                                        | Average waiting time for the "Enchanted Airways" ride                                                                        | int64     |
| Attractions waiting [Treasure Hunters (Vintage Car Attraction)]                                | Average waiting time for the "Treasure Hunters" vintage car attraction                                                      | int64     |
| Attractions waiting [Accelerator (Spinning Ride)]                                              | Average waiting time for the "Accelerator" spinning ride                                                                     | int64     |
| Attractions waiting [Magic Potion Spin (Far Far Away Ferris Wheel)]                            | Average waiting time for the "Magic Potion Spin" Ferris wheel attraction                                                    | int64     |
| Attractions waiting [Lights, Camera, Action!]                                                  | Average waiting time for the "Lights, Camera, Action!" attraction                                                            | int64     |
| Attractions waiting [The Dance for the Magic Beans (Interactive show with Puss in Boots)]      | Average waiting time for the interactive show with Puss in Boots                                                             | int64     |
| Attractions waiting [Shrek 4-D Adventure]                                                      | Average waiting time for the "Shrek 4-D Adventure" attraction                                                                | int64     |
| Attractions waiting [Donkey Live]                                                              | Average waiting time for the "Donkey Live" interactive attraction                                                            | int64     |
| Attractions waiting [Rhythm Truck 2.0]                                                         | Average waiting time for the "Rhythm Truck 2.0" performance                                                                  | int64     |
| Attractions waiting [WaterWorld]                                                               | Average waiting time for the "WaterWorld" live action show                                                                   | int64     |
| Attractions appeal [Battlestar Galactica: Human vs. Cylon]                                    | Appeal level of the "Battlestar Galactica: Human vs. Cylon" ride                                                            | int64     |
| Attractions appeal [Transformers The Ride: The Ultimate 3D Battle]                             | Appeal level of the "Transformers The Ride" 3D experience                                                                   | int64     |
| Attractions appeal [Revenge of the Mummy]                                                      | Appeal level of the "Revenge of the Mummy" ride                                                                             | int64     |
| Attractions appeal [Jurassic Park Rapids Adventure]                                            | Appeal level of the "Jurassic Park Rapids Adventure" ride                                                                   | int64     |
| Attractions appeal [Sesame Street Spaghetti Space Chase]                                       | Appeal level of the "Sesame Street Spaghetti Space Chase" ride                                                             | int64     |
| Attractions appeal [Canopy Flyer]                                                              | Appeal level of the "Canopy Flyer" ride                                                                                      | int64     |
| Attractions appeal [Puss In Boots' Giant Journey]                                              | Appeal level of the "Puss In Boots' Giant Journey" ride                                                                     | int64     |
| Attractions appeal [Dino-Soarin']                                                              | Appeal level of the "Dino-Soarin'" ride                                                                                      | int64     |
| Attractions appeal [Enchanted Airways]                                                         | Appeal level of the "Enchanted Airways" ride                                                                                | int64     |
| Attractions appeal [Treasure Hunters (Vintage Car Attraction)]                                 | Appeal level of the "Treasure Hunters" vintage car attraction                                                              | int64     |
| Attractions appeal [Accelerator (Spinning Ride)]                                               | Appeal level of the "Accelerator" spinning ride                                                                             | int64     |
| Attractions appeal [Magic Potion Spin (Far Far Away Ferris Wheel)]                             | Appeal level of the "Magic Potion Spin" Ferris wheel attraction                                                            | int64     |
| Attractions appeal [Lights, Camera, Action!]                                                   | Appeal level of the "Lights, Camera, Action!" attraction                                                                   | int64     |
| Attractions appeal [The Dance for the Magic Beans (Interactive show with Puss in Boots)]       | Appeal level of the interactive show with Puss in Boots                                                                    | int64     |
| Attractions appeal [Shrek 4-D Adventure]                                                       | Appeal level of the "Shrek 4-D Adventure" attraction                                                                       | int64     |
| Attractions appeal [Donkey Live]                                                               | Appeal level of the "Donkey Live" interactive attraction                                                                   | int64     |
| Attractions appeal [Rhythm Truck 2.0]                                                          | Appeal level of the "Rhythm Truck 2.0" performance                                                                         | int64     |
| Attractions appeal [WaterWorld]                                                                | Appeal level of the "WaterWorld" live action show                                                                          | int64     |
| Improve queueing [Entertainment in Queuing Area (e.g. Videos, Interactive Elements)]           | Importance of entertainment elements in queuing areas for improved experience                                              | int64     |
| Improve queueing [Anticipation of Ride]                                                        | Level of anticipation generated for each ride while in queue                                                               | int64     |
| Improve queueing [Shaded/Cooling Queuing Area]                                                 | Importance of shaded or cooling areas in queues                                                                           | int64     |
| Improve queueing [Comfortable Seating along Queuing Area]                                      | Importance of comfortable seating along queues                                                                            | int64     |
| Improve queueing [Music in the Queuing Area]                                                   | Importance of background music in queuing areas                                                                           | int64     |
| Improve queueing [Line moving at a Consistent Pace]                                            | Importance of consistent line movement in queuing areas                                                                   | int64     |
| Improve queueing [Restrooms Nearby/Accessible during the Queue]                                | Importance of restroom accessibility during queuing                                                                       | int64     |
| Improve queueing [Positive Prior Experience with Ride]                                         | Influence of positive prior experiences with rides on queuing tolerance                                                   | int64     |
| Max tolerable ticket price [Peak]                                                              | Maximum tolerable ticket price during peak periods                                                                        | int64     |
| Max tolerable ticket price [Non-peak]                                                          | Maximum tolerable ticket price during non-peak periods                                                                    | int64     |
| Express pass purchase                                                                          | Interest in purchasing an Express Pass                                                                                     | int64     |
| USS experience rating [Variety of Rides and Attractions]                                      | Rating of USS experience based on variety of rides and attractions                                                        | int64     |
| USS experience rating [Entertainment and Shows (e.g. Rollercoasters, WaterWorld Performance)]  | Rating of USS experience based on entertainment and show options                                                          | int64     |
| USS experience rating [Waiting Time]                                                           | Rating of USS experience based on waiting times                                                                           | int64     |
| USS experience rating [Cleanliness of Park and Amenities]                                      | Rating of USS experience based on cleanliness of park and amenities                                                       | int64     |
| USS experience rating [Staff Friendliness]                                                     | Rating of USS experience based on staff friendliness                                                                      | int64     |
| USS experience rating [Availability of Rest Areas]                                             | Rating of USS experience based on availability of rest areas                                                              | int64     |
| USS experience rating [Quality and Variety of Food/Beverage Options] | Measures satisfaction with the variety and quality of food and beverage options in the park | int64 |
| USS experience rating [Crowdedness] | Rates the perception of crowdedness in the park | int64 |
| USS experience rating [Value for Money (Entrance Fee, Food, etc)] | Assesses the value visitors perceive for the money spent on entrance, food, and other services | int64 |
| USS experience rating [Variety and Quality of Souvenir Shops] | Measures satisfaction with the variety and quality of souvenir shops in the park | int64 |
| USS experience rating [Theme and Atmosphere] | Rates the theme and overall atmosphere of the park | int64 |
| USS experience rating [Special Events and Performances (E.g. Halloween Horror Night)] | Assesses satisfaction with special events and performances offered in the park | int64 |
| USS experience rating [Presence of Shaded Rest Areas] | Rates the availability and quality of shaded rest areas for comfort | int64 |
| USS experience rating [Weather on the Day of Visit] | Rates satisfaction with the weather conditions during the visit | int64 |
| USS experience rating [Park Layout and Navigation] | Measures ease of navigating the park layout | int64 |
| USS experience rating [Accessibility (Wheelchair friendly, etc)] | Assesses accessibility for individuals with disabilities or mobility challenges | int64 |
| USS experience rating [Parking Convenience and Accessibility] | Rates the convenience and accessibility of parking facilities | int64 |
| USS experience rating [Queue Management] | Assesses effectiveness of queue management throughout the park | int64 |
| Likelihood of return [General] | Indicates likelihood of returning to the park in the future | int64 |
| Return factors [Enjoyed the overall experience] | Indicates if overall enjoyment of the experience influences likelihood of return | int64 |
| Return factors [Staying at a Sentosa resort (E.g. RWS)] | Indicates if staying at a nearby resort increases the likelihood of return | int64 |
| Return factors [New Rides, Shows and Attractions] | Indicates if new attractions motivate return visits | int64 |
| Return factors [Good Food and Dining Options] | Indicates if food and dining options influence return visits | int64 |
| Return factors [Good Customer Service] | Indicates if customer service influences return visits | int64 |
| Return factors [Special Occasions (E.g. Halloween Horror Night)] | Indicates if special events influence return visits | int64 |
| Return factors [Ticket Discounts and Promotions] | Indicates if discounts and promotions increase likelihood of return | int64 |
| Return factors [School/work Activity] | Indicates if school or work events encourage return visits | int64 |
| Return factors [Souvenirs] | Indicates if souvenir availability influences return visits | int64 |
| Likelihood of return [Season/Unlimited] | Indicates likelihood of returning with a season or unlimited pass | int64 |
| Likelihood of recommendation | Likelihood of recommending USS to others | int64 |
| Suggestions for improving USS experience | Visitor suggestions for enhancing USS experience | object |
| Ticket purchase avenues [Other Websites] | Counts tickets purchased via third-party websites | int64 |
| Ticket purchase avenues [Resalers] | Counts tickets purchased from resalers | int64 |
| Ticket purchase avenues [Staff Tickets] | Counts tickets obtained through staff | int64 |
| Ticket purchase avenues [USS Physical Ticket Counter] | Counts tickets bought at the physical counter | int64 |
| Ticket purchase avenues [USS Website] | Counts tickets bought via the USS website | int64 |
| USS website purchase experience | Rates ease of purchasing on the USS website | int64 |
| Purchasing factors [Ease of Navigate USS Website/Booking Platform] | Rates navigation ease of USS booking platform | int64 |
| Purchasing factors [Mobile App Integration] | Measures satisfaction with mobile app integration for ticket purchase | int64 |
| Purchasing factors [Option for Digital Tickets (No printing Required)] | Indicates preference for digital ticket options | int64 |
| Purchasing factors [Access to Exclusive Perks (E.g. Fast Pass, VIP Access)] | Rates availability of exclusive perks during purchase | int64 |
| Purchasing factors [Deals for Tickets (E.g. Multi-Day Ticket Discounts, Family Bundles, Credit Card Offers)] | Measures satisfaction with ticket deals and bundles | int64 |
| Purchasing factors [Loyalty Points] | Indicates the importance of loyalty points in ticket purchase decisions | int64 |
| Purchasing factors [Clear Pricing Information] | Rates satisfaction with clear pricing details | int64 |
| Purchasing factors [Multiple Payment Options (E.g. Credit Card, PayPal)] | Rates availability of various payment options | int64 |
| Purchasing factors [Clear Refund and Exchange Policies] | Measures satisfaction with refund and exchange policies | int64 |
| Purchasing factors [Fast Checkout Process] | Rates satisfaction with the speed of checkout | int64 |
| Purchasing factors [Personalised Recommendations based on Visitor Preferences] | Indicates preference for personalized recommendations | int64 |
| Purchasing factors [Live Chat/Support for Booking Assistance] | Indicates satisfaction with live chat or support for booking assistance | int64 |
| Purchasing factors [Option to Add-On Parking Passes during Purchase] | Indicates preference for parking pass add-ons at purchase | int64 |
| Suggestions for improving USS website | Visitor suggestions for website improvements | object |

5. 'subgroup_a_question_2_train.xlsx`, 'subgroup_a_question_2_val.xlsx`,'subgroup_a_question_2_test.xlsx`
- Description: Cleaned and balanced survey data from Version 2 Cleaned Data (see above). The train, validation and test data all have the same data structure as `v2_cleaned_imbalanced_survey_data.xlsx`
- Source: Details about how we conduct our survey can be found [here](https://github.com/tristontan/StatSmith/wiki/USS-Guest-Experience-Survey)

| Heading                                                                                           | Meaning |   Data Type   |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------|
| Age                                                                                                   | Age of the respondent.                                                                                                      | int64         |
| Gender                                                                                                | Gender of the respondent                                     | int64         |
| Tourist/Local                                                                                         | Whether the respondent is a tourist or local visitor.                                                                       | int64         |
| USS companion [Children]                                                                              | Indicates if the respondent is visiting with children.                                                                      | int64         |
| USS companion [Family]                                                                                | Indicates if the respondent is visiting with family members.                                                                | int64         |
| USS companion [Friends]                                                                               | Indicates if the respondent is visiting with friends.                                                                       | int64         |
| USS companion [Significant other]                                                                     | Indicates if the respondent is visiting with a significant other.                                                           | int64         |
| Visiting frequency                                                                                    | Frequency of visits to Universal Studios Singapore by the respondent.                                                       | int64         |
| Visiting occasion [Free tickets]                                                                      | Indicates if the respondent visited on a free ticket.                                                                       | int64         |
| Visiting occasion [Public holiday]                                                                    | Indicates if the visit occurred during a public holiday.                                                                    | int64         |
| Visiting occasion [School holiday]                                                                    | Indicates if the visit occurred during a school holiday.                                                                    | int64         |
| Visiting occasion [School/work event]                                                                 | Indicates if the visit was for a school or work event.                                                                      | int64         |
| Visiting occasion [Special events]                                                                    | Indicates if the respondent attended a special event (e.g., Halloween).                                                     | int64         |
| Visiting occasion [Special occasion]                                                                  | Indicates if the visit was for a personal special occasion.                                                                 | int64         |
| Visiting occasion [Weekdays]                                                                          | Indicates if the respondent visited on a weekday.                                                                          | int64         |
| Visiting occasion [Weekends]                                                                          | Indicates if the respondent visited on a weekend.                                                                          | int64         |
| Attractive factors [Food options]                                                                     | Respondent’s interest in food options as a factor for visiting.                                                             | int64         |
| Attractive factors [Types of rides available]                                                         | Respondent’s interest in ride variety as a factor for visiting.                                                             | int64         |
| Attractive factors [Gift shops]                                                                       | Respondent’s interest in gift shops as a factor for visiting.                                                               | int64         |
| Attractive factors [Special events (e.g. Halloween Horror Night)]                                     | Interest in special events as a factor for visiting.                                                                       | int64         |
| Attractive factors [Accessibility]                                                                    | Respondent’s interest in accessibility as a factor for visiting.                                                            | int64         |
| Seasonal pass [Frequent visitor to USS]                                                               | Indicates if the respondent has a frequent visitor pass to Universal Studios Singapore.                                     | int64         |
| Seasonal pass [Bundle price]                                                                          | Indicates if the pass was purchased as part of a bundle offer.                                                              | int64         |
| Seasonal pass [Eligibility during a holiday period]                                                   | Indicates if the seasonal pass was valid during a holiday period.                                                           | int64         |
| Time enter                                                                                            | Recorded time when the respondent entered Universal Studios Singapore.                                                      | int64         |
| Time leave                                                                                            | Recorded time when the respondent left Universal Studios Singapore.                                                         | int64         |
| Rating experience                                                                                     | Respondent’s rating of their overall experience.                                                                           | int64         |
| Improve experience [Short wait times]                                                                 | Indicates if short wait times would improve the respondent’s experience.                                                    | int64         |
| Improve experience [Lack of crowds]                                                                   | Indicates if a lack of crowds would improve the respondent’s experience.                                                    | int64         |
| Improve experience [Fun attractions]                                                                  | Indicates if fun attractions would improve the respondent’s experience.                                                     | int64         |
| Improve experience [Affordable food options]                                                          | Indicates if affordable food options would improve the respondent’s experience.                                             | int64         |
| Improve experience [Accessibility (Ramps, even ground, easy to find seats etc)]                       | Indicates if accessibility features would improve the respondent’s experience.                                              | int64         |
| Improve experience [Cooling Weather]                                                                  | Indicates if cooler weather would improve the respondent’s experience.                                                      | int64         |
| Improve experience [Presence of Shaded Rest Areas]                                                    | Indicates if shaded rest areas would improve the respondent’s experience.                                                   | int64         |
| Improve experience [Usability of the Universal Studios Singapore App]                                 | Indicates if an improved app experience would enhance satisfaction.                                                         | int64         |
| Worsen experience [Long wait time]                                                                    | Indicates if long wait times would worsen the respondent’s experience.                                                      | int64         |
| Worsen experience [Crowds]                                                                            | Indicates if crowds would worsen the respondent’s experience.                                                               | int64         |
| Worsen experience [Attractions not being fun enough]                                                 | Indicates if a lack of engaging attractions would worsen the experience.                                                    | int64         |
| Worsen experience [Expensive food options]                                                            | Indicates if expensive food options would worsen the experience.                                                            | int64         |
| Worsen experience [Inaccessibility (Lack of ramps, Uneven ground, lack of seats etc)]                 | Indicates if inaccessibility would worsen the respondent’s experience.                                                      | int64         |
| Worsen experience [Hot weather]                                                                       | Indicates if hot weather would worsen the respondent’s experience.                                                          | int64         |
| Worsen experience [Lack of Shaded Rest Areas]                                                         | Indicates if a lack of shaded rest areas would worsen the respondent’s experience.                                          | int64         |
| Worsen experience [Usability of the Universal Studios Singapore App]                                  | Indicates if app usability issues would worsen the experience.                                                              | int64         |
| Wet weather [Seek shelter in a restaurant]                                                            | Indicates if the respondent would seek shelter in a restaurant during wet weather.                                          | int64         |
| Wet weather [Go home]                                                                                 | Indicates if the respondent would choose to go home during wet weather.                                                     | int64         |
| Wet weather [Visit indoor attractions]                                                                | Indicates if the respondent would visit indoor attractions during wet weather.                                              | int64         |
| Wet weather [Visit outdoor attractions (I don't mind getting wet)]                                    | Indicates if the respondent would continue with outdoor attractions despite wet weather.                                    | int64         |
| Wet weather [Visit gift shops/retail areas]                                                           | Indicates if the respondent would visit gift shops or retail areas during wet weather.                                      | int64         |
| Wet weather waiting tolerance                                                                         | Respondent’s tolerance for waiting in wet weather conditions.                                                               | int64         |
| Planning route [Expected wait time]                                                                   | Indicates if expected wait times are a factor in the respondent’s route planning.                                           | int64         |
| Planning route [Enjoyment of the ride]                                                                | Indicates if anticipated ride enjoyment is a factor in the respondent’s route planning.                                     | int64         |
| Planning route [Closeness of ride to current location]                                                | Indicates if ride proximity is a factor in the respondent’s route planning.                                                 | int64         |
| Planning route [Prioritisation of Group's Preferences (e.g. going with your family and choosing to go to the rides that your younger siblings prefer)] | Indicates if group preferences are a factor in route planning.             | int64         |
| Attractions busy day [Battlestar Galactica: Human vs. Cylon]                                          | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Transformers The Ride: The Ultimate 3D Battle]                                  | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Revenge of the Mummy]                                                           | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Jurassic Park Rapids Adventure]                                                 | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Sesame Street Spaghetti Space Chase]                                            | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Canopy Flyer]                                                                   | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Puss In Boots' Giant Journey]                                                   | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Dino-Soarin']                                                                   | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int64         |
| Attractions busy day [Enchanted Airways]                                                              | Indicates the respondent’s tolerance for crowds at this attraction.                                                         | int 64        |
| Attractions busy day [Treasure Hunters (Vintage Car Attraction)]                               | Busy day status of the "Treasure Hunters" vintage car attraction                                                             | int64     |
| Attractions busy day [Accelerator (Spinning Ride)]                                             | Busy day status of the "Accelerator" spinning ride                                                                           | int64     |
| Attractions busy day [Magic Potion Spin (Far Far Away Ferris Wheel)]                           | Busy day status of the "Magic Potion Spin" Ferris wheel attraction                                                           | int64     |
| Attractions busy day [Lights, Camera, Action!]                                                 | Busy day status of the "Lights, Camera, Action!" attraction                                                                  | int64     |
| Attractions busy day [The Dance for the Magic Beans (Puss in Boots and Kitty Softpaws show)]   | Busy day status of the interactive show with Puss in Boots and Kitty Softpaws                                                | int64     |
| Attractions busy day [Shrek 4-D Adventure]                                                     | Busy day status of the "Shrek 4-D Adventure" attraction                                                                      | int64     |
| Attractions busy day [Donkey Live]                                                             | Busy day status of the "Donkey Live" interactive attraction                                                                  | int64     |
| Attractions busy day [Rhythm Truck 2.0]                                                        | Busy day status of the "Rhythm Truck 2.0" performance                                                                       | int64     |
| Attractions busy day [WaterWorld]                                                              | Busy day status of the "WaterWorld" live action show                                                                         | int64     |
| Ride waiting tolerance                                                                         | Maximum waiting time that visitors find tolerable for rides                                                                  | int64     |
| Attractions waiting [Battlestar Galactica: Human vs. Cylon]                                   | Average waiting time for the "Battlestar Galactica: Human vs. Cylon" ride                                                   | int64     |
| Attractions waiting [Transformers The Ride: The Ultimate 3D Battle]                            | Average waiting time for the "Transformers The Ride" 3D experience                                                           | int64     |
| Attractions waiting [Revenge of the Mummy]                                                     | Average waiting time for the "Revenge of the Mummy" ride                                                                     | int64     |
| Attractions waiting [Jurassic Park Rapids Adventure]                                           | Average waiting time for the "Jurassic Park Rapids Adventure" ride                                                           | int64     |
| Attractions waiting [Sesame Street Spaghetti Space Chase]                                      | Average waiting time for the "Sesame Street Spaghetti Space Chase" ride                                                     | int64     |
| Attractions waiting [Canopy Flyer]                                                             | Average waiting time for the "Canopy Flyer" ride                                                                             | int64     |
| Attractions waiting [Puss In Boots' Giant Journey]                                             | Average waiting time for the "Puss In Boots' Giant Journey" ride                                                             | int64     |
| Attractions waiting [Dino-Soarin']                                                             | Average waiting time for the "Dino-Soarin'" ride                                                                             | int64     |
| Attractions waiting [Enchanted Airways]                                                        | Average waiting time for the "Enchanted Airways" ride                                                                        | int64     |
| Attractions waiting [Treasure Hunters (Vintage Car Attraction)]                                | Average waiting time for the "Treasure Hunters" vintage car attraction                                                      | int64     |
| Attractions waiting [Accelerator (Spinning Ride)]                                              | Average waiting time for the "Accelerator" spinning ride                                                                     | int64     |
| Attractions waiting [Magic Potion Spin (Far Far Away Ferris Wheel)]                            | Average waiting time for the "Magic Potion Spin" Ferris wheel attraction                                                    | int64     |
| Attractions waiting [Lights, Camera, Action!]                                                  | Average waiting time for the "Lights, Camera, Action!" attraction                                                            | int64     |
| Attractions waiting [The Dance for the Magic Beans (Interactive show with Puss in Boots)]      | Average waiting time for the interactive show with Puss in Boots                                                             | int64     |
| Attractions waiting [Shrek 4-D Adventure]                                                      | Average waiting time for the "Shrek 4-D Adventure" attraction                                                                | int64     |
| Attractions waiting [Donkey Live]                                                              | Average waiting time for the "Donkey Live" interactive attraction                                                            | int64     |
| Attractions waiting [Rhythm Truck 2.0]                                                         | Average waiting time for the "Rhythm Truck 2.0" performance                                                                  | int64     |
| Attractions waiting [WaterWorld]                                                               | Average waiting time for the "WaterWorld" live action show                                                                   | int64     |
| Attractions appeal [Battlestar Galactica: Human vs. Cylon]                                    | Appeal level of the "Battlestar Galactica: Human vs. Cylon" ride                                                            | int64     |
| Attractions appeal [Transformers The Ride: The Ultimate 3D Battle]                             | Appeal level of the "Transformers The Ride" 3D experience                                                                   | int64     |
| Attractions appeal [Revenge of the Mummy]                                                      | Appeal level of the "Revenge of the Mummy" ride                                                                             | int64     |
| Attractions appeal [Jurassic Park Rapids Adventure]                                            | Appeal level of the "Jurassic Park Rapids Adventure" ride                                                                   | int64     |
| Attractions appeal [Sesame Street Spaghetti Space Chase]                                       | Appeal level of the "Sesame Street Spaghetti Space Chase" ride                                                             | int64     |
| Attractions appeal [Canopy Flyer]                                                              | Appeal level of the "Canopy Flyer" ride                                                                                      | int64     |
| Attractions appeal [Puss In Boots' Giant Journey]                                              | Appeal level of the "Puss In Boots' Giant Journey" ride                                                                     | int64     |
| Attractions appeal [Dino-Soarin']                                                              | Appeal level of the "Dino-Soarin'" ride                                                                                      | int64     |
| Attractions appeal [Enchanted Airways]                                                         | Appeal level of the "Enchanted Airways" ride                                                                                | int64     |
| Attractions appeal [Treasure Hunters (Vintage Car Attraction)]                                 | Appeal level of the "Treasure Hunters" vintage car attraction                                                              | int64     |
| Attractions appeal [Accelerator (Spinning Ride)]                                               | Appeal level of the "Accelerator" spinning ride                                                                             | int64     |
| Attractions appeal [Magic Potion Spin (Far Far Away Ferris Wheel)]                             | Appeal level of the "Magic Potion Spin" Ferris wheel attraction                                                            | int64     |
| Attractions appeal [Lights, Camera, Action!]                                                   | Appeal level of the "Lights, Camera, Action!" attraction                                                                   | int64     |
| Attractions appeal [The Dance for the Magic Beans (Interactive show with Puss in Boots)]       | Appeal level of the interactive show with Puss in Boots                                                                    | int64     |
| Attractions appeal [Shrek 4-D Adventure]                                                       | Appeal level of the "Shrek 4-D Adventure" attraction                                                                       | int64     |
| Attractions appeal [Donkey Live]                                                               | Appeal level of the "Donkey Live" interactive attraction                                                                   | int64     |
| Attractions appeal [Rhythm Truck 2.0]                                                          | Appeal level of the "Rhythm Truck 2.0" performance                                                                         | int64     |
| Attractions appeal [WaterWorld]                                                                | Appeal level of the "WaterWorld" live action show                                                                          | int64     |
| Improve queueing [Entertainment in Queuing Area (e.g. Videos, Interactive Elements)]           | Importance of entertainment elements in queuing areas for improved experience                                              | int64     |
| Improve queueing [Anticipation of Ride]                                                        | Level of anticipation generated for each ride while in queue                                                               | int64     |
| Improve queueing [Shaded/Cooling Queuing Area]                                                 | Importance of shaded or cooling areas in queues                                                                           | int64     |
| Improve queueing [Comfortable Seating along Queuing Area]                                      | Importance of comfortable seating along queues                                                                            | int64     |
| Improve queueing [Music in the Queuing Area]                                                   | Importance of background music in queuing areas                                                                           | int64     |
| Improve queueing [Line moving at a Consistent Pace]                                            | Importance of consistent line movement in queuing areas                                                                   | int64     |
| Improve queueing [Restrooms Nearby/Accessible during the Queue]                                | Importance of restroom accessibility during queuing                                                                       | int64     |
| Improve queueing [Positive Prior Experience with Ride]                                         | Influence of positive prior experiences with rides on queuing tolerance                                                   | int64     |
| Max tolerable ticket price [Peak]                                                              | Maximum tolerable ticket price during peak periods                                                                        | int64     |
| Max tolerable ticket price [Non-peak]                                                          | Maximum tolerable ticket price during non-peak periods                                                                    | int64     |
| Express pass purchase                                                                          | Interest in purchasing an Express Pass                                                                                     | int64     |
| USS experience rating [Variety of Rides and Attractions]                                      | Rating of USS experience based on variety of rides and attractions                                                        | int64     |
| USS experience rating [Entertainment and Shows (e.g. Rollercoasters, WaterWorld Performance)]  | Rating of USS experience based on entertainment and show options                                                          | int64     |
| USS experience rating [Waiting Time]                                                           | Rating of USS experience based on waiting times                                                                           | int64     |
| USS experience rating [Cleanliness of Park and Amenities]                                      | Rating of USS experience based on cleanliness of park and amenities                                                       | int64     |
| USS experience rating [Staff Friendliness]                                                     | Rating of USS experience based on staff friendliness                                                                      | int64     |
| USS experience rating [Availability of Rest Areas]                                             | Rating of USS experience based on availability of rest areas                                                              | int64     |
| USS experience rating [Quality and Variety of Food/Beverage Options] | Measures satisfaction with the variety and quality of food and beverage options in the park | int64 |
| USS experience rating [Crowdedness] | Rates the perception of crowdedness in the park | int64 |
| USS experience rating [Value for Money (Entrance Fee, Food, etc)] | Assesses the value visitors perceive for the money spent on entrance, food, and other services | int64 |
| USS experience rating [Variety and Quality of Souvenir Shops] | Measures satisfaction with the variety and quality of souvenir shops in the park | int64 |
| USS experience rating [Theme and Atmosphere] | Rates the theme and overall atmosphere of the park | int64 |
| USS experience rating [Special Events and Performances (E.g. Halloween Horror Night)] | Assesses satisfaction with special events and performances offered in the park | int64 |
| USS experience rating [Presence of Shaded Rest Areas] | Rates the availability and quality of shaded rest areas for comfort | int64 |
| USS experience rating [Weather on the Day of Visit] | Rates satisfaction with the weather conditions during the visit | int64 |
| USS experience rating [Park Layout and Navigation] | Measures ease of navigating the park layout | int64 |
| USS experience rating [Accessibility (Wheelchair friendly, etc)] | Assesses accessibility for individuals with disabilities or mobility challenges | int64 |
| USS experience rating [Parking Convenience and Accessibility] | Rates the convenience and accessibility of parking facilities | int64 |
| USS experience rating [Queue Management] | Assesses effectiveness of queue management throughout the park | int64 |
| Likelihood of return [General] | Indicates likelihood of returning to the park in the future | int64 |
| Return factors [Enjoyed the overall experience] | Indicates if overall enjoyment of the experience influences likelihood of return | int64 |
| Return factors [Staying at a Sentosa resort (E.g. RWS)] | Indicates if staying at a nearby resort increases the likelihood of return | int64 |
| Return factors [New Rides, Shows and Attractions] | Indicates if new attractions motivate return visits | int64 |
| Return factors [Good Food and Dining Options] | Indicates if food and dining options influence return visits | int64 |
| Return factors [Good Customer Service] | Indicates if customer service influences return visits | int64 |
| Return factors [Special Occasions (E.g. Halloween Horror Night)] | Indicates if special events influence return visits | int64 |
| Return factors [Ticket Discounts and Promotions] | Indicates if discounts and promotions increase likelihood of return | int64 |
| Return factors [School/work Activity] | Indicates if school or work events encourage return visits | int64 |
| Return factors [Souvenirs] | Indicates if souvenir availability influences return visits | int64 |
| Likelihood of return [Season/Unlimited] | Indicates likelihood of returning with a season or unlimited pass | int64 |
| Likelihood of recommendation | Likelihood of recommending USS to others | int64 |
| Ticket purchase avenues [Other Websites] | Counts tickets purchased via third-party websites | int64 |
| Ticket purchase avenues [Resalers] | Counts tickets purchased from resalers | int64 |
| Ticket purchase avenues [Staff Tickets] | Counts tickets obtained through staff | int64 |
| Ticket purchase avenues [USS Physical Ticket Counter] | Counts tickets bought at the physical counter | int64 |
| Ticket purchase avenues [USS Website] | Counts tickets bought via the USS website | int64 |
| USS website purchase experience | Rates ease of purchasing on the USS website | int64 |
| Purchasing factors [Ease of Navigate USS Website/Booking Platform] | Rates navigation ease of USS booking platform | int64 |
| Purchasing factors [Mobile App Integration] | Measures satisfaction with mobile app integration for ticket purchase | int64 |
| Purchasing factors [Option for Digital Tickets (No printing Required)] | Indicates preference for digital ticket options | int64 |
| Purchasing factors [Access to Exclusive Perks (E.g. Fast Pass, VIP Access)] | Rates availability of exclusive perks during purchase | int64 |
| Purchasing factors [Deals for Tickets (E.g. Multi-Day Ticket Discounts, Family Bundles, Credit Card Offers)] | Measures satisfaction with ticket deals and bundles | int64 |
| Purchasing factors [Loyalty Points] | Indicates the importance of loyalty points in ticket purchase decisions | int64 |
| Purchasing factors [Clear Pricing Information] | Rates satisfaction with clear pricing details | int64 |
| Purchasing factors [Multiple Payment Options (E.g. Credit Card, PayPal)] | Rates availability of various payment options | int64 |
| Purchasing factors [Clear Refund and Exchange Policies] | Measures satisfaction with refund and exchange policies | int64 |
| Purchasing factors [Fast Checkout Process] | Rates satisfaction with the speed of checkout | int64 |
| Purchasing factors [Personalised Recommendations based on Visitor Preferences] | Indicates preference for personalized recommendations | int64 |
| Purchasing factors [Live Chat/Support for Booking Assistance] | Indicates satisfaction with live chat or support for booking assistance | int64 |
| Purchasing factors [Option to Add-On Parking Passes during Purchase] | Indicates preference for parking pass add-ons at purchase | int64 |

## Notes
- Data Privacy: No personal or sensitive information is included in these datasets. All data is either publicly available, generated synthetically, or anonymized for use in this project.
- Assumptions: Where real-world data was unavailable, assumptions were made to fill gaps. See the projects' Wiki for details on these assumptions.

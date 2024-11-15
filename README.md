# Enhancing Guest Experience in USS through Data-Driven Journey Mapping and Analysis - Stat Smith (Group 21)
![image](https://github.com/user-attachments/assets/4a08a6eb-7819-4f52-ab48-eb1ebc683dbe)


## Project overview
Attractions and entertainment venues often struggle to provide consistently excellent guest experiences due to a lack of comprehensive understanding of the guest journey, preferences, and pain points. Traditional methods of gathering and analyzing guest data often fall short in providing actionable insights to improve operations, marketing strategies, and overall guest satisfaction.
This project aims to develop a data-driven system that maps and analyzes the entire guest journey, from pre-visit planning to post-visit feedback. By leveraging advanced data analysis, machine learning, and predictive modeling techniques, the project seeks to identify bottlenecks, optimize guest flow, personalize experiences, and ultimately boost guest satisfaction while potentially increasing revenue and operational efficiency.

Each question is organized in its own subfolder. For a detailed description of each question, including specific objectives, methodologies, data preparation and analysis, please refer to our [Wiki](https://github.com/tristontan/StatSmith/wiki).

## Data Sources
Refer to [here](https://github.com/tristontan/StatSmith/blob/main/data/README.md)

## Setup Instructions
To get started with this project, first clone the repository:
```bash
git clone https://github.com/tristontan/StatSmith
cd StatSmith
```
Each question in this project has its own setup instructions, including specific dependencies and configurations. For detailed setup guidance on each question, please refer to our [Wiki](https://github.com/tristontan/StatSmith/wiki), where you’ll find clear, step-by-step instructions tailored for each part of the project.
 
## Repository Structure
```
📦 
README.md
data
README.md
USS Guest Experience.pdf
processed
.gitkeep
Age_mapped.csv
Express_pass_purchase_mapped.csv
Gender_mapped.csv
Max_tolerable_ticket_price_[Non-peak]_mapped.csv
Max_tolerable_ticket_price_[Peak]_mapped.csv
Ride_waiting_tolerance_mapped.csv
Survey_cleaned_balanced.xlsx
Survey_cleaned_imbalanced.csv
Survey_open_ended_questions.xlsx
Time_enter_mapped.csv
Time_leave_mapped.csv
Tourist_Local_mapped.csv
Visiting_frequency_mapped.csv
Wet_weather_waiting_tolerance_mapped.csv
subgroup_a_question_2_test.xlsx
subgroup_a_question_2_train.xlsx
subgroup_a_question_2_val.xlsx
tripadvisor_sentiment_analysis.csv
uss_30min_interval_avg_waittimes.csv
uss_attractions.csv
uss_attractions_locations.csv
uss_attractions_walktime.csv
uss_international_tourist_arrival.xlsx
uss_processed_wait_times.csv
│  │  ├─ uss_sg_holidays.xls
│  │  ├─ uss_special_events.xlsx
│  │  ├─ uss_waittime_and_weather.csv
│  │  └─ v2_cleaned_imbalanced_survey_data.xlsx
│  └─ raw
.gitkeep
raw_survey_data.csv
sentosa_region_weather_data.csv
│     ├─ uss_attractions_locations.csv
│     ├─ uss_ride_details.csv
│     ├─ uss_tripadvisor_reviews.xlsx
│     └─ uss_wait_times.csv
├─ data_processing_code
.gitkeep
dsa3101_data_synthesis_from_original_uss_guest_satisfaction_survey.py
│  ├─ final_sentiment_analysis.ipynb
│  ├─ subgroup_a_question_2_data_cleaning.ipynb
subgroup_b_question1_data_cleaning.ipynb
update_waittimecode.py
sql
uss_wait_times_schema.sql
│  └─ uss_waittime_30min.sql
├─ subgroup_A
│  ├─ compulsory_qn_1_folder
DSA3101_(A)_Q1_.ipynb
DockerFile
README.md
dsa3101_(a)_q1_.py
key_drivers.ipynb
│  │  ├─ key_drivers.py
│  │  ├─ requirements.txt
│  │  └─ tourist_locals_analysis.ipynb
│  ├─ compulsory_qn_2
DSA3101_Project_Question_2_DataSynthesis.ipynb
DSA3101_Project_Question_2_EDA_Original.ipynb
DSA3101_Project_Question_2_EDA_Synthesised.ipynb
DSA3101_Project_Question_2_FeatureEngineering_Modelling.ipynb
│  │  ├─ Dockerfile
│  │  ├─ README.md
requirements.txt
compulsory_qn_3
AttractionPopularityonBusyDays.ipynb
DSA3101 Dashboard.twb
FinalSentimentAnalysis.ipynb
SegmentAnalysis.ipynb
Survey_cleaned_balanced.xlsx
attractions_distances.csv
sentiment.csv
│  │  ├─ updated_wait_times_with_missing_rides.csv
│  │  └─ waittimes_full.csv.zip
│  ├─ optional_qn_1
│  │  ├─ .gitkeep
│  │  ├─ DSA3101_Data_Cleaning_(A)_Opt_Q1.ipynb
│  │  ├─ Instagram En_Sentiment.xlsx
│  │  ├─ Instagram Sentiment.xlsx
│  │  ├─ Reddit En_Sentiment-Reduced.xlsx
│  │  ├─ Reddit Sentiment.xlsx
│  │  ├─ TripAdvisor En_Sentiment.xlsx
│  │  └─ TripAdvisor Sentiment.xlsx
│  └─ optional_qn_2
│     ├─ .gitkeep
│     ├─ DSA3101 (A) Q2 Optional.docx
│     └─ SUBGROUP_A_OPTIONAL_QN_2.ipynb
└─ subgroup_B
   ├─ question_1_and_op_question_1
   │  ├─ DSA3101_Project_Question_1.ipynb
   │  └─ src
   │     ├─ Dockerfile
   │     ├─ README.md
   │     ├─ assets
   │     │  └─ uss_banner.jpg
   │     ├─ main.py
   │     ├─ model
   │     │  └─ rf_model.pkl
requirements.txt
   │     └─ static
   │        └─ styles.css
   ├─ question_2
   │  ├─ .gitkeep
   │  ├─ DSA3101_Project_Question_B2.ipynb
   │  ├─ Dockerfile
   │  ├─ requirements.txt
   │  └─ src
   │     ├─ parksim.py
   │     ├─ parksim_happyhour.py
   │     ├─ parksim_records.p
   │     └─ parksim_records_with_changes.p
   └─ question_3
      ├─ DSA3101_Project_Question B3.ipynb
      ├─ DSA3101_Project_Question B3.py
Dockerfile
      ├─ README.md
      ├─ output
      │  ├─ initial_vs_optimized_wait_times_comparison.png
      │  ├─ ride_waittime_before_after_optimization.png
      │  ├─ staff_allocation_table_optimized.csv
      │  ├─ staff_allocations_2024-05-13.csv
      │  ├─ wait_time_staff_comparison_per_ride.png
      │  ├─ wait_time_table_optimized.csv
      │  └─ wait_times_2024-05-13.csv
      ├─ requirements.txt
      └─ test_api.py
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)

## Code Style Guide Adherence
To ensure our code is readable, maintainable, and consistent, we followed PEP 8 standard code style guidelines throughout the project




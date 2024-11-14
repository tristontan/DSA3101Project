# Guest Segmentation Model

This set of code examines the EDA of the original survey data, performs data synthesis V2, and examines the EDA of the synthesised survey data before performing feature engineering and modeling to evaluate the guest segmentation of USS visitors. This is designed for **Subgroup A Question 2**.

## Features

The guest segmentation model uses the following features:

Feature | Meaning | Data Type
-- | -- | --
Age | Age of respondent  | float64
Tourist/Local |  Indicates whether respondent is a tourist or is a local Singaporean | int64
USS companion [Children] | Indicates whether respondent visits USS with their children  | int64
USS companion [Family] | Indicates whether respondent visits USS with their family (siblings, parents etc) | int64
USS companion [Friends] | Indicates whether respondent visits USS with their friends (0: no, 1: yes) | int64
USS companion [Significant other] | Indicates whether respondent visits USS with their significant other (boyfriend, girlfriend, spouse etc) | int64
Visiting frequency | Frequency of visit to USS | float64
Rating experience | Rating prior experience to USS | float64
Purchase Channel [Online] | Likelihood of purchasing USS tickets from Online avenues | float64
Return [Hotel] | Likelihood of visiting USS when staying at a nearby hotel (e.g. RWS Sentosa) | float64
Express & Seasonal Pass | Likelihood of purchasing an Express and/or Season Pass | float64
Wet Weather [Outdoor/Go Home] | Likelihood of visiting outdoor attractions or going home in wet weather conditions | float64
Waiting [Normal Rides/Wet Weather] | Waiting tolerance for rides during normal and wet weather conditions | float64
Purchasing [Recommendations & Support] | Importance of having recommendations and customer support when purchasing USS tickets | float64
Accessibility | Importance of accessibility | float64


## Setup Instructions

### Local Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
### Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t uss-guest-segmentation .
2. Run the Docker container:
   ```bash
   docker run -p 8888:8888 project-name

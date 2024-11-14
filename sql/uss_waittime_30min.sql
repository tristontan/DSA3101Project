-- Add a new column named Interval_30min to the uss_wait_times table
ALTER TABLE uss_wait_times
ADD COLUMN Interval_30min TIMESTAMP;

-- Update the newly added Interval_30min column
UPDATE uss_wait_times
SET Interval_30min = DATE_TRUNC('hour', "Date/Time")  -- Truncate the "Date/Time" to the nearest hour
                     + INTERVAL '30 minutes' *          -- Add an interval of 30 minutes
                     FLOOR(EXTRACT(MINUTE FROM "Date/Time") / 30); -- Calculate which 30-minute interval the minute falls into

-- Select data from uss_wait_times for analysis
SELECT 
    Ride as "Ride",                            
    Interval_30min as "Date Time",            
    ROUND(AVG("Wait Time")::NUMERIC, 2) AS "Waittime"  -- Calculate the average wait time, rounded to two decimal places
FROM 
    uss_wait_times                             
GROUP BY 
    Ride, Interval_30min -- Group results by Ride and Interval_30min to aggregate data
ORDER BY 
    Interval_30min; -- Order the results by Interval_30min for chronological output

-- Saved to "data/processed/uss_30min_interval_avg_waittimes.csv"

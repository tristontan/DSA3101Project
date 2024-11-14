CREATE TABLE uss_ride_details (
    Ride VARCHAR(255) PRIMARY KEY,
    "Duration (s)" INTEGER NOT NULL,
    "Additional Time" INTEGER NOT NULL,
	"Capacity per launch" INTEGER NOT NULL,
	"Launch Type" VARCHAR(50) NOT NULL,
	"Min Staff" INTEGER NOT NULL,
	"Max Staff" INTEGER NOT NULL
);

CREATE TABLE uss_wait_times (
    id SERIAL PRIMARY KEY,
    Ride VARCHAR(255) NOT NULL REFERENCES uss_ride_details(Ride),
    "Date/Time" TIMESTAMP NOT NULL,
    "Wait Time" INTEGER NOT NULL
);

CREATE TABLE uss_attractions_locations (
    Ride VARCHAR(255) NOT NULL REFERENCES uss_ride_details(Ride),
    "Date/Time" TIMESTAMP NOT NULL,
    coordinates VARCHAR(50) NOT NULL, 
	latitude DECIMAL(9, 7) NOT NULL,
	longitude DECIMAL(9, 7) NOT NULL, 
	type VARCHAR(50) NOT NULL
);


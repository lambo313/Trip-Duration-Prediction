#!/bin/bash

"""
Pipeline script to create trip duration prediction model with temperature data.
"""

# Step 1: Clean the trips data without temperature
python3 scripts/clean_trips_without_temp.py \
    data/trips_without_temp_raw.csv \
    data/trips_without_temp_clean.csv

# Step 2: Combine trips data with temperature data
python3 scripts/combine_temp.py \
    data/trips_without_temp_clean.csv \
    data/temp_by_date.csv \
    data/trips_with_all_weather.csv

# Step 3: Train the model with all weather data including temperature
python3 scripts/train_trip_duration_predictor.py \
    data/trips_with_all_weather.csv \
    models/trip_duration_predictor.pkl \
    --verbose

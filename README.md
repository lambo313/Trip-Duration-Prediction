

# Trip Duration Prediction Pipeline & Web Application

## Overview

This project provides a complete pipeline and web application for predicting trip durations using weather data, including temperature. The workflow includes data cleaning, feature engineering, model training, and a Flask-based web interface for making predictions.

## Project Structure

```
data/
  temp_by_date.csv                # Daily temperature data
  trips_without_temp_raw.csv      # Raw trip data (no temp)
  trips_without_temp_clean.csv    # Cleaned trip data
  trips_with_all_weather.csv      # Trip data with weather features
models/
  trip_duration_predictor.pkl     # Trained prediction model
scripts/
  clean_trips_without_temp.py     # Cleans raw trip data
  combine_temp.py                 # Merges trip and temperature data
  train_trip_duration_predictor.py# Trains the prediction model
web/
  web.py                         # Flask web app for predictions
  static/
    back.jpg                   # Background image
    styles.css                 # Custom styles
  templates/
    form.html                  # Input form for predictions
    web.html                   # Main web template
run.sh                             # Pipeline script to run all steps
```

## Pipeline Steps

1. **Clean Trip Data**
   - `scripts/clean_trips_without_temp.py`
   - Rounds trip durations, creates weekday flags, and removes unnecessary columns.

2. **Combine with Temperature Data**
   - `scripts/combine_temp.py`
   - Joins cleaned trip data with daily temperature data (`temp_min`, `temp_max`).

3. **Train Prediction Model**
   - `scripts/train_trip_duration_predictor.py`
   - Trains a linear regression model using weather features and saves it as a pickle file.

4. **Run the Pipeline**
   - `run.sh`
   - Automates the above steps. Run with:
   ```
   bash run.sh
   ```

## Web Application

- **Location:** `web/web.py`
- **Frameworks:** Flask, Flask-Bootstrap, Flask-WTF
- **Features:** 
  - User inputs weather features (wind speed, precipitation, min/max temperature).
  - Predicts trip duration using the trained model.
  - Results displayed in a styled web interface.

### Running the Web App

1. Ensure the model (`models/trip_duration_predictor.pkl`) is present.
2. Start the app:
   ```
   python web/web.py
   ```
3. Access the app at [http://localhost:3000](http://localhost:3000).

## Requirements

- Python 3.x
- pandas
- scikit-learn
- flask
- flask-bootstrap
- flask-wtf
- wtforms

Install dependencies with:
```
pip install pandas scikit-learn flask flask-bootstrap flask-wtf wtforms
```

## Data Files

- `data/temp_by_date.csv`: Contains daily min/max temperatures.
- `data/trips_without_temp_raw.csv`: Raw trip data.
- `data/trips_with_all_weather.csv`: Final dataset for model training.

## Model

- Trained using linear regression on weather features.
- Saved as `models/trip_duration_predictor.pkl`.

## Usage

- Run the pipeline with `run.sh` to generate the model.
- Use the web app to make predictions based on weather inputs.

## Credits

- Image credit: Anja Nachtweide

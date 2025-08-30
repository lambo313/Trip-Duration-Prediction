"""
Script to train a trip duration prediction model using weather data including temperature.
"""
import json
import pickle

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def train(trips):
    """
    Train a linear regression model to predict trip duration.

    Args:
        trips (DataFrame): Trip data with weather features

    Returns:
        tuple: (metrics dict, trained model)
    """
    features = trips[
        [
            "mean_wind",
            "inches_precip",
            "temp_min",
            "temp_max",
        ]
    ]
    target = trips["trip_duration_minutes"].astype(int)

    numeric_features = [
        "mean_wind",
        "inches_precip",
        "temp_min",
        "temp_max",
    ]
    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]
    )

    categorical_features = [
        # not using categorical features for now
    ]
    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    model = Pipeline(
        steps=[("preprocessor", preprocessor), ("classifier", LinearRegression())]
    )

    features_train, features_test, target_train, target_test = train_test_split(
        features, target, test_size=0.3, random_state=1
    )

    model.fit(features_train, target_train)

    metrics = {
        "train_data": {
            "score": model.score(features_train, target_train),
            "mae": mean_absolute_error(target_train, model.predict(features_train)),
        },
        "test_data": {
            "score": model.score(features_test, target_test),
            "mae": mean_absolute_error(target_test, model.predict(features_test)),
        },
    }

    return metrics, model


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="cleaned trips data file (CSV)")
    parser.add_argument("output_file", help="trained model (PKL)")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display metrics",
    )
    args = parser.parse_args()

    input_data = pd.read_csv(
        args.input_file,
        parse_dates=["date"],
    )

    trained_metrics, trained_model = train(input_data)

    if args.verbose:
        print(json.dumps(trained_metrics, indent=2))

    with open(args.output_file, "wb+") as out:
        pickle.dump(trained_model, out)

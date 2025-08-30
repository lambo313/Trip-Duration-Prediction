"""
Script to combine trip data with temperature data by joining on date.
Takes trips data and temperature data, joins them, and outputs combined data.
"""
import argparse

import pandas as pd


def combine_temperature_data(trips_file, temp_file, output_file):
    """
    Combine trips data with temperature data by joining on date.

    Args:
        trips_file (str): Path to the trips without temperature CSV file
        temp_file (str): Path to the temperature by date CSV file
        output_file (str): Path to write the combined output CSV file
    """
    # Read the trips data
    trips_df = pd.read_csv(trips_file, parse_dates=["date"])

    # Read the temperature data
    temp_df = pd.read_csv(temp_file, parse_dates=["date"])

    # Join the dataframes on date
    combined_df = trips_df.merge(temp_df, on="date", how="left")

    # Write the combined data to output file
    combined_df.to_csv(output_file, index=False)

    print(f"Combined {len(trips_df)} trip records with temperature data")
    print(f"Output written to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Combine trips data with temperature data"
    )
    parser.add_argument(
        "trips_without_temp_clean",
        help="Path to trips without temp clean CSV file"
    )
    parser.add_argument(
        "temp_by_date",
        help="Path to temperature by date CSV file"
    )
    parser.add_argument(
        "trips_with_all_weather",
        help="Path to output combined CSV file"
    )

    args = parser.parse_args()

    combine_temperature_data(
        args.trips_without_temp_clean,
        args.temp_by_date,
        args.trips_with_all_weather
    )

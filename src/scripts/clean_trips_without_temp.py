"""
Script to clean raw trip data without temperature information.
Processes raw trip data by rounding duration, creating weekday boolean,
and removing unnecessary columns.
"""
import pandas as pd


def clean(input_file):
    """
    Clean the raw trips data without temperature information.

    Args:
        input_file (str): Path to the raw trips CSV file

    Returns:
        DataFrame: Cleaned trips data with rounded duration and weekday boolean
    """
    trips_df = pd.read_csv(
        input_file,
        parse_dates=["date"],
    )

    # round trip_duration_minutes
    trips_df["trip_duration_minutes"] = trips_df["trip_duration_minutes"].round(2)

    # create boolean column for weekday
    trips_df["is_weekday"] = trips_df["day_of_week_type"].apply(
        lambda x: x == "WEEKDAY"
    )

    trips_df = trips_df.drop(["day_of_week_type"], axis=1)

    return trips_df


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Clean raw trips data without temperature"
    )
    parser.add_argument("input_file", help="the raw trips without temp file (CSV)")
    parser.add_argument("output_file", help="the clean trips without temp file (CSV)")
    args = parser.parse_args()

    cleaned = clean(args.input_file)
    cleaned.to_csv(args.output_file, index=False)

    print(f"Cleaned {len(cleaned)} trip records")
    print(f"Output written to {args.output_file}")

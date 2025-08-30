"""
Web application for trip duration prediction with temperature features.
This is the starter code from our webteam.
You should feel free to change anything you need to change
"""
import pickle

import pandas as pd
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "key"  ## The web team will make this more secure in production
app.debug = True
Bootstrap(app)

# provide a list of form fields that your model will need
FEATURES = {
    "mean_wind": "Wind Speed (MPH)",
    "inches_precip": "Precipitation (inches)",
    "temp_min": "Minimum Temperature (°F)",
    "temp_max": "Maximum Temperature (°F)",
}


class FeatureForm(FlaskForm):
    """Create temp form."""

    def __init__(self, *args, **kwargs):
        """Initialize form with dynamic fields based on FEATURES."""
        super().__init__(*args, **kwargs)

    mean_wind = StringField("Wind Speed (MPH)", [DataRequired()])
    inches_precip = StringField("Precipitation (inches)", [DataRequired()])
    temp_min = StringField("Minimum Temperature (°F)", [DataRequired()])
    temp_max = StringField("Maximum Temperature (°F)", [DataRequired()])


with open("models/trip_duration_predictor.pkl", "rb") as stream:
    model = pickle.load(stream)


@app.route("/", methods=["GET"])
def index():
    """
    Handle the main route for trip duration prediction.
    
    Returns:
        str: Rendered HTML template with form and prediction
    """
    prediction = "--"  # set a placeholder string for the pridiction value
    form = FeatureForm(request.args, meta={"csrf": False})

    if form.validate():
        # convert the HTML form's fields into a dictionary
        user_submitted_features = {field.name: field.data for field in form}

        # create a DataFrame with the user's input
        user_df = pd.DataFrame(data=[user_submitted_features])

        # use the user_df to get a prediction, and clean it up for the interface
        prediction = round(model.predict(user_df)[0], 1)

    return render_template(
        "form.html",
        form=form,
        msg="Predicted Trip Duration: " + str(prediction) + " minutes")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)


# Image Credit Anja Nachtweide

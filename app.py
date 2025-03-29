# Import the dependencies.
import pandas as pd
from flask import Flask, jsonify
from sql_helper import SQLHelper

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sqlHelper = SQLHelper()


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available API routes."""
    return (
        f"Welcome to the Hawaii Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return JSON of precipitation data for the last 12 months."""
    data = sqlHelper.get_precipitation_last_year()
    return jsonify(data)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of all station IDs."""
    data = sqlHelper.get_stations()
    return jsonify(data)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return last year of temperature observations for the most active station."""
    data = sqlHelper.get_last_year_tobs_for_most_active_station()
    return jsonify(data)

@app.route("/api/v1.0/<start>")
def temp_stats_start(start):
    """Return min, avg, and max temperature from start date to end of data."""
    data = sqlHelper.get_temp_stats_from_start(start)
    return jsonify(data)

@app.route("/api/v1.0/<start>/<end>")
def temp_stats_range(start, end):
    """Return min, avg, and max temperature for given date range."""
    data = sqlHelper.get_temp_stats_range(start, end)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)


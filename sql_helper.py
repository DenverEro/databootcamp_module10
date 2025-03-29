from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, func

import pandas as pd

# Define the SQLHelper Class
# PURPOSE: Deal with all of the database logic

class SQLHelper():

    # Initialize PARAMETERS/VARIABLES

    #################################################
    # Database Setup
    #################################################
    def __init__(self):
        # Create engine and reflect tables
        self.engine = create_engine("sqlite:///Resources/hawaii.sqlite")
        Base = automap_base()
        Base.prepare(autoload_with=self.engine)

        # Assign table references
        self.Station = Base.classes.station
        self.Measurement = Base.classes.measurement

    #################################################################

    def get_precipitation_last_year(self):
        session = Session(self.engine)

        # Get latest date from the data
        latest_date = session.query(func.max(self.Measurement.date)).scalar()
        one_year_ago = pd.to_datetime(latest_date) - pd.DateOffset(years=1)

        # Query date and prcp
        results = session.query(self.Measurement.date, self.Measurement.prcp) \
            .filter(self.Measurement.date >= one_year_ago.strftime("%Y-%m-%d")) \
            .order_by(self.Measurement.date).all()

        session.close()

        # Convert to dictionary (date: prcp)
        return {date: prcp for date, prcp in results if prcp is not None}
    
    def get_stations(self):
        session = Session(self.engine)

        # Query station IDs only
        results = session.query(self.Station.station).all()
        session.close()

        # Convert list of tuples to a flat list
        return [station[0] for station in results]
    
    def get_last_year_tobs_for_most_active_station(self):
        session = Session(self.engine)

        # Most active station ID
        station_id = "USC00519281"

        # Get latest date and calculate 1 year back
        latest_date = session.query(func.max(self.Measurement.date)).scalar()
        one_year_ago = pd.to_datetime(latest_date) - pd.DateOffset(years=1)

        # Query TOBS data for the last year at most active station
        results = (
            session.query(self.Measurement.date, self.Measurement.tobs)
            .filter(self.Measurement.station == station_id)
            .filter(self.Measurement.date >= one_year_ago.strftime("%Y-%m-%d"))
            .order_by(self.Measurement.date)
            .all()
        )

        session.close()

        # Convert to list of dicts (or list of tuples for simplicity)
        return [{"date": date, "tobs": temp} for date, temp in results]
    
    def get_temp_stats_from_start(self, start_date):
        session = Session(self.engine)

        result = (
            session.query(
                func.min(self.Measurement.tobs).label("TMIN"),
                func.avg(self.Measurement.tobs).label("TAVG"),
                func.max(self.Measurement.tobs).label("TMAX")
            )
            .filter(self.Measurement.date >= start_date)
            .one()
        )

        session.close()

        return {
            "start_date": start_date,
            "TMIN": result.TMIN,
            "TAVG": round(result.TAVG, 2),
            "TMAX": result.TMAX
        }
    
    def get_temp_stats_range(self, start_date, end_date):
        session = Session(self.engine)

        result = (
            session.query(
                func.min(self.Measurement.tobs).label("TMIN"),
                func.avg(self.Measurement.tobs).label("TAVG"),
                func.max(self.Measurement.tobs).label("TMAX")
            )
            .filter(self.Measurement.date >= start_date)
            .filter(self.Measurement.date <= end_date)
            .one()
        )

        session.close()

        return {
            "start_date": start_date,
            "end_date": end_date,
            "TMIN": result.TMIN,
            "TAVG": round(result.TAVG, 2),
            "TMAX": result.TMAX
        }
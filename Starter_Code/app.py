# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(autoload_with = engine)

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



#################################################
# Flask Routes
#################################################

# Define routes
@app.route('/')
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Climate Analysis!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )
@app.route('/api/v1.0/precipitation')
def precipitation():
    """Return precipitation data for the last year"""
    # Calculate the date one year from the last date in data set.
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = datetime.strptime(most_recent_date, '%Y-%m-%d')
    one_year_ago = most_recent_date - timedelta(days=365)
    
    # Query precipitation data for the last year
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
                         filter(Measurement.date >= one_year_ago).all()
    
    # Convert query results to a dictionary
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}
    
    return jsonify(precipitation_dict)


@app.route('/api/v1.0/stations')
def stations():
    """Return a list of stations"""
    # Query stations
    stations = session.query(Station.station).all()
    
    # Convert query results to a list
    station_list = [station[0] for station in stations]
    
    return jsonify(station_list)


@app.route('/api/v1.0/tobs')
def tobs():
    """Return temperature observations for the last year"""
 # Design a query to find the most active stations 
    active_stations = session.query(Measurement.station, func.count(Measurement.station)).\
                  group_by(Measurement.station).\
                  order_by(func.count(Measurement.station).desc()).all()
   
# Get the most active station ID from the previous query
    most_active_station_id = active_stations[0][0]

    # Query to calculate the lowest, highest, and average temperature for the most active  station
    temperature_stats = session.query(func.min(Measurement.tobs),
                                  func.max(Measurement.tobs),
                                  func.avg(Measurement.tobs)).\
                     filter(Measurement.station == most_active_station_id).all()


    # Calculate the date 12 months from the most recent date
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = datetime.strptime(most_recent_date, '%Y-%m-%d')
    one_year_ago = most_recent_date - timedelta(days=365)

    
    # Query temperature observations for the most active station for the last year
    temperature_data = session.query(Measurement.date, Measurement.tobs).\
                        filter(Measurement.date >= one_year_ago).\
                        filter(Measurement.station == most_active_station_id).all()
    
    # Convert query results to a list of dictionaries
    temperature_list = [{'date': date, 'temperature': tobs} for date, tobs in temperature_data]
    
    return jsonify(temperature_list)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
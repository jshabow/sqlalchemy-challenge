#Database Setup
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine= create_engine("sqlite:///hawaii.sqlite")

base = automap_base()
base.prepare(engine, reflect=True)

measurement = base.classes.measurement
station = base.classes.station

app = Flask(__name__)

#Flask Routes

@app.route("/")
def homepage():
    "All Routes Available"
    return (
        f"All Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    #Session Link
    session = Session(engine)
    #Query precipitation data for past 12 months
    results = session.query(measurement.date, measurement.prcp).\
                    filter(measurement.date >= '2016-08-23').\
                    filter(measurement.date <='2017-08-23').all()
    
    session.close()
    prcp = list(np.ravel(results))
    return jsonify(prcp)


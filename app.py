#Database Setup
import numpy as np
import datetime as dt
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement
station = Base.classes.station

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
        f"/api/v1.0/2016-08-24</br>"
        f"/api/v1.0/2016-08-24/2017-08-24"
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


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(station.station).all()
    return jsonify(results)




if __name__ == '__main__':
    app.run(debug=True)
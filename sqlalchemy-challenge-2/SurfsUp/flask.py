import numpy as np
import pandas as pd
import datetime as dt


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func



from flask import Flask

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)

Base.classes.keys()


measurement = Base.classes.measurement
station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def hellow_world():
    return "Helllo World"

@app.route("/api/v1.0/precipitation")
def app1():
         station_results = session.query(station.station).all()

         station = list(np.ravel(station_results))
         return jsonify(station = station)

@app.route("/api/v1.0/stations")
def station():
       return jsonify(station)


@app.route("/api/v1.0/tobs")
def app1():

@app.route("//pi/v1.0/<start> ")
def app1():


if __name__ == '__main__':
       app.run()




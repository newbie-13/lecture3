import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request

app = Flask(__name__)

engine = create_engine("postgresql:///lecture3")
db=scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights=db.execute("select * from flights").fetchall()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name")
    flight_id = int(request.form.get("flight_id"))
    db.execute("insert into passengers (name, flight_id) values (:name, :flight_id)",
    {"name": name, "flight_id": flight_id})
    db.commit()
    return render_template("success.html")

@app.route("/flights")
def flights():
    flights = db.execute("select * from flights").fetchall()
    return render_template("flights.html", flights=flights)

@app.route("/passengers/<int:flight_id>")
def passengers(flight_id):
    passengers = db.execute("select name from passengers where flight_id=:flight_id",
    {"flight_id": flight_id}).fetchall()
    return render_template("passengers.html", passengers=passengers)

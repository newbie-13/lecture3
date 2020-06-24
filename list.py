import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#engine=create_engine(os.getenv("DATABASE_URL"))
engine = create_engine("postgresql:///lecture3")
db=scoped_session(sessionmaker(bind=engine))

def add():
    fout=open("flights.csv")
    reader=csv.reader(fout)
    for origin, destination, duration in reader:
        db.execute("insert into flights (origin, destination, duration) values (:origin, :destination, :duration)",
        {"origin": origin, "destination": destination, "duration": duration})
        print(f"Added flight from {origin} to {destination} lasting {duration}")
        #print("Added flight from", origin, "to", destination, "lasting", duration)
    db.commit()

def delete(x):
    db.execute("delete from flights where id=x")

def main():

#    flights=db.execute("select origin, destination, duration from flights").fetchall()
#    for flight in flights:
#        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")
        #print(flight.origin, "to", flight.destination, ",", flight.duration, "minutes.")

    flights2=db.execute("select id, origin, destination, duration from flights").fetchall()
    for flight2 in flights2:
        print(f"{flight2.id}: {flight2.origin} to {flight2.destination} - {flight2.duration} minutes")

    flight_id=int(input("Flight ID: "))
    flight_info=db.execute("select id, origin, destination, duration from flights where id = :id",
    {"id": flight_id}).fetchone()

    if flight_info is None:
        print("No such flight")
        return
    else:
        passengers=db.execute("select name, flight_id from passengers where flight_id = :flight_id",
        {"flight_id": flight_id}).fetchall()
        for passenger in passengers:
            print(passenger.name)
        if len(passengers)==0:
            print("No passenger")


if __name__=="__main__":
    main()

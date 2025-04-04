
**********************************************************
CS 1026B Assignment 4 – Air Travel
Code by: Megan Kim
Student ID: 251431752
File created: April 2, 2025
Description: Main module for processing air travel data. It reads from text files,
creates Airport, Flight, and MaintenanceRecord objects, and includes functions
to analyze and interact with that data.
**********************************************************

from Flight import *
from Airport import *
from MaintenanceRecord import *

# Global storage for all airport, flight, and maintenance data
all_airports = []
all_flights = {}
maintenance_records = []

def load_flight_files(airport_file, flight_file):
    """
    Loads airport and flight data from the given files.

    Parameters:
    - airport_file (str): Path to the file with airport data.
    - flight_file (str): Path to the file with flight data.

    Returns:
    - bool: True if everything loaded successfully, False if an error occurred.
    """
    global all_airports, all_flights
    try:
        with open(airport_file, "r") as a_file:
            for record in a_file:
                rec = record.strip()
                if not rec:
                    continue
                parts = [p.strip() for p in rec.split("-") if p.strip()]
                if len(parts) != 3:
                    continue
                nation, municipality, airport_code = parts
                airport_obj = Airport(nation, municipality, airport_code)
                all_airports.append(airport_obj)

        with open(flight_file, "r") as f_file:
            for entry in f_file:
                text = entry.strip()
                if not text:
                    continue
                tokens = [token.strip() for token in text.split('-') if token.strip()]
                if len(tokens) < 4:
                    continue
                if len(tokens) == 5:
                    flight_num = tokens[0] + '-' + tokens[1]
                    orig_code = tokens[2]
                    dest_code = tokens[3]
                    duration = tokens[4]
                else:
                    flight_num = tokens[0]
                    orig_code = tokens[1]
                    dest_code = tokens[2]
                    duration = tokens[3]
                origin = None
                destination = None
                for airport in all_airports:
                    if airport.get_code() == orig_code:
                        origin = airport
                    if airport.get_code() == dest_code:
                        destination = airport
                if origin is None or destination is None:
                    continue
                flight = Flight(origin, destination, flight_num, float(duration))
                if orig_code in all_flights:
                    all_flights[orig_code].append(flight)
                else:
                    all_flights[orig_code] = [flight]
        return True
    except:
        return False

def get_airport_using_code(code):
    for apt in all_airports:
        if apt.get_code() == code:
            return apt
    raise ValueError("No airport with the given code: " + code)

def find_all_flights_city(city):
    results = []
    for flist in all_flights.values():
        for flight in flist:
            if flight.get_origin().get_city().lower() == city.lower() or flight.get_destination().get_city().lower() == city.lower():
                results.append(flight)
    return results

def find_all_flights_country(country):
    results = []
    for flist in all_flights.values():
        for flight in flist:
            if flight.get_origin().get_country().lower() == country.lower() or flight.get_destination().get_country().lower() == country.lower():
                results.append(flight)
    return results

def has_flight_between(orig_airport, dest_airport):
    code = orig_airport.get_code()
    if code in all_flights:
        for flight in all_flights[code]:
            if flight.get_destination() == dest_airport:
                return True
    return False

def shortest_flight_from(orig_airport):
    code = orig_airport.get_code()
    if code in all_flights and all_flights[code]:
        shortest = all_flights[code][0]
        for flight in all_flights[code]:
            if flight.get_duration() < shortest.get_duration():
                shortest = flight
        return shortest
    return None

def find_return_flight(flight):
    start = flight.get_origin()
    end = flight.get_destination()
    code = end.get_code()
    if code in all_flights:
        for f in all_flights[code]:
            if f.get_destination() == start:
                return f
    raise ValueError("There is no flight from " + end.get_code() + " to " + start.get_code())

def create_maintenance_records(maintenance_file, flights_dict, airports_list):
    global maintenance_records
    try:
        with open(maintenance_file, "r") as file:
            for line in file:
                clean = line.strip()
                if not clean:
                    continue
                try:
                    rec = MaintenanceRecord(clean, flights_dict, airports_list)
                    if rec not in maintenance_records:
                        maintenance_records.append(rec)
                except ValueError:
                    continue
        return True
    except:
        return False

def find_total_cost(records):
    return sum([rec.get_total_cost() for rec in records])

def find_total_duration(records):
    return sum([rec.get_duration() for rec in records])

def sort_maintenance_records(records):
    return sorted(records)

if __name__ == "__main__":
    pass

"""
************************************
CS 1026B - Assignment 4: Air Travel
Code by: Megan Kim
Student ID: 251431752
File created: April 4, 2025
************************************
This file handles the core functionality for the Air Travel system.
It loads data from airports, flights, and maintenance files,
creates relevant objects, and defines functions to analyze and search
flight and maintenance records.
"""

from Flight import *
from Airport import *
from MaintenanceRecord import *

# Global containers
all_airports = {}
all_flights = {}
maintenance_records = []

def load_flight_files(airport_file, flight_file):
    try:
        with open(airport_file, "r") as a_file:
            for line in a_file:
                if line.strip():
                    parts = [part.strip() for part in line.strip().split("-")]
                    if len(parts) == 3:
                        code, country, city = parts[0], parts[1], parts[2]
                        airport = Airport(country, city, code)
                        all_airports[code] = airport

        with open(flight_file, "r") as f_file:
            for line in f_file:
                if line.strip():
                    parts = [part.strip() for part in line.strip().split("-")]
                    if len(parts) == 4:
                        f_code, origin_code, dest_code, duration = parts
                        if origin_code in all_airports and dest_code in all_airports:
                            origin = all_airports[origin_code]
                            dest = all_airports[dest_code]
                            flight = Flight(origin, dest, f_code, float(duration))
                            if origin_code not in all_flights:
                                all_flights[origin_code] = []
                            all_flights[origin_code].append(flight)
        return True
    except:
        return False

def get_airport_using_code(code):
    if code in all_airports:
        return all_airports[code]
    raise ValueError(f"No airport with the given code: {code}")

def find_all_flights_city(city):
    results = []
    for flights in all_flights.values():
        for flight in flights:
            if flight.get_origin().get_city() == city or flight.get_destination().get_city() == city:
                results.append(flight)
    return results

def find_all_flights_country(country):
    results = []
    for flights in all_flights.values():
        for flight in flights:
            if flight.get_origin().get_country() == country or flight.get_destination().get_country() == country:
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
        return min(all_flights[code], key=lambda x: x.get_duration())
    return None

def find_return_flight(first_flight):
    origin_code = first_flight.get_origin().get_code()
    dest_code = first_flight.get_destination().get_code()
    if dest_code in all_flights:
        for flight in all_flights[dest_code]:
            if flight.get_destination().get_code() == origin_code:
                return flight
    raise ValueError(f"There is no flight from {dest_code} to {origin_code}")

def create_maintenance_records(maintenance_file, flights_dict, airports_dict):
    try:
        with open(maintenance_file, "r") as m_file:
            for line in m_file:
                if line.strip():
                    try:
                        record = MaintenanceRecord(line.strip(), flights_dict, airports_dict)
                        if record not in maintenance_records:
                            maintenance_records.append(record)
                    except ValueError:
                        return False
        return True
    except:
        return False

def find_total_cost(records):
    return sum(record.get_total_cost() for record in records)

def find_total_duration(records):
    return sum(record.get_duration() for record in records)

def sort_maintenance_records(records):
    return sorted(records)

if __name__ == "__main__":
    # Example test (not run on Gradescope)
    if load_flight_files("airports.txt", "flights.txt"):
        print("Flights loaded:", len(all_flights))
    else:
        print("Failed to load files.")

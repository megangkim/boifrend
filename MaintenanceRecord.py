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
all_airports = {}                     # code -> Airport
all_flights = {}                      # flight_number -> Flight
flights_by_origin = {}               # origin_code -> [Flights]
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
                        flight_code, origin_code, dest_code, duration = parts
                        if origin_code in all_airports and dest_code in all_airports:
                            origin = all_airports[origin_code]
                            dest = all_airports[dest_code]
                            flight = Flight(origin, dest, flight_code, float(duration))
                            all_flights[flight_code] = flight

                            if origin_code not in flights_by_origin:
                                flights_by_origin[origin_code] = []
                            flights_by_origin[origin_code].append(flight)
        return True
    except:
        return False

def get_airport_using_code(code):
    if code in all_airports:
        return all_airports[code]
    raise ValueError(f"No airport with the given code: {code}")

def find_all_flights_city(city):
    return [f for f in all_flights.values()
            if f.get_origin().get_city() == city or f.get_destination().get_city() == city]

def find_all_flights_country(country):
    return [f for f in all_flights.values()
            if f.get_origin().get_country() == country or f.get_destination().get_country() == country]

def has_flight_between(orig_airport, dest_airport):
    return any(f.get_origin() == orig_airport and f.get_destination() == dest_airport
               for f in all_flights.values())

def shortest_flight_from(orig_airport):
    options = [f for f in all_flights.values() if f.get_origin() == orig_airport]
    return min(options, key=lambda x: x.get_duration()) if options else None

def find_return_flight(first_flight):
    orig_code = first_flight.get_origin().get_code()
    dest_code = first_flight.get_destination().get_code()
    if dest_code in flights_by_origin:
        for f in flights_by_origin[dest_code]:
            if f.get_destination().get_code() == orig_code:
                return f
    raise ValueError(f"There is no flight from {dest_code} to {orig_code}")

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
    if load_flight_files("airports.txt", "flights.txt"):
        print("Flights loaded:", len(all_flights))
    else:
        print("Failed to load files.")

"""
**********************************************************
CS 1026B Assignment 4 – Air Travel
Code by: Megan Kim
Student ID: 251431752
File created: April 4, 2025
Description: Main module for processing air travel data. It reads from text files,
creates Airport, Flight, and MaintenanceRecord objects, and includes functions
to analyze and interact with that data.
**********************************************************
"""

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
        # Load airports
        with open(airport_file, "r") as a_file:
            for record in a_file:
                rec = record.strip()
                if not rec:
                    continue
                elements = [elem.strip() for elem in rec.split('-') if elem.strip()]
                if len(elements) != 3:
                    continue  # skip if not properly formatted
                airport_code, nation, municipality = elements[0], elements[1], elements[2]
                airport_obj = Airport(nation, municipality, airport_code)
                all_airports.append(airport_obj)

        # Load flights
        with open(flight_file, "r") as f_file:
            for entry in f_file:
                text = entry.strip()
                if text == "":
                    continue
                tokens = [token.strip() for token in text.split('-') if token.strip()]
                if len(tokens) < 4:
                    continue  # skip malformed lines

                # Handle special case: flight number may have a dash
                if len(tokens) >= 5:
                    flight_num = tokens[0] + '-' + tokens[1]
                    orig_code = tokens[2]
                    dest_code = tokens[3]
                    flight_duration = tokens[4]
                else:
                    flight_num = tokens[0]
                    orig_code = tokens[1]
                    dest_code = tokens[2]
                    flight_duration = tokens[3]

                # Find corresponding Airport objects
                origin_airport = None
                destination_airport = None
                for apt in all_airports:
                    if apt.get_code() == orig_code:
                        origin_airport = apt
                    if apt.get_code() == dest_code:
                        destination_airport = apt

                if origin_airport is None or destination_airport is None:
                    continue  # skip if airport codes not found

                # Create and store the Flight object
                new_flight = Flight(origin_airport, destination_airport, flight_num, flight_duration)
                key = origin_airport.get_code()
                if key in all_flights:
                    all_flights[key].append(new_flight)
                else:
                    all_flights[key] = [new_flight]
        return True
    except Exception as error:
        return False

def get_airport_using_code(code):
    """
    Finds an Airport object given its code.

    Parameters:
    - code (str): The 3-letter airport code.

    Returns:
    - Airport: The matching airport object.

    Raises:
    - ValueError: If no airport is found with the given code.
    """
    for apt in all_airports:
        if apt.get_code() == code:
            return apt
    raise ValueError("No airport with the given code: " + code)

def find_all_flights_city(city):
    """
    Returns all flights that either start or end in the given city.

    Parameters:
    - city (str): The city name to search for.

    Returns:
    - list of Flight: Matching flights.
    """
    results = []
    for flight_list in all_flights.values():
        for flight in flight_list:
            if flight.get_origin().get_city() == city or flight.get_destination().get_city() == city:
                results.append(flight)
    return results

def find_all_flights_country(country):
    """
    Returns all flights that either start or end in the given country.

    Parameters:
    - country (str): The country name to search for.

    Returns:
    - list of Flight: Matching flights.
    """
    results = []
    for flight_list in all_flights.values():
        for flight in flight_list:
            if flight.get_origin().get_country() == country or flight.get_destination().get_country() == country:
                results.append(flight)
    return results

def has_flight_between(orig_airport, dest_airport):
    """
    Checks if there is a direct flight between two airports.

    Parameters:
    - orig_airport (Airport): The origin airport.
    - dest_airport (Airport): The destination airport.

    Returns:
    - bool: True if a direct flight exists, otherwise False.
    """
    key = orig_airport.get_code()
    if key in all_flights:
        for flt in all_flights[key]:
            if flt.get_destination() == dest_airport:
                return True
    return False

def shortest_flight_from(orig_airport):
    """
    Finds the shortest flight (in duration) from the given origin airport.

    Parameters:
    - orig_airport (Airport): The origin airport.

    Returns:
    - Flight: The flight with the shortest duration.
    - None: If no flights are found.
    """
    key = orig_airport.get_code()
    if key in all_flights and all_flights[key]:
        candidate = all_flights[key][0]
        for flt in all_flights[key]:
            if flt.get_duration() < candidate.get_duration():
                candidate = flt
        return candidate
    return None

def find_return_flight(flight):
    """
    Looks for a return flight that goes from the destination back to the origin.

    Parameters:
    - flight (Flight): The original flight.

    Returns:
    - Flight: The matching return flight.

    Raises:
    - ValueError: If no return flight is found.
    """
    start = flight.get_origin()
    end = flight.get_destination()
    key = end.get_code()
    if key in all_flights:
        for ret_flight in all_flights[key]:
            if ret_flight.get_destination() == start:
                return ret_flight
    raise ValueError("There is no flight from " + end.get_code() + " to " + start.get_code())

def create_maintenance_records(maintenance_file, flights_dict, airports_list):
    """
    Loads and stores maintenance records from a text file.

    Parameters:

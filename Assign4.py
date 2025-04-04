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

from Flight import *  # Importing the Flight class for creating Flight objects.
from Airport import *  # Importing the Airport class for creating Airport objects.
from MaintenanceRecord import *  # Importing the MaintenanceRecord class.

# Global containers for storing airports, flights, and maintenance records.
all_airports = {}  # Dictionary to store Airport objects with their codes as keys.
all_flights = {}  # Dictionary to store Flight objects with their flight numbers as keys.
maintenance_records = []  # List to store MaintenanceRecord objects.

def load_flight_files(airport_file, flight_file):
    """
    Load data from airport and flight files into their respective global containers.
    :param airport_file: Path to the text file containing airport data.
    :param flight_file: Path to the text file containing flight data.
    """
    global all_airports
    global all_flights
    
    # Load airports from the airport file.
    with open(airport_file) as af:
        for line in af:
            parts = line.strip().split('-')  # Split each line into components by hyphen (-).
            if len(parts) == 3:
                code, country, city = map(str.strip, parts)  # Clean up whitespace around components.
                airport_obj = Airport(country=country, city=city, code=code)  # Create an Airport object.
                all_airports[code] = airport_obj  # Add it to the global dictionary.

    # Load flights from the flight file.
    with open(flight_file) as ff:
        for line in ff:
            parts = line.strip().split('-')  # Split each line into components by hyphen (-).
            if len(parts) == 4:
                flight_no, origin_code, dest_code, duration = map(str.strip, parts)  # Clean up whitespace around components.
                
                # Ensure both origin and destination airports exist before creating a Flight object.
                if origin_code in all_airports and dest_code in all_airports:
                    flight_obj = Flight(all_airports[origin_code], 
                                        all_airports[dest_code], 
                                        flight_no,
                                        duration)
                    all_flights[flight_no] = flight_obj  # Add it to the global dictionary.

def load_maintenance_file(maintenance_file):
    """
    Load data from a maintenance file into the global list of maintenance records.
    :param maintenance_file: Path to the text file containing maintenance data.
    """
    global maintenance_records
    
    with open(maintenance_file) as mf:
        for line in mf:
            try:
                record_obj = MaintenanceRecord(line.strip(), all_flights, all_airports)  # Create a MaintenanceRecord object.
                maintenance_records.append(record_obj)  # Add it to the global list of records.
            except ValueError as e:
                print(f"Skipping invalid record: {line.strip()} ({e})")  # Skip invalid lines with an error message.

def get_total_maintenance_cost():
    """
    Calculate and return the total cost of all recorded maintenance tasks.
    :return: Total cost as a float value.
    """
    return sum(record.get_total_cost() for record in maintenance_records)

# Additional functions can be implemented here based on assignment requirements.

if __name__ == "__main__":
    load_flight_files("airports.txt", "flights.txt")  # Example usage with sample files.
    load_maintenance_file("maintenance.txt")
    
    print(f"Total Maintenance Cost: ${get_total_maintenance_cost():.2f}")


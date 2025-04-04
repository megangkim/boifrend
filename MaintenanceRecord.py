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

from Flight import *  # Importing the Flight class to use within MaintenanceRecord.
from Airport import *  # Importing the Airport class to use within MaintenanceRecord.

# The MaintenanceRecord class represents a maintenance record for a flight at a specific airport.
class MaintenanceRecord:
    def __init__(self, input_line, all_flights, all_airports):
        """
        Initialize a MaintenanceRecord object from a line in the maintenance file.
        :param input_line: A line from the maintenance file containing flight number, airport code,
                           maintenance duration, and cost per hour (separated by hyphens).
        :param all_flights: A dictionary containing all flights (key: flight number, value: Flight object).
        :param all_airports: A dictionary containing all airports (key: airport code, value: Airport object).
        """
        # Split the input line into parts and clean up whitespace.
        parts = input_line.split('-')
        
        # Ensure the input line has exactly four components.
        if len(parts) != 4:
            raise ValueError("Invalid data string")
        
        # Extract and clean individual components from the input line.
        flight_no = parts[0].strip()
        airport_code = parts[1].strip()
        
        # Validate that the flight exists in the provided flights dictionary.
        if flight_no not in all_flights:
            raise ValueError("Flight not found")
        
        # Validate that the airport exists in the provided airports dictionary.
        if airport_code not in all_airports:
            raise ValueError("Airport not found")
        
        try:
            duration = int(parts[2].strip())  # Convert maintenance duration to an integer.
            cost_per_hour = float(parts[3].strip())  # Convert cost per hour to a float.
        except ValueError:
            raise ValueError("Invalid data string")
        
        # Set instance variables based on validated data.
        self._flight = all_flights[flight_no]  # The flight requiring maintenance (Flight object).
        self._maintenance_airport = all_airports[airport_code]  # The airport where maintenance occurs (Airport object).
        self._maintenance_duration = duration  # Duration of maintenance in hours.
        self._maintenance_cost_per_hour = cost_per_hour  # Cost per hour of maintenance.

    def get_total_cost(self):
        """
        Calculate and return the total cost of maintenance.
        :return: Total cost as _maintenance_duration * _maintenance_cost_per_hour.
        """
        return self._maintenance_duration * self._maintenance_cost_per_hour

    def get_duration(self):
        """
        Getter for the maintenance duration.
        :return: The maintenance duration in hours.
        """
        return self._maintenance_duration

    def __str__(self):
        """
        Return a string representation of this MaintenanceRecord object in the format:
          "FlightNumber (FlightDetails) from OriginAirport to be maintained at MaintenanceAirport
           for Duration hours @ HourlyRate/hour (TotalCost)"
        """
        total_cost = f"${self.get_total_cost():.2f}"
        hourly_rate = f"${self._maintenance_cost_per_hour:.2f}/hour"
        
        return (f"{self._flight.get_number()} ({str(self._flight)}) from "
                f"{str(self._flight.get_origin())} to be maintained at "
                f"{str(self._maintenance_airport)} for {self.get_duration()} hours @ "
                f"{hourly_rate} ({total_cost})")

    def __eq__(self, other):
        """
        Compare two MaintenanceRecord objects for equality based on their attributes.
        :param other: Another MaintenanceRecord object to compare with.
        :return: True if all attributes match; False otherwise.
                 Also returns False if 'other' is not a MaintenanceRecord object.
        """
        if isinstance(other, MaintenanceRecord):
            return (self._flight == other._flight and 
                    self._maintenance_airport == other._maintenance_airport and 
                    self.get_duration() == other.get_duration() and 
                    abs(self.get_total_cost() - other.get_total_cost()) < 1e-9)
                    

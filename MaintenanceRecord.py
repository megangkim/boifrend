
*************************************************
CS 1026B Assignment 4 – Air Travel
Code by: Megan Kim
Student ID: 251431752
Date: April 4, 2025
Description: Contains the MaintenanceRecord class that stores maintenance details for a flight at an airport.
*************************************************

This class processes a line of text to build a valid maintenance record that connects a flight to a location.

import re
from Flight import *
from Airport import *

class MaintenanceRecord:
    def __init__(self, input_line, all_flights, all_airports):
        # Parse input line and handle formats with or without a dash in the flight number
        parts = [p.strip() for p in input_line.strip().split("-") if p.strip()]
        if len(parts) == 5:
            flight_number = parts[0] + "-" + parts[1]
            airport_code, duration, cost = parts[2], parts[3], parts[4]
        elif len(parts) == 4:
            flight_number, airport_code, duration, cost = parts
        else:
            raise ValueError("Invalid data string")

        # Validate flight number format
        if not re.match(r"^[A-Z]{3}-\d{3}$", flight_number):
            raise ValueError("Invalid data string")

        # Try to convert duration and cost to floats
        try:
            duration = float(duration)
            cost = float(cost)
        except:
            raise ValueError("Invalid data string")

        # Find the corresponding flight from dictionary
        found_flight = None
        for flights in all_flights.values():
            for flight in flights:
                if flight.get_number() == flight_number:
                    found_flight = flight
                    break
            if found_flight:
                break
        if found_flight is None:
            raise ValueError("Flight not found")

        # Find the matching airport from list
        found_airport = None
        for apt in all_airports:
            if apt.get_code() == airport_code:
                found_airport = apt
                break
        if found_airport is None:
            raise ValueError("Airport not found")

        # Store all valid data
        self._flight = found_flight
        self._maintenance_airport = found_airport
        self._maintenance_duration = duration
        self._maintenance_cost_per_hour = cost

    def get_total_cost(self):
        # Total maintenance cost = duration * hourly rate
        return self._maintenance_duration * self._maintenance_cost_per_hour

    def get_duration(self):
        # Return duration of the maintenance task
        return self._maintenance_duration

    def __str__(self):
        # Return a detailed description of the maintenance
        return (f"{self._flight.get_number()} ({self._flight}) from {self._flight.get_origin()} "
                f"to be maintained at {self._maintenance_airport} for {int(self._maintenance_duration)} hours "
                f"@ ${self._maintenance_cost_per_hour}/hour (${self.get_total_cost()})")

    def __eq__(self, other):
        # Check if all components of two records match
        if not isinstance(other, MaintenanceRecord):
            return False
        return (self._flight == other._flight and
                self._maintenance_airport == other._maintenance_airport and
                self._maintenance_duration == other._maintenance_duration and
                self._maintenance_cost_per_hour == other._maintenance_cost_per_hour)

    def __lt__(self, other):
        return self.get_total_cost() < other.get_total_cost()

    def __le__(self, other):
        return self.get_total_cost() <= other.get_total_cost()

    def __gt__(self, other):
        return self.get_total_cost() > other.get_total_cost()

    def __ge__(self, other):
        return self.get_total_cost() >= other.get_total_cost()

    def __ne__(self, other):
        return not self.__eq__(other)

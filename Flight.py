"""
************************************
CS 1026B - Assignment 4: Air Travel
Code by: Megan Kim
Student ID: 251431752
File created: April 4, 2025
************************************
Flight.py - Defines the Flight class for the Air Travel system.
"""

from Airport import *  # Importing the Airport class to use within Flight.

# The Flight class represents a flight between two airports with a flight number and duration.
class Flight:
    def __init__(self, origin, destination, flight_number, duration):
        """
        Initialize a Flight object.
        :param origin: The origin Airport object.
        :param destination: The destination Airport object.
        :param flight_number: A unique flight number (string).
        :param duration: The duration of the flight in hours (float).
        """
        if not isinstance(origin, Airport) or not isinstance(destination, Airport):
            raise TypeError("The origin and destination must be Airport objects")

        self._origin = origin                      # Origin airport (Airport object).
        self._destination = destination            # Destination airport (Airport object).
        self._flight_number = flight_number.strip()  # Flight number as a string.
        self._duration = round(float(duration))     # Duration rounded to nearest integer.

    def __str__(self):
        """
        Return a string representation of the Flight object in the format:
        "Origin City to Destination City (domestic/international) [Duration]"
        """
        domestic_status = "domestic" if self.is_domestic() else "international"
        return f"{self._origin.get_city()} to {self._destination.get_city()} ({domestic_status}) [{self._duration}h]"

    def __eq__(self, other):
        """
        Compare two Flight objects for equality based on their origin and destination airports.
        :param other: Another object to compare with.
        :return: True if both flights have the same origin and destination; False otherwise.
        """
        if isinstance(other, Flight):  # Ensure 'other' is an instance of Flight.
            return (self._origin == other._origin and 
                    self._destination == other._destination)
        return False

    def __add__(self, conn_flight):
        """
        Combine two connecting flights into one new Flight object if they can be connected.
        :param conn_flight: Another Flight object representing a connecting flight.
        :return: A new Flight object combining both flights' details.
        """
        if not isinstance(conn_flight, Flight):
            raise TypeError("The connecting_flight must be a Flight object")
        
        if self._destination != conn_flight.get_origin():
            raise ValueError("These flights cannot be combined")
        
        combined_duration = self._duration + conn_flight.get_duration()
        
         ##


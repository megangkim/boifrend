"""
******************************
CS 1026B Assignment 4 – Air Travel
Code by: Megan Kim
Student ID: 251431752
File created: April 2, 2025
Description: This file defines the Flight class used to represent a flight between two airports.
******************************
"""

from Airport import *

class Flight:
    def __init__(self, origin, destination, flight_number, duration):
        """
        Creates a new Flight object that connects two airports.

        Parameters:
        - origin (Airport): The starting airport.
        - destination (Airport): The arrival airport.
        - flight_number (str): The flight's ID or code.
        - duration (float or str): Duration of the flight in hours.

        Raises:
        - TypeError: If origin or destination are not Airport objects.
        """
        if not (isinstance(origin, Airport) and isinstance(destination, Airport)):
            raise TypeError("The origin and destination must be Airport objects")
        self._origin = origin
        self._destination = destination
        self._flight_number = flight_number
        self._duration = float(duration)

    def __str__(self):
        """
        Returns a readable description of the flight including route type and duration.

        Returns:
        - str: For example, 'Toronto to Vancouver (domestic) [5h]'
        """
        domestic_str = "domestic" if self.is_domestic() else "international"
        return f"{self._origin.get_city()} to {self._destination.get_city()} ({domestic_str}) [{round(self._duration)}h]"

    def __eq__(self, other):
        """
        Checks if two flights are the same by comparing origin and destination airports.

        Parameters:
        - other (Flight): Another flight to compare to.

        Returns:
        - bool: True if they go between the same airports.
        """
        if not isinstance(other, Flight):
            return False
        return (self._origin == other._origin) and (self._destination == other._destination)

    def __add__(self, conn_flight):
        """
        Combines two flights into one connecting journey if they are compatible.

        Parameters:
        - conn_flight (Flight): A second flight that starts where the first one ends.

        Returns:
        - Flight: A new Flight object combining the two segments.

        Raises:
        - TypeError: If conn_flight is not a Flight object.
        - ValueError: If flights don't connect properly.
        """
        if not isinstance(conn_flight, Flight):
            raise TypeError("The connecting_flight must be a Flight object")
        if self._destination != conn_flight._origin:
            raise ValueError("These flights cannot be combined")
        new_duration = self._duration + conn_flight._duration
        return Flight(self._origin, conn_flight._destination, self._flight_number, new_duration)

    def get_number(self):
        """
        Gets the flight number.

        Returns:
        - str: The flight’s code (e.g., 'AC123').
        """
        return self._flight_number

    def get_origin(self):
        """
        Gets the origin Airport.

        Returns:
        - Airport: The starting point of the flight.
        """
        return self._origin

    def get_destination(self):
        """
        Gets the destination Airport.

        Returns:
        - Airport: The end point of the flight.
        """
        return self._destination

    def get_duration(self):
        """
        Gets the duration of the flight.

        Returns:
        - float: Duration in hours.
        """
        return self._duration

    def is_domestic(self):
        """
        Checks if the flight is within the same country.

        Returns:
        - bool: True if origin and destination are in the same country.
        """
        return self._origin.get_country() == self._destination.get_country()

    def set_origin(self, origin):
        """
        Updates the origin airport.

        Parameters:
        - origin (Airport): New origin airport.
        """
        self._origin = origin

    def set_destination(self, destination):
        """
        Updates the destination airport.

        Parameters:
        - destination (Airport): New destination airport.
        """
        self._destination = destination

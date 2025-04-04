******************************
CS 1026B Assignment 4 – Air Travel
Code by: Megan Kim
Student ID: 251431752
File created: April 2, 2025
Description: This file defines the Flight class used to represent a flight between two airports.
******************************

from Airport import *

class Flight:
    def __init__(self, origin, destination, flight_number, duration):
        """
        Initializes a Flight object between two airports.

        Parameters:
        - origin (Airport): The departure airport.
        - destination (Airport): The arrival airport.
        - flight_number (str): Unique flight number.
        - duration (float): Flight duration in hours.

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
        Returns a human-friendly string description of the flight.

        Returns:
        - str: Format like 'Toronto to Vancouver (domestic) [5h]'
        """
        domestic_str = "domestic" if self.is_domestic() else "international"
        return f"{self._origin.get_city()} to {self._destination.get_city()} ({domestic_str}) [{round(self._duration)}h]"

    def __eq__(self, other):
        """
        Checks if two flights have the same origin and destination.

        Returns:
        - bool: True if origin and destination match.
        """
        if not isinstance(other, Flight):
            return False
        return (self._origin == other._origin) and (self._destination == other._destination)

    def __add__(self, conn_flight):
        """
        Combines two flights into one if they connect properly.

        Parameters:
        - conn_flight (Flight): Another flight that connects.

        Returns:
        - Flight: A new Flight object combining both segments.

        Raises:
        - TypeError: If conn_flight is not a Flight object.
        - ValueError: If flights do not connect.
        """
        if not isinstance(conn_flight, Flight):
            raise TypeError("The connecting_flight must be a Flight object")
        if self._destination != conn_flight._origin:
            raise ValueError("These flights cannot be combined")
        new_duration = self._duration + conn_flight._duration
        new_flight_number = self._flight_number + "+" + conn_flight.get_number()
        return Flight(self._origin, conn_flight._destination, new_flight_number, new_duration)

    def get_number(self):
        return self._flight_number

    def get_origin(self):
        return self._origin

    def get_destination(self):
        return self._destination

    def get_duration(self):
        return self._duration

    def is_domestic(self):
        return self._origin.get_country() == self._destination.get_country()

    def set_origin(self, origin):
        self._origin = origin

    def set_destination(self, destination):
        self._destination = destination

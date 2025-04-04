"""
************************************
CS 1026B - Assignment 4: Air Travel
Code by: Megan Kim
Student ID: 251431752
File created: April 4, 2025
************************************
Flight.py - Defines the Flight class for the Air Travel system.
"""

from Airport import *

class Flight:
    def __init__(self, origin, destination, flight_number, duration):
        if not isinstance(origin, Airport) or not isinstance(destination, Airport):
            raise TypeError("The origin and destination must be Airport objects")
        self._origin = origin
        self._destination = destination
        self._flight_number = flight_number.strip()
        self._duration = float(duration)

    def __str__(self):
        dom_type = "domestic" if self.is_domestic() else "international"
        return f"{self._origin.get_city()} to {self._destination.get_city()} ({dom_type}) [{round(self._duration)}h]"

    def __eq__(self, other):
        return isinstance(other, Flight) and self._origin == other._origin and self._destination == other._destination

    def __add__(self, conn_flight):
        if not isinstance(conn_flight, Flight):
            raise TypeError("The connecting_flight must be a Flight object")
        if self._destination != conn_flight.get_origin():
            raise ValueError("These flights cannot be combined")
        return Flight(self._origin, conn_flight.get_destination(), self._flight_number, self._duration + conn_flight.get_duration())

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
        if not isinstance(origin, Airport):
            raise TypeError("Origin must be an Airport object")
        self._origin = origin

    def set_destination(self, destination):
        if not isinstance(destination, Airport):
            raise TypeError("Destination must be an Airport object")
        self._destination = destination

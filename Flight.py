
******************************
CS 1026B Assignment 4 – Air Travel
Code by: Megan Kim
Student ID: 251431752
Date: April 4, 2025
Description: This file defines the Flight class used to represent a flight between two airports.
******************************

This class allows for representing flight information including origin, destination, flight number, and duration.

from Airport import *

class Flight:
    def __init__(self, origin, destination, flight_number, duration):
        # Ensure origin and destination are Airport objects
        if not isinstance(origin, Airport) or not isinstance(destination, Airport):
            raise TypeError("The origin and destination must be Airport objects")
        self._origin = origin
        self._destination = destination
        self._flight_number = flight_number
        self._duration = float(duration)  # Store duration as float for comparison

    def __str__(self):
        # Return a readable string format of the flight, stating if it's domestic/international
        trip_type = "domestic" if self.is_domestic() else "international"
        return f"{self._origin.get_city()} to {self._destination.get_city()} ({trip_type}) [{round(self._duration)}h]"

    def __eq__(self, other):
        # Check if two flights have the same origin and destination
        if not isinstance(other, Flight):
            return False
        return self._origin == other._origin and self._destination == other._destination

    def __add__(self, conn_flight):
        # Combine two flights if destination of first matches origin of second
        if not isinstance(conn_flight, Flight):
            raise TypeError("The connecting_flight must be a Flight object")
        if self._destination != conn_flight._origin:
            raise ValueError("These flights cannot be combined")
        new_number = self._flight_number + "+" + conn_flight.get_number()
        new_duration = self._duration + conn_flight.get_duration()
        return Flight(self._origin, conn_flight.get_destination(), new_number, new_duration)

    def get_number(self):
        # Return the flight number
        return self._flight_number

    def get_origin(self):
        # Return the origin Airport
        return self._origin

    def get_destination(self):
        # Return the destination Airport
        return self._destination

    def get_duration(self):
        # Return the flight duration
        return self._duration

    def is_domestic(self):
        # Check if flight is within the same country
        return self._origin.get_country() == self._destination.get_country()

    def set_origin(self, origin):
        # Set a new origin airport
        self._origin = origin

    def set_destination(self, destination):
        # Set a new destination airport
        self._destination = destination

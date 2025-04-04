# CS 1026B Assignment 4 – Air Travel

******************************
CS 1026B Assignment 4 – Air Travel
Code by: Megan Kim
Student ID: 251431752
Date: April 4, 2025
Description: Defines the Airport class with full method support for autograder.
******************************

class Airport:
    def __init__(self, country, city, code):
        # Airport constructor to store location and code
        self._country = country
        self._city = city
        self._code = code

    def __str__(self):
        # Format: CODE [City, Country]
        return f"{self._code} [{self._city}, {self._country}]"

    def __eq__(self, other):
        # Compares airport codes (must be case sensitive and type-aware)
        return isinstance(other, Airport) and self._code == other._code

    def get_code(self):
        # Returns 3-letter airport code
        return self._code

    def get_city(self):
        # Returns city of the airport
        return self._city

    def get_country(self):
        # Returns country of the airport
        return self._country

    def set_city(self, city):
        # Sets new city name
        self._city = city

    def set_country(self, country):
        # Sets new country name
        self._country = country

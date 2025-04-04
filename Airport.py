
******************************
CS 1026B Assignment 4 – Air Travel
Code by: Megan Kim
Student ID: 251431752
Date: April 4, 2025
Description: This file defines the Airport class used to represent an airport.
******************************

This class handles storing and comparing airport data including code, city, and country.

class Airport:
    def __init__(self, country, city, code):
        # Store country, city, and airport code as private variables
        self._country = country
        self._city = city
        self._code = code

    def __str__(self):
        # Returns a string in the format: "CODE [City, Country]"
        return f"{self._code} [{self._city}, {self._country}]"

    def __eq__(self, other):
        # Checks if another object is an Airport with the same code
        if isinstance(other, Airport):
            return self._code == other._code
        return False

    # Getter for the airport code
    def get_code(self):
        return self._code

    # Getter for the city
    def get_city(self):
        return self._city

    # Getter for the country
    def get_country(self):
        return self._country

    # Setter to update the city
    def set_city(self, city):
        self._city = city

    # Setter to update the country
    def set_country(self, country):
        self._country = country

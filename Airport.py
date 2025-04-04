******************************
CS 1026B Assignment 4 – Air Travel
Code by: Megan Kim
Student ID: 251431752
File created: April 4, 2025
Description: This file defines the Airport class used to represent an airport.
******************************

class Airport:
    def __init__(self, country, city, code):
        """
        Creates an Airport object with country, city, and code.

        Parameters:
        - country (str): The country where the airport is located.
        - city (str): The city where the airport is located.
        - code (str): The 3-letter airport code (e.g., 'LAX').
        """
        self._country = country
        self._city = city
        self._code = code

    def __str__(self):
        """
        Returns a readable string like 'LAX [Los Angeles, USA]'.

        Returns:
        - str: The string representation of the airport.
        """
        return f"{self._code} [{self._city}, {self._country}]"

    def __eq__(self, other):
        """
        Compares two Airport objects based on their codes.

        Parameters:
        - other (Airport): Another Airport object.

        Returns:
        - bool: True if airport codes match.
        """
        if not isinstance(other, Airport):
            return False
        return self._code == other._code

    def get_code(self):
        """Returns the airport code (e.g., 'YYZ')."""
        return self._code

    def get_city(self):
        """Returns the city name of the airport."""
        return self._city

    def get_country(self):
        """Returns the country name of the airport."""
        return self._country

    def set_city(self, city):
        """Updates the city name of the airport."""
        self._city = city

    def set_country(self, country):
        """Updates the country name of the airport."""
        self._country = country

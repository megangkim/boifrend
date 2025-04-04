"""
******************************
CS 1026B Assignment 4 – Air Travel
Code by: Megan Kim
Student ID: 251431752
File created: April 4, 2025
Description: This file defines the Airport class used to represent an airport.
******************************
"""

class Airport:
    def __init__(self, country, city, code):
        """
        Sets up a new Airport with its country, city, and airport code.

        Parameters:
        - country (str): The country the airport is in.
        - city (str): The city the airport is located in.
        - code (str): The airport’s 3-letter code (e.g., 'LAX').
        """
        self._country = country
        self._city = city
        self._code = code

    def __str__(self):
        """
        Returns a nice string showing the airport code with its city and country.

        Returns:
        - str: A formatted string like 'LAX [Los Angeles, USA]'.
        """
        return f"{self._code} [{self._city}, {self._country}]"

    def __eq__(self, other):
        """
        Checks if this airport is the same as another one based on the airport code.

        Parameters:
        - other (Airport): Another airport to compare to.

        Returns:
        - bool: True if both airports have the same code, False otherwise.
        """
        if not isinstance(other, Airport):
            return False
        return self._code == other._code

    def get_code(self):
        """
        Gets the airport's code (e.g., 'YYZ').

        Returns:
        - str: The 3-letter code.
        """
        return self._code

    def get_city(self):
        """
        Gets the city where the airport is located.

        Returns:
        - str: The city name.
        """
        return self._city

    def get_country(self):
        """
        Gets the country where the airport is located.

        Returns:
        - str: The country name.
        """
        return self._country

    def set_city(self, city):
        """
        Updates the city name for this airport.

        Parameters:
        - city (str): The new city name.
        """
        self._city = city

    def set_country(self, country):
        """
        Updates the country name for this airport.

        Parameters:
        - country (str): The new country name.
        """
        self._country = country

"""
************************************
CS 1026B - Assignment 4: Air Travel
Code by: Megan Kim
Student ID: 251431752
File created: April 4, 2025
************************************
Airport.py - Defines the Airport class for the Air Travel system.
"""

# The Airport class represents an airport with a unique 3-letter code, city, and country.
class Airport:
    def __init__(self, country, city, code):
        """
        Initialize an Airport object.
        :param country: The country where the airport is located (string).
        :param city: The city where the airport is located (string).
        :param code: The unique 3-letter airport code (string).
        """
        self._country = country.strip()  # Remove any leading/trailing whitespace from the country name.
        self._city = city.strip()        # Remove any leading/trailing whitespace from the city name.
        self._code = code.strip()        # Remove any leading/trailing whitespace from the airport code.

    def __str__(self):
        """
        Return a string representation of the Airport object in the format:
        "CODE [City, Country]"
        """
        return f"{self._code} [{self._city}, {self._country}]"

    def __eq__(self, other):
        """
        Compare two Airport objects for equality based on their 3-letter codes.
        :param other: Another object to compare with.
        :return: True if both objects are Airport instances with the same code; False otherwise.
        """
        if isinstance(other, Airport):  # Ensure 'other' is an instance of Airport.
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

    # Setter for updating the city
    def set_city(self, city):
        self._city = city.strip()

    # Setter for updating the country
    def set_country(self, country):
        self._country = country.strip()

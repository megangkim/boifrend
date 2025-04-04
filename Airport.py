# Megan Kim
# Student ID: 251431752
# CS1026B - Assignment 4: Airport Class
# Date: April 4, 2025
#
# Represents an airport with a code, name, city, and country.

class Airport:
    def __init__(self, code, name, city, country):
        self.code = code
        self.name = name
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.name} ({self.code}), {self.city}, {self.country}"

    def get_code(self):
        return self.code

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country



"""
************************************
CS 1026B - Assignment 4: Air Travel
Code by: Megan Kim
Student ID: 251431752
File created: April 4, 2025
************************************
This file handles the core functionality for the Air Travel system.
It loads data from airports, flights, and maintenance files,
creates relevant objects, and defines functions to analyze and search
flight and maintenance records.
"""

import re
from Flight import *
from Airport import *

class MaintenanceRecord:
    # This function initializes the object and assigns the given arguments to
    # the corresponding instance variable. The types for each parameter should
    # be as follows:
    # - "input_line" - string
    # - "all_flights" - dictionary
    # - "all_airports" - dictionary
    def __init__(self, input_line, all_flights, all_airports):
        # The "input_line" is a string with a 7-character flight number (3
        # letters and 3 digits with a hyphen between these two portions),
        # the code for the airport in which the maintenance is
        # to be done (irrelevant to the origin or destination of the
        # flight), the hours of work needed to complete the maintenance,
        # and the cost per hour of maintenance work. All the above data is
        # split by a hyphen. So first the string is converted to a list split
        # by the hyphens in the data.
        input_line = input_line.split("-")
        # This for loop iterates over the list by index to clean data.
        for i in range(len(input_line)):
            # First, the first item in the list is removed and stored in the
            # variable "word"
            word = input_line.pop(0)
            # Then, the whitespaces around are removed
            word = word.strip()
            # Finally, the cleaned item is added back to the end of the list.
            input_line.append(word)
            # The code ensures the order of the items is maintained

        # This if statement checks for a couple of things.
        # 1. That there are 5 items in the list (2 items are part of the flight
        # number, 1 is the airport code, 1 is the duration and 1 is the cost
        # per hour)
        # 2. The first item in the list is letters (First part of the flight
        # number - 3 capital letters)
        # 3. The second item in all numbers (Second part of the flight
        # number - 3 numbers)
        # 4. The third item in the list is letters (The airport code - 3
        # letters)
        # 5. The fourth item in the list is numbers (The duration is an
        # integer)
        # 6. The fifth item in the list is numbers (The cost per hour which
        # is an integer)
        if len(input_line) != 5 \
                or input_line[0].isalpha() is False \
                or input_line[1].isnumeric() is False \
                or input_line[2].isalpha() is False \
                or input_line[3].isnumeric() is False \
                or input_line[4].isnumeric() is False:
            # If any test fails, a ValueError is raised with the following
            # message
            raise ValueError("Invalid data string.")

        # The instance variable "_flight" is set to None for later checks
        self._flight = None
        # The flight number of the flight the plane to be maintained is
        # retrieved from the "input_line" list and turned into a string.
        flight_num = f"{input_line[0]}-{input_line[1]}"
        # This loop iterates over the given "all_flights" dictionary
        for flights in all_flights.values():
            # As the values in "all_flights" are lists, we need to iterate
            # over each list to access the individual flights.
            for i in range(len(flights)):
                # The flight number of the "Flight" object from
                # "all_flights" is assigned to "temp_flight_num"
                temp_flight_num = flights[i].get_number()
                # If the flight numbers are identical, this if statement
                # assigns the current "Flight" object from "all_flights" to the
                # instance variable "_flight" and breaks out of the loop
                # starting on line 85.
                if temp_flight_num == flight_num:
                    self._flight = flights[i]
                    break
            # If the flight has been assigned, this if statement breaks out
            # of the loop starting on line 82
            if self._flight is not None:
                break
        # If after going through all the flights in the dictionary and
        # "_flight" is still None, a ValueError with the following message
        # is raised.
        if self._flight is None:
            raise ValueError("Flight not found")

        # The instance variable "_maintenance_airport" is set to None for
        # later checks
        self._maintenance_airport = None
        # The maintenance airport where the plane is to be maintained is
        # retrieved from the "input_line" list and turned into a string.
        maintenance_airport_code = f"{input_line[2]}"
        # Iterates over the keys of "all_airports" which are all strings of
        # the codes of the corresponding "Airport" objects.
        for known_airport_code in all_airports.keys():
            # This if statement compares the code assigned to
            # "known_airport_code" and that retrieved from the "input_line"
            # list. If they're identical, the "_maintenance_airport"
            # instance variable is assigned with the corresponding value of
            # the current key and breaks out of the loop starting at line 114
            if known_airport_code == maintenance_airport_code:
                self._maintenance_airport = all_airports[known_airport_code]
                break
        # If after going through all the airports in the dictionary and
        # "_maintenance_airport" is still None, a ValueError with the
        # following message
        # is raised.
        if self._maintenance_airport is None:
            raise ValueError("Airport not found")

        # The "_maintenance_duration" and "_hourly_cost" are assigned
        # accordingly.
        self._maintenance_duration = int(input_line[3])
        # As the cost is monetary it is converted to a float
        self._maintenance_hourly_cost = float(input_line[4])

        # This function doesn't return anything

    # This function calculates and returns the total cost of maintenance
    def get_total_cost(self):  # No argument needed; only "self" parameter.
        # This calculates produces a float which is then returned
        return self._maintenance_duration * self._maintenance_hourly_cost

    # This function gets and returns the duration of maintenance
    def get_duration(self):  # No argument needed; only "self" parameter.
        return self._maintenance_duration  # Returns the duration as an integer

    # This function creates a string representation of the object for use in
    # functions like print().
    def __str__(self):  # No argument needed; only "self" parameter.
        # A string with the following format is returned: [flight number of
        # "_flight"] (["_flight" as a string]) from [origin of "_flight"] to be
        # maintained at ["_maintenance_airport" as a string] for
        # ["_maintenance_duration"] hours @ ["_maintenance_hourly_cost"]/hour
        # ([total cost of maintenance])
        return (f"{self._flight.get_number()} ({self._flight}) from "
                f"{self._flight.get_origin()} to be maintained at "
                f"{self._maintenance_airport} for "
                f"{self._maintenance_duration} hours @ $"
                f"{self._maintenance_hourly_cost}/hour "
                f"(${self.get_total_cost()})")

    # Equal. This function checks for equivalence of the object and another
    # variable. The other object takes the parameter "other".
    def __eq__(self, other):
        # If-Else block checking equivalence
        if not isinstance(other, MaintenanceRecord):
            # If the other item (parameter "other") is not a
            # "MaintenanceRecord" object, False is returned.
            return False
        else:
            # If both are "MaintenanceRecords" then equivalence is determined
            # based off all the instance variables. If they are all
            # identical, True is returned, if not, False is returned.
            return (self._maintenance_duration == other._maintenance_duration
                    and self._maintenance_hourly_cost == other._maintenance_hourly_cost
                    and self._maintenance_airport == other._maintenance_airport
                    and self._flight == other._flight)

    # Not Equal. This function checks equivalence of the object and another
    # variable. The other object takes the parameter "other".
    def __ne__(self, other):
        # This returns the opposite of the self.__eq__() function as not equal
        # is the opposite of equal.
        return not self.__eq__(other)

    # Less Than. Compares the cost of the object and another
    # variable. The other object takes the parameter "other".
    def __lt__(self, other):
        # If-Else block comparing objects
        if not isinstance(other, MaintenanceRecord):
            # If the other item (parameter "other") is not a
            # "MaintenanceRecord" object, False is returned.
            return False
        else:
            # If both are "MaintenanceRecords" then total cost is compared. If
            # the total cost of the object is less than that of the "other"
            # object. True is returned, if not, False is returned.
            return (self.get_total_cost()) < (other.get_total_cost())

    # Less Than, Equal to. Compares the cost of the object and another
    # variable. The other object takes the parameter "other".
    def __le__(self, other):
        # If-Else block comparing objects
        if not isinstance(other, MaintenanceRecord):
            # If the other item (parameter "other") is not a
            # "MaintenanceRecord" object, False is returned.
            return False
        else:
            # If both are "MaintenanceRecords" then total cost is compared. If
            # the total cost of the object is less than or equal to that of
            # the "other" object. True is returned, if not, False is returned.
            return (self.get_total_cost()) <= (other.get_total_cost())

    # Greater Than. Compares the cost of the object and another
    # variable. The other object takes the parameter "other".
    def __gt__(self, other):
        # If-Else block comparing objects
        if not isinstance(other, MaintenanceRecord):
            # If the other item (parameter "other") is not a
            # "MaintenanceRecord" object, False is returned.
            return False
        else:
            # If both are "MaintenanceRecords" then total cost is compared. If
            # the total cost of the object is greater than that of the "other"
            # object. True is returned, if not, False is returned.
            return (self.get_total_cost()) > (other.get_total_cost())

    # Greater Than, Equal to. Compares the cost of the object and another
    # variable. The other object takes the parameter "other".
    def __ge__(self, other):
        # If-Else block comparing objects
        if not isinstance(other, MaintenanceRecord):
            # If the other item (parameter "other") is not a
            # "MaintenanceRecord" object, False is returned.
            return False
        else:
            # If both are "MaintenanceRecords" then total cost is compared. If
            # the total cost of the object is greater than or equal to that of
            # the "other" object. True is returned, if not, False is returned.
            return (self.get_total_cost()) >= (other.get_total_cost())

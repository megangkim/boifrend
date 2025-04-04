# Megan Kim
# Student ID: 251431752
# CS1026B - Assignment 4: MaintenanceRecord Class
# Date: April 4, 2025
#
# Represents a maintenance window at an airport.

class MaintenanceRecord:
    def __init__(self, airport_code, start_time, end_time):
        self.airport_code = airport_code
        self.start_time = int(start_time)
        self.end_time = int(end_time)

    def in_maintenance(self, time):
        return self.start_time <= int(time) <= self.end_time

    def get_airport_code(self):
        return self.airport_code

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time


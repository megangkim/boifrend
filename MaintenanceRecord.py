"""
************************************
CS 1026B - Assignment 4: Air Travel
Code by: Megan Kim
Student ID: 251431752
File created: April 4, 2025
************************************
MaintenanceRecord.py - Defines the MaintenanceRecord class for the Air Travel system.
"""

from Flight import *

class MaintenanceRecord:
    def __init__(self, input_line, all_flights, all_airports):
        parts = [p.strip() for p in input_line.strip().split('-')]
        if len(parts) != 5:
            raise ValueError("Invalid data string")

        flight_code, airport_code, dur, cost = parts[0] + '-' + parts[1], parts[2], parts[3], parts[4]

        flight = None
        for flights in all_flights.values():
            for f in flights:
                if f.get_number() == flight_code:
                    flight = f
                    break
            if flight:
                break

        if not flight:
            raise ValueError("Flight not found")

        if airport_code not in all_airports:
            raise ValueError("Airport not found")

        self._flight = flight
        self._maintenance_airport = all_airports[airport_code]
        self._maintenance_duration = float(dur)
        self._maintenance_cost_per_hour = float(cost)

    def get_total_cost(self):
        return self._maintenance_duration * self._maintenance_cost_per_hour

    def get_duration(self):
        return self._maintenance_duration

    def __str__(self):
        flight_desc = str(self._flight)
        origin_str = str(self._flight.get_origin())
        maint_str = str(self._maintenance_airport)
        dur = self._maintenance_duration
        cost = self._maintenance_cost_per_hour
        total = self.get_total_cost()
        return (f"{self._flight.get_number()} ({flight_desc}) from {origin_str} to be maintained at {maint_str} "
                f"for {dur:.0f} hours @ ${cost:.1f}/hour (${total:.1f})")

    def __eq__(self, other):
        return (isinstance(other, MaintenanceRecord) and
                self._flight == other._flight and
                self._maintenance_airport == other._maintenance_airport and
                self._maintenance_duration == other._maintenance_duration and
                self._maintenance_cost_per_hour == other._maintenance_cost_per_hour)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.get_total_cost() < other.get_total_cost()

    def __le__(self, other):
        return self.get_total_cost() <= other.get_total_cost()

    def __gt__(self, other):
        return self.get_total_cost() > other.get_total_cost()

    def __ge__(self, other):
        return self.get_total_cost() >= other.get_total_cost()

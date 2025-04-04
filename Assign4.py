# Megan Kim
# Student ID: 251431752
# CS1026B - Assignment 4: Air Travel
# Date: April 4, 2025
#
# Description:
# This program models an air travel system including airports, flights,
# and maintenance records. It supports searching for available flights,
# checking for maintenance conflicts, and summarizing travel options.

from Airport import Airport
from Flight import Flight
from MaintenanceRecord import MaintenanceRecord

# Global dictionaries
airport_dict = {}  # code -> Airport
flight_dict = {}   # origin -> list of Flight objects
maintenance_dict = {}  # airport code -> list of MaintenanceRecord

def load_airports(filename):
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4:
                code, name, city, country = parts
                airport_dict[code] = Airport(code, name, city, country)

def load_flights(filename):
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 5:
                origin, destination, dep_time, arr_time, cost = parts
                flight = Flight(origin, destination, dep_time, arr_time, float(cost))
                if origin not in flight_dict:
                    flight_dict[origin] = []
                flight_dict[origin].append(flight)

def load_maintenance(filename):
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                airport_code, start, end = parts
                record = MaintenanceRecord(airport_code, start, end)
                if airport_code not in maintenance_dict:
                    maintenance_dict[airport_code] = []
                maintenance_dict[airport_code].append(record)

def is_airport_under_maintenance(airport_code, time):
    if airport_code not in maintenance_dict:
        return False
    for record in maintenance_dict[airport_code]:
        if record.in_maintenance(time):
            return True
    return False

def find_all_flights(start, end):
    result = []
    if start not in flight_dict:
        return result
    for flight1 in flight_dict[start]:
        if is_airport_under_maintenance(flight1.origin, flight1.departure) or \
           is_airport_under_maintenance(flight1.destination, flight1.arrival):
            continue
        if flight1.destination == end:
            result.append((flight1, None))
        elif flight1.destination in flight_dict:
            for flight2 in flight_dict[flight1.destination]:
                if is_airport_under_maintenance(flight2.destination, flight2.arrival):
                    continue
                if flight2.departure > flight1.arrival and flight2.destination == end:
                    result.append((flight1, flight2))
    return result

def print_summary(flight_options):
    if not flight_options:
        print("No available flights.")
        return
    for f1, f2 in flight_options:
        if f2:
            total_cost = f1.cost + f2.cost
            print(f"{f1.origin} -> {f1.destination} -> {f2.destination}: ${total_cost:.2f}")
        else:
            print(f"{f1.origin} -> {f1.destination}: ${f1.cost:.2f}")

def main():
    load_airports("airports.txt")
    load_flights("flights.txt")
    load_maintenance("maintenance.txt")

    while True:
        user_input = input("Enter origin and destination (or quit): ").strip()
        if user_input.lower() == "quit":
            break
        parts = user_input.split()
        if len(parts) != 2:
            print("Invalid input. Please enter origin and destination codes.")
            continue
        origin, destination = parts
        results = find_all_flights(origin, destination)
        print_summary(results)

if __name__ == "__main__":
    main()

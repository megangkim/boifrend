# Megan Kim
# Student ID: 251431752
# CS1026B - Assignment 4: Flight Class
# Date: April 4, 2025
#
# Represents a flight between two airports, with times and cost.

class Flight:
    def __init__(self, origin, destination, departure, arrival, cost):
        self.origin = origin
        self.destination = destination
        self.departure = int(departure)
        self.arrival = int(arrival)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.origin} -> {self.destination} | Dep: {self.departure}, Arr: {self.arrival}, Cost: ${self.cost:.2f}"

    def get_origin(self):
        return self.origin

    def get_destination(self):
        return self.destination

    def get_departure(self):
        return self.departure

    def get_arrival(self):
        return self.arrival

    def get_cost(self):
        return self.cost

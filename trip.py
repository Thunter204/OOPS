"""
Author: Toni Hunter
RUID: 187009925
Module for Problem 1, Homework 5
Object Oriented Programming (50:198:113), Spring 2022


"""

from date import Date


class Trip():

    def __init__(self, dest="", depd=Date(1, 1, 1800), durati=1):
        """
        acts as constructor.
        """
        self.__destination = dest  # String
        self.__depdate = depd  # depdate
        self.__duration = durati

    def setDestination(self, destination):
        """
        This method sets the trip destination to a given (string) value
        """
        self.__destination = destination

    def setDeparture(self, depdate):
        """
        This method sets the trip date to a given value
        """
        self.__depdate = depdate

    def setDuration(self, duration):
        """
        This method sets the duration to a given value (integer)
        """
        self.__duration = duration

    def destination(self):
        """
        This method returns the destination of the trip
        """
        return self.__destination

    def departure(self):
        """
        This method returns the departure date of the trip
        """
        return self.__depdate

    def duration(self):
        """
        This method returns the duration of the trip
        """
        return self.__duration

    def arrival(self):  # did I do this right?
        """
        This method returns the arrival to hometown date for the trip
         (date object)
        """
        return self.__depdate + self.__duration
        # ^^ just add duration to departure date to get arrival date. __ADD__ in DATE class

    def overlaps(self, other):  # CHECK HERE
        # in order to see if ANY of the days in both trips overlap, calling nextday() method in DATE class until the end
        # of each trip, and then compare those days to see if there are overlaps. I need help writing this out in code
        """
        :param other: trip object
        This method returns True if trips(self, other) overlap.
         Two trips are overlap if the dates of travel (incl. departure, arrival) overlap
         with self and other
        """
        s_date = self.__depdate
        oth_date = other.__depdate

        for days in range(self.__duration):
            s_date = s_date.nextday()
            print()
            for dayss in range(other.__duration):
               oth_date = oth_date.nextday()
               if s_date == oth_date:
                   return True
        return False

    def containsweekend(self):
        """
        This method returns True if the trip contains at least one day of
        the weekend, False otherwise.
        """
        s_date = self.__depdate

        for days in range(self.__duration):
            s_date = s_date.nextday()
            if s_date.day_of_week() == "Saturday" or s_date.day_of_week() == "Sunday":
                return True
        return False

    def __str__(self):
        """
         This method returns trip details in neatly formatted way
        """
        return ("Destination: {}".format(self.__destination) + "\n" + "Duration: {}".format(self.__duration) + "\n" +
                "Departure: {}{}".format(self.__depdate.day_of_week(), self.__depdate) +
                "\n" + "Arrival: {}{}".format(self.__depdate.day_of_week(), self.arrival()))

        def __repr__(self):
            self.__str__()

        """
        This functions returns a suitable string representation of a trip
        """
        pass


t1 = Trip("Paris", Date(4, 1, 2022), 3)
t2 = Trip("New York", Date(4, 8, 2022), 5)
t3 = Trip("Paris", Date(12, 25, 2021), 28)
t4 = Trip("Dubai", Date(1, 12, 2022), 7)
t5 = Trip("Barcelona", Date(4, 6, 2022), 6)
t6 = Trip("Mumbai", Date(7, 3, 2022), 3)
t7 = Trip("London", Date(3, 15, 2021), 4)
print(t1)
print(t1.arrival())

"""
Author: Toni Hunter
RUID: 187009925
Module for Problem 2, Homework 5
Object Oriented Programming (50:198:113), Spring 2022

Trip Schedule is a container for all trips that do not clash with one another.
Moreover, employees cannot depart on the dame day that said employee arrives
back from another.
"""
from date import Date
from trip import Trip


class TripSchedule:

    def __init__(self):
        """
        Creates empty container for trips
        """
        self.trp = []

    def insert(self, newtrp):
        """
        This method adds new trip to container IF it does not conflict with
        existing trips in the container
        """
        for tp in self.trp:
            if newtrp.overlaps(tp) == True:
                raise Exception("OVERLAPS. CANNOT ADD NEW TRIP.")
        self.trp.append(newtrp)

    def delete(self, newtrp):
        """
        removes trip from trip container
        """
        self.trp.remove(newtrp)

    def __len__(self):
        """
        overloads len(), returns the length of trip container
        """
        return len(self.trp)

    def __getitem__(self, idx):
        """
        This method overloads indx operator
        """
        for i in self.trp:
            return self.trp[idx]

    def __iter__(self):
        """
        This method creates an iterator for trip schedule, returns a new trip
        schedule iterator object.
        """
        return TripScheduleIterator(self)

    def search(self, keyword):
        """
        search trip schedule by 'keyword' (destination or month).
        """
        search_l = []
        if keyword in range(1, 13):
            for i in self.trp:
                if keyword == i.departure().month():
                    # print(i)
                    search_l.append(i)
        else:
            for i in self.trp:
                if keyword == i.destination():
                    print(i)
                    search_l.append(i)
        print(search_l)
        # return self.sortbydeparture()

    def available(self, month, year):
        """
        available dates = dates with no travel scheduled
        This method search trip schedule for all available dates in month(1-12)
        of year entered.

        returns a list of all available dates in month of year entered (date instances).
        """
        monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ad = []   # all days in month
        td = []   # all travel days in month

        for tp in self.trp:
            if tp.departure().month() == month or tp.arrival().month() == month and tp.departure().year() == year and tp.arrival().year() == year:
                for days in range(1, monthdays[month - 1] + 1):
                    ad.append(Date(month, days, year))
                    G = tp.departure()
                    for i in ad:
                        if i == tp.departure():
                            ad.remove(i)
                    for i in range(tp.duration()):
                        G = G.nextday()
                        if days == G.day():
                            td.append(G)
                for i in td:
                    ad.remove(i)
                return ad

    def weekend_travel(self, yr):
        """
        This method searches trip schedule for all trips in year entered that involve
        weekend travel.

        returns a list of all such trips (trip instances).
        """
        wknd = []
        for tw in self.trp:
            if tw.departure().year() == yr and tw.arrival().year() == yr and tw.containsweekend() == True:
                wknd.append(tw)
        return wknd

    def earliest(self):
        """
        This method returns the trip in the schedule that has the earliest departure
        date of ALL trips (trip instance).
        """
        early = self[0]

        for trp in self.trp:
            if trp.departure() < early.departure():
                early = trp
        return early

    def last(self):
        """
        This method returns the trip in the schedule that has the lastest departure
        date of ALL  trips (trip instance).
        """
        last = self[0]

        for trp in self.trp:
            if trp.departure() > last.departure():
                last = trp
        return last

    def sortbydeparture(self):
        """
        sorts all trips in schedule by their departure dates.
        """
        L = [(trp.departure(), trp) for trp in self]

        L.sort()
        self.trp = [i[1] for i in L]

    def __str__(self):
        strr = ''

        for tp in self.trp:
            strr += str(tp) + "\n"
        return strr

    def __repr__(self):
        return str(self)


class TripScheduleIterator:
    def __init__(self, schedule):
        self.__s = schedule
        self.__currentt = 0

    def __next__(self):
        if self.__currentt >= len(self.__s):
            raise StopIteration
        answer = self.__s[self.__currentt]
        self.__currentt += 1
        return answer


# t1 = Trip("Paris", Date(4, 1, 2022), 3)
# t2 = Trip("New York", Date(4, 8, 2022), 5)
# t3 = Trip("Dubai", Date(4, 29, 2022), 7)
# t4 = Trip("Paris", Date(12, 3, 2021), 8)   ########
# t5 = Trip("Madrid", Date(4, 15, 2021), 6)
# t6 = Trip("Damascus", Date(5, 20, 2022), 3)
# t7 = Trip("Barcelona", Date(4, 6, 2022), 6)
# t8 = Trip("Melbourne", Date(12, 18, 2022), 14)
# t10 = Trip("Paris", Date(12, 24, 2021), 3)   #######
#
# S = TripSchedule()
# S.insert(t10)
# S.insert(t1)
# S.insert(t3)
# S.insert(t2)
# S.insert(t6)
# S.insert(t4)
# S.insert(t8)
# S.insert(t5)
#
# S.sortbydeparture()
# print(S)
# print("Testing the search() method. All trips in the month of April in the schedule are shown below: ")
# print(S.search(4))
# print("\n")
# print(S.search("Paris"))
# print("\n")


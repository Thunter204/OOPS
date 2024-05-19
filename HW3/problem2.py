"""
Author: Toni Hunter
RUID: 187009925
Module for Problem 2, Homework 3
Object Oriented Programming (50:198:113), Spring 2022

implement a class called Date for calendar dates occurring on or after January 1, 1800. The constructor sets the values
of the month, day, and year attributes of the date. The constructor must check for the validity of the date, and if the
date is invalid, should raise an exception. each method in class Date is explained in their respective documentation.
"""


class Date:
    min_year = 1800  # Initializing Jan 1, 1800
    dow_jan1 = 'Wednesday'

    def __init__(self, month, day, year):
        """
        :param month: user input month
        :param day: user input day
        :param year: user input year
        self attributes are created for parameters and user input date is check if invalid. if invalid, exceptrions are
        raised and if not, continues to other functions in class Date.
        """
        self.__lmonth = month  # self attributes
        self.__lday = day
        self.__lyear = year

        if self.__lmonth not in range(1, 13):  # check if month is between 1 and 12
            raise Exception("INVALID MONTH")  # raise an exception if not between 1 and 12
        if self.__lmonth in (1, 3, 5, 7, 8, 10, 12) and self.__lday > 31:
            raise Exception("INVALID DAY")
        if self.__lmonth in (4, 6, 9, 11) and self.__lday > 30:
            raise Exception("INVALID DAY")
        if self.__lmonth == 2 and self.__lday > 28:
            if self.__year_is_leap and self.__lday < 29:
                raise Exception("INVALID DAY")

        if self.__lyear < 1800:
            raise Exception("INVALID YEAR")

    def month(self):
        """
        returns int month
        """
        return self.__lmonth

    def day(self):
        """
        returns int day
        """
        return self.__lday

    def year(self):
        """
        returns int year
        """
        return self.__lyear

    def __year_is_leap(self, y=None):
        """
        :param y: user input year
        functions checks if leap year. if year is divisible by 400, it is leap year or if it is divisible by 4 and not
        100, it is leap year. other wise, it is not a leap year
        """
        if y is None:
            y = self.__lyear
        if y % 400 == 0:
            return True  # if divisible by 400, it is a leap year
        elif y % 4 == 0 and y % 100 != 0:  # is year is only multiple of 4, it is a leap year
            return True
        return False

    def __daycount(self):
        totaldays = 0  # counter
        for i in range(1800, self.__lyear):
            if self.__year_is_leap(i):
                totaldays += 366
            else:
                totaldays += 365
        for i in range(1, self.__lmonth):
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:  # made redundant so that 2 is
                # accessed
                totaldays += 31  # 31 days for month 1, 3, 5, 7, 8, 10, 12
            elif i == 4 or i == 6 or i == 9 or i == 11:
                totaldays += 30  # 30 days for months 4, 6, 9, 11
            elif i == 2:
                if self.__year_is_leap(self.__lyear):  # called here to check if february is in leap to count days
                    totaldays += 29
                else:
                    totaldays += 28
        totaldays += self.__lday  # accounts for days that occurred in month entered
        return totaldays

    def day_of_week(self):  # saturday
        day = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
        weekday = self.__daycount() % 7 - 1
        return day[weekday]

    def __str__(self):  # ex--> January 1, 2000
        month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                 'October', 'November', 'December']
        monthr = self.__lmonth - 1
        return "{} {}, {}".format(month[monthr], self.__lday, self.__lyear)

    def __repr__(self):  # ex--> January 1, 2000 was on a Saturday
        return "{} was on a {}".format(str(self), self.day_of_week())

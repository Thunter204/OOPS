"""
Author: Toni Hunter
RUID: 187009925
Module for Problem 1, Homework 4
Object Oriented Programming (50:198:113), Spring 2022

is a continuation of the Date class implementation from Homework 3, asked to include this new implementation
of additional methods for the class, including overloaded arithmetic and comparison operators.
"""
from date import Date

def nextday(self):
    """
    adds +1 day to date entered
    """
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # day in month
    n_month = self.__lmonth
    n_day = self.__lday
    n_year = self.__lyear

    if self.__lmonth == 12 and self.__lday == 31:  # checks to change year if month is December
        n_month = 1
        n_day = 1
        n_year += 1
    elif self.__year_is_leap() == True:  # for February
        m1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if m1[self.__lmonth - 1] == self.__lday:
            n_day = 1
            n_month += 1
        else:
                n_day += 1
    elif m[self.__lmonth - 1] == self.__lday and self.__year_is_leap() == False:
        n_day = 1
        n_month += 1
    else:
        n_day += 1
    return Date(n_month, n_day, n_year)

def prevday(self):
    """
    subtracts -1 days to date entered
    """
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    n_month = self.__lmonth
    n_day = self.__lday
    n_year = self.__lyear

    if self.__lmonth == 1 and self.__lday == 1:
        n_month = 12
        n_day = 31
        n_year -= 1
    elif self.__year_is_leap() == True:  # checks for leap
        m1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if m1[self.__lmonth - 1] == self.__lday:
            n_day -= 1
        elif self.__lday == 1:
            n_month -= 1
            n_day = m1[self.__lmonth - 2]
        else:
            n_day -= 1
    elif m[self.__lmonth - 1] == self.__lday and self.__year_is_leap() == False:
        n_day -= 1
    elif self.__lday == 1:
        n_month -= 1
        n_day = m[self.__lmonth - 2]  # FEBRUARY!!!
    else:
        n_day -= 1
        # n_month -= 1
    return Date(n_month, n_day, n_year)

def __add__(self, n):
    add_d = self
    for i in range(n):
        add_d = add_d.nextday()
    return add_d

def __sub__(self, n):
    sub_d = self
    for i in range(n):
        sub_d = sub_d.prevday()
    return sub_d

def __lt__(self, other):
    if self.__lyear <= other.__lyear:
        if self.__lmonth <= other.__lmonth:
            if self.__lday < other.__lday:
                return True
            else:
                return False

def __eq__(self, other):
    return self.__lday == other.__lday and self.__lmonth == other.__lmonth and self.__lyear == other.__lyear

def __le__(self, other):
    return self < other or self == other

def __gt__(self, other):
    return self.__lday < other.__lday and self.__lmonth < other.__lmonth and self.__lyear < other.__lyear

def __ge__(self, other):
    return self > other or self == other

def __ne__(self, other):
    return not (self == other)


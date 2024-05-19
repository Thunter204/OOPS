"""
Author: Toni Hunter
RUID: 187009925
Module for Problem 2, Homework 4
Object Oriented Programming (50:198:113), Spring 2022

Asked to implement three functions that manipulate Date objects in this module. se Date class methods (as implemented
 in Problem 1 (date.py)) to implement all of the following functions.
"""
from date import Date


def weekend_dates(m, y):
    """
    :param m: month
    :param y: year
    :return: returns all the weekends in that month
    """
    mth_d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(1, mth_d[m]):
        mth_d = Date(m, i, y)
        if mth_d.day_of_week() == 'Saturday' or mth_d.day_of_week() == 'Sunday':
            print(mth_d, "({})".format(mth_d.day_of_week()))


def first_monday(y):
    """
    :param y: year
    :return: returns all the first mondays of each month specified year
    """
    print("First Mondays of {}:".format(y), "\n")

    for i in range(1, 13):
        mth_d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for j in range(1, mth_d[i - 1]):
            mth_d = Date(i, j, y)
            if mth_d.day_of_week() == 'Monday' and j <= 7:
                print(mth_d)


def interval_schedule(start_date, end_date, intvl):
    """
    :param start_date: day you are starting on
    :param end_date: day you end on
    :param intval:  number of days between two date
    :return: intervals of days between start and end
    """

    start = start_date.daycount()
    end = end_date.daycount()
    final = end - start
    intvl_dates = start_date
    intvl_List = []

    for i in range(final // intvl):
        intvl_dates += intvl
        intvl_List.append(intvl_dates)
    return intvl_List
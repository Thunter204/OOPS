"""
Module for Homework 3, Problem 2
Author: Suneeta Ramaswami
Object-Oriented Programming (50:198:113), Spring 2022

Class and methods have not been documented due to time constraints! 
You, however, must do as I say, not as I do.
"""

class Date:
    min_year = 1800
    dow_jan1 = "Wednesday"

    def __init__(self, init_m = 1, init_d = 1, init_y = min_year):
        if init_m < 1 or init_m > 12:
            raise Exception("Invalid Date assignment")
        if init_y < self.min_year:
            raise Exception("Invalid Date assignment")
        self.m = init_m
        self.y = init_y
        monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.year_is_leap():
            monthdays[1] = 29
        if init_d < 1 or init_d > monthdays[self.m-1]:
            raise Exception("Invalid Date assignment")
        self.d = init_d

    def month(self):
        return self.m

    def day(self):
        return self.d

    def year(self):
        return self.y

    def year_is_leap(self):
        if self.y%100 != 0 and self.y%4 == 0:
            return True
        elif self.y%400 == 0:
            return True
        else:
            return False

    def daycount(self):
        monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.year_is_leap():
            monthdays[1] = 29
        total = 0
        d = Date(1, 1, self.min_year)
        while d.year() < self.year():  # This loop counts number of days in whole years
            total += 365
            if d.year_is_leap():
                total += 1
            d = Date(1, 1, d.year() + 1)
        while d.month() < self.month():  # This loop counts number of days in whole months
            total += monthdays[d.month() - 1]
            d = Date(d.month() + 1, 1, d.year())
        total += self.day()
        return total

    def day_of_week(self):
        weekdaynames = ["Sunday", "Monday", "Tuesday", "Wednesday",
                        "Thursday", "Friday", "Saturday"]

        numdays = self.daycount()
        wkday_idx = weekdaynames.index(self.dow_jan1) #index of day of week for Jan 1 of min_year
        
        if numdays%7 == 1:
            return weekdaynames[wkday_idx]
        elif numdays%7 == 2:
            return weekdaynames[(wkday_idx + 1)%7]
        elif numdays%7 == 3:
            return weekdaynames[(wkday_idx + 2)%7]
        elif numdays%7 == 4:
            return weekdaynames[(wkday_idx + 3)%7]
        elif numdays%7 == 5:
            return weekdaynames[(wkday_idx + 4)%7]
        elif numdays%7 == 6:
            return weekdaynames[(wkday_idx + 5)%7]
        else:
            return weekdaynames[(wkday_idx + 6)%7]            

    def __str__(self):
        monthnames = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]
        return "%s %d, %d"%(monthnames[self.month() - 1], self.day(), self.year())

    def __repr__(self):
        return str(self)


    

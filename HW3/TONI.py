class Date:
    min_year = 1800  # Initializing Jan 1, 1800
    dow_jan1 = 'Wednesday'

    def __init__(self, month, day, year):
        self.lmonth = month  # self attributes
        self.lday = day
        self.lyear = year

        if self.lmonth not in range(1, 12):   # check if month is between 1 and 12
            raise Exception("INVALID MONTH")   # raise an exception if not between 1 and 12
        if self.lmonth == 1 or self.lmonth == 3 or self.lmonth == 5 or self.lmonth == 7 or self.lmonth == 8 or \
                self.lmonth == 10 or self.lmonth == 12:
            raise Exception("INVALID DAY")
        elif self.lmonth == 4 or self.lmonth == 6 or self.lmonth == 9 or self.lmonth == 11:
            raise Exception("INVALID DAY")

    def month(self):
        return self.lmonth

    def day(self):
        return self.lday

    def year(self):
        return self.lyear

    def year_is_leap(self, y):
        if y % 400 == 0:
            return True  # if divisible by 400, it is a leap year
        elif y % 4 == 0 and y % 100 != 0:  # is year is only multiple of 4, it is a leap year
            return True
        return False

    def daycount(self):
        totaldays = 0  # counter
        for i in range(1800, self.lyear):
            if self.year_is_leap(i):
                totaldays += 366
            else:
                totaldays += 365
        for i in range(1, self.lmonth):
            print(i)
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:  # made redundant so that 2 is
                                                                                      # accessed
                totaldays += 31  # 31 days for month 1, 3, 5, 7, 8, 10, 12
            elif i == 4 or i == 6 or i == 9 or i == 11:
                totaldays += 30  # 30 days for months 4, 6, 9, 11
            elif i == 2:
                print(self.lyear, "year")
                if self.year_is_leap(self.lyear):  # self.lyear parameter
                    totaldays += 29
                else:
                    totaldays += 28
        totaldays += self.lday
        return totaldays

    def day_of_week(self):
        day = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
        weekday = self.daycount() % 7 - 1
        return day[weekday]

    def __str__(self):
        pass
    def __repr__(self):
        pass


d = Date(7, 4, 1876)
print(d.day_of_week())

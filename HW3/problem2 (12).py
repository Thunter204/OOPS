# Programmer:Sammu Suryanarayanan
#
# RUID: 210006062
# Date: 3/1/22
# Assingment:2
#
# File:p2.py
#
# Program Description:
# In this problem, you are asked to implement a class
# called Date for calendar dates occurring on or after January 1, 1800. FYI, January 1, 1800
# was a Wednesday. Instances of the Date class have a month, day, and year value representing
# valid calendar dates on or after January 1, 1800.


# creat a class

class Date:

    min_year = 1800

    dow_jan1 = 'Wednesday'

    def __init__(self, month = 1, day = 1, year = min_year):

        """
        This function goes through and makes sure the values entered are
        not out of range. 
        """
        self.lday = day
        self.lmonth = month
        #self.month2 = month
        self.lyear = year
        if self.lmonth > 12:
            raise Exception("Month can't be greater than")
        if self.lyear < self.min_year:
            raise Exception("Year must be after 1800")

        # check if the date is valid:

        if self.lmonth == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if day > 31:
                raise Exception("Day can't be more than 31")
        elif self.lmonth == 4 or 6 or 9 or 11:
            if day > 30:
                raise Exception("Day can't be more the 30 days")
    def month(self):
        """
        This function returns the month that the user enters.
        """
        #self.months = {1:'January', 2:'Febuary', 3:'March',4:'April',
                       #5:'May', 6:'June', 7:'July', 8:'August', 9:'Septmeber',
                       #10:'October' ,11:'November', 12: 'December'}
        #for key in self.months:
            #if key == self.month2:
        return self.lmonth

    def day(self):
        """
        This function returns the day
        """

        
        return self.lday
    def year(self):
        """
        This function returns the year
        """

        return self.lyear

    def year_is_leap(self):
        """
        This function return if the year is a leap year or not
        """
        
        if (self.lyear % 4 == 0 and self.lyear % 100 != 0) or(self.lyear % 400 == 0):
            return True
        return False
    
    def daycount(self):
        """
        This function calculate how days have passed since January 1st, 1800
        """

        days_passed = 0

        for i in range(1800,self.lyear):

            if self.year_is_leap()== True:

                days_passed += 366
            else:
                days_passed +=365

        for i in range(1, self.lmonth):
            if i == 1 or i==3 or i==5 or i==7 or i ==8 or i==10 or i==12:
                days_passed += 31

            elif i ==4 or i == 6 or i == 9 or i ==11 :
                days_passed += 30

            elif i == 2:
                if self.year_is_leap() == True:
                    days_passed += 29
                else:
                    days_passed += 28
                   
            
        days_passed += self.lday

        return (days_passed)
    
    def day_of_week(self):
        """
        This function returns what day of the week it was. 
        """
        self.week =['Wednesday','Thursday','Friday',
                    'Saturday','Sunday','Monday','Tuesday',]
        day = self.daycount() % 7 - 1

        return(self.week[day])
    
    def __str__(self):
        """
        This function formats the answer
        """
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                 'October', 'November', 'December']
        month = self.lmonth - 1
        return "{} {}, {}".format(months[month], self.lday, self.lyear)

    
    def __repr__(self):
        return str(self)


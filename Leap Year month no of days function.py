#This program contains 2 functions that check if a year is a leap year and then takes any month number in this year and outputs the number of days in this month
Leapflag=False
def isYearLeap(year):
    LeapFLag=False
    if year%4==0:
        if year%100==0:
            if year%400==0:
                LeapFlag=True
            else: LeapFlag=False
        else: LeapFlag=True
    else: LeapFlag=False
    return LeapFlag


def daysInMonth(year, month):
    Leapflag=isYearLeap(year)
    if month==2:
        if Leapflag==True:
            return(29)
        else:
            return(28)
    else:
        if month==1 or month==3 or month==5 or month==7 or month==10 or month==10 or month==12:
            return(31)
        else:return(30)

from datetime import date

year=int(input("Enter your birth year\n"))
month=int(input("Enter your birth month\n"))
day=int(input("Enter your birth day\n"))

Datetod = str(date.today())

yeartod = int(Datetod[0:4])
monthtod = int(Datetod[5:7])
daytod = int(Datetod[8:10])

if month==monthtod and day == daytod:
    years = yeartod-year
    months = 0
    days = 0

elif month > monthtod:
    years = yeartod - (year+1)
    months = 12 - (month- monthtod)
    if day > daytod:
        days = day-daytod
    elif day == daytod:
        days=0
    else:
        months-=1
        days = 30 - day + daytod
else:
    months = month - monthtod
    if day > daytod:
        days == day-daytod
    elif day == daytod:
        days=0
    else:
        months-=1
        days = 30 - day + daytod
if days > 30:
    months+=1
    days-=30
    
print(f"You are {years} years old, {months} months old, and {days} days old")

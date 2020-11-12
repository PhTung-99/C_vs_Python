import timeit
import datetime
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def checkYear():
    i=0
    n=0
    while i<1000:
        if is_leap_year(n)== True:
            print(n)
            i=i+1
            #print(f"{i}")
        n=n+1
def checkTimeRun():
    time = str(datetime.timedelta( seconds =timeit.timeit(checkYear, number=1)))
    print (time)

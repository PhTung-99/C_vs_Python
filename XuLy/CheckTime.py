import datetime
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def time():
    i=0
    n=0
    old = datetime.datetime.now()
    while i<1000:
        if is_leap_year(n)== True:
            print(f"Nam nhuan{n}")
            i=i+1
            #print(f"{i}")
        n=n+1
        
    new = datetime.datetime.now()
    print(new - old)

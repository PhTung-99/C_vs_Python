import timeit
import datetime
def check(n):
    Tong =0
    for i in range (1,n):
        if n % i == 0:
            Tong=Tong+i
    if Tong==n:
        return True
    else:
        return False
def printSoHH():
    i=0
    n=0
    while i<=100:
        if check(n)== True:
            print(n)
            i=i+1
        n=n+1
        
        if n==100000:
            break
def checkTimeRun():
    time = str(datetime.timedelta( seconds =timeit.timeit(printSoHH, number=1)))
    print (time)

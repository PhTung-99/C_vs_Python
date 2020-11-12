from math import *
import timeit
import datetime
def check(n):
        if n<2:
            return False
        count = 0
        for i in range (2,n,1):
            if n%i==0:
                count=count+1
        
        if count ==0:
            return True
        else:
            return False
def printSoNt():
    i=0
    n=0
    while i<=1000:
        if check(n)== True:
            print(n)
            i=i+1
        n=n+1
        
        if n==100000:
            break
def checkTimeRun():
    time = str(datetime.timedelta( seconds =timeit.timeit(printSoNt, number=1)))
    print (time)

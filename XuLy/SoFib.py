import timeit
import datetime
def fib():
    def recur_fibo(n):
        if n < 0:
           return -1
        elif (n==0 or n==1):
            return n
        else:
           return(recur_fibo(n-1) + recur_fibo(n-2))     
    i=0
    while i<45:
        print(f"{recur_fibo(i)}")
        i=i+1
        
def checkTimeRun():
    time = str(datetime.timedelta( seconds =timeit.timeit(fib, number=1)))
    print (time)
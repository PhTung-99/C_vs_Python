import timeit
import datetime
def fib():
    def recur_fibo(n):
       if n <= 1:
           return n
       else:
           return(recur_fibo(n-1) + recur_fibo(n-2))     
    i=1
    while i<45:
        print(f"{recur_fibo(i)}")
        i=i+1
        
def checkTimeRun():
    time = str(datetime.timedelta( seconds =timeit.timeit(fib, number=1)))
    print (time)
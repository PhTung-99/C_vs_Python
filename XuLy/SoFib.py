import datetime
def fib():
    def recur_fibo(n):
       if n <= 1:
           return n
       else:
           return(recur_fibo(n-1) + recur_fibo(n-2))
        
            
    old = datetime.datetime.now()
    print(old)
    i=0
    while i<45:
        print(f"{recur_fibo(i)}")
        i=i+1
        
    new = datetime.datetime.now()
    print(new - old)

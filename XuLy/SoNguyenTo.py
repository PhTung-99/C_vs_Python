import datetime
from math import *
def SoNguyenTo():
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
            
    
    old = datetime.datetime.now()
    print(old)
    i=0
    n=0
    while i<=1000:
        if check(n)== True:
            print(f"So nguyen to{n}")
            i=i+1
        else:
            print(f"{n}")
        n=n+1
        
        if n==100000:
            break
        
    new = datetime.datetime.now()
    print(new - old)

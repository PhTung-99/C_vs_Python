import datetime
def soHoanHao():
    def check(n):
        Tong =0
        for i in range (1,n):
            if n % i == 0:
                Tong=Tong+i
        if Tong==n:
            return True
        else:
            return False
            
    old = datetime.datetime.now()
    print(old)
    i=0
    n=0
    while i<=100:
        if check(n)== True:
            print(f"So hoan hao{n}")
            i=i+1
        else:
            print(f"{n}")
        n=n+1
        
        if n==100000:
            break
        
    new = datetime.datetime.now()
    print(new - old)

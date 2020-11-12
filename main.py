
import XuLy.SoNguyenTo as bai1
import XuLy.SoFib as bai2
import XuLy.CheckTime as bai3
import XuLy.SoHoanHao as bai4
import sys 
import os

clear = lambda: os.system('cls')
clear()

def runC(link):
    input("Press Enter to run C...")
    run = lambda: os.system(link)
    run()

def Again():
    print("Co muon tiep tuc chuong trinh")
    temp = int(input("1---Yes    0----No"))
    if(temp == 1 ):
        clear()
        chonMenu()
    if( temp== 0):
        print("BYE BYE")
        sys.exit()
def chonMenu():
        print("1. Số Nguyên Tố ")
        print("2. Số Fibonacci")
        print("3. Năm Nhuận")
        print("4. Số Hoàn Hảo")
        print("0. Exit")   
        i = int(input("Chọn Chương Trình\n"))
        if( i> 4 or i<0):          
            print("Nhap lai menu")
            print()
            chonMenu()
        if (i == 1):
            print("So Nguyen To")
            bai1.checkTimeRun()
            runC('C\songuyento')
        if (i == 2):
            print("So Fib") 
            bai2.checkTimeRun()
            runC('C\Sofibonacci')
        if (i == 3):
            print("So Nam Nhuan")     
            bai3.checkTimeRun()
            runC('C\year')
        if (i == 4):
            print("So Hoan Hao")
            bai4.checkTimeRun()
            runC('C\soHoanHao')
        Again()

chonMenu()

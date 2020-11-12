
import XuLy.SoNguyenTo as bai1
import XuLy.SoFib as bai2
import XuLy.CheckTime as bai3
import XuLy.SoHoanHao as bai4
import sys
def Again():
    print("Co muon tiep tuc chuong trinh")
    temp = int(input("1---Yes    0----No"))
    if(temp == 1 ):
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
        i = int(input("Chọn Chương Trình"))
        if( i> 4 or i<0):          
            print("Nhap lai menu")
            print()
            chonMenu()
        if (i == 1):
            print("So Nguyen To")
            bai1.SoNguyenTo()
        if (i == 2):
            print("So Fib") 
            bai2.fib()
        if (i == 3):
            print("So Nam Nhuan")     
            bai3.time()
        if (i == 4):
            print("So Hoan Hao")
            bai4.soHoanHao()
        Again()


chonMenu()




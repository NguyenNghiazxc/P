from random import randint
from operator import truediv
luoi = [0,1,2,3,4,5,6,7,8]
win= " "
def maTran():
    for i in range(0,9,3):
        print(luoi[i],"|",luoi[i+1],"|",luoi[i+2])
        print("---------")
maTran()

def trong():
    for i in range(9):
        if luoi[i] != "X" and luoi[i] != "O":
            return True
def ktr_dong(chon,x1,x2,x3):
    if luoi[x1]==chon and luoi[x2]==chon and luoi[x3]==chon:
        return True
def ktr_all(chon):
    if ktr_dong(chon,0,1,2)==True:
        return True 
    if ktr_dong(chon,3,4,5)==True:
        return True 
    if ktr_dong(chon,6,7,8)==True:
        return True 
    if ktr_dong(chon,2,5,8)==True:
        return True 
    if ktr_dong(chon,1,4,7)==True:
        return True 
    if ktr_dong(chon,0,3,6)==True:
        return True 
    if ktr_dong(chon,0,4,8)==True:
        return True 
    if ktr_dong(chon,2,4,6)==True:
        return True 
    return False
while trong():
    nguoi = int(input("Ban hay chon mot o trong [0-8] : "))
    if luoi[nguoi]== "X" or luoi[nguoi]=="O":
        print("O da duoc chon")
    else:
        luoi[nguoi]="X"
    may = randint(0,8)
    if luoi[may]=="X" or luoi[may]=="O":
        pass
    else:
        luoi[may]="O"
    maTran()
    if ktr_all("X"):
        win="Ban"
        break
    if ktr_all("O"):
        win="Computer"
        break
if win == " ":
    print("Hoa")
else:
    print(win,"Thang")
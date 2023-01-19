import math

def prim(szam):
    for i in range(2,int(math.sqrt(szam))+1):
        if szam % i==0:
            return False
    return True

db = 0 #Még nincs primszam
szam = 2

while db<100:
    if prim(szam): #ha prim
        print(szam, end=' ') # akkor kiirjuk (egymas melléé)
        db+=1
    szam+=1

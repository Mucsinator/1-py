#1. FÉLE

import math

def prim(szam):        
    for i in range(2,int(math.sqrt(szam))+1):
        if szam%i==0:
            return False
    return True

szam=int(input("\nKérek egy számot: "))

if prim(szam):         
    print("A megadott szám prím.")
else:                  
    print("A megadott szám NEM prím.")
    
#------------------------------------------------------------------
#2. FÉLE LISTÁBÓL VAN-E PRÍM

import random 
import math

def ez_prím(szam):
    for i in range(2, int(math.sqrt(szam))+1):
        if szam%i==0:
            return False
    return True

def vaneprim():
    for item in szamok:
        if ez_prím(item):
            return 'Van prímszám a listában!'
    return 'Nincs prímszám a listában!'

szamok=[]
for i in range(10):
    szamok.append(random.randint(10,99))

print(szamok)
print(vaneprim())
#------------------------------------------

#3. FÉLE TARTOMÁNY PRÍM

# Prímszámok tartományon

import math

def prim(szam):         #a kapott szám prím-e vagy nem (True/False)
    for i in range(2,int(math.sqrt(szam))+1):
        if szam%i==0:   #vizsgálati egyenlőség jel "=="
            return False
    return True

also_hatar=0
while also_hatar<=0:
    also_hatar=int(input("Kérem adja meg az intervallum alsó határát: "))

felso_hatar=0
while felso_hatar<=also_hatar:
    felso_hatar=int(input("Kérem adja meg az intervallum felső határát: "))


szam=also_hatar

while szam<=felso_hatar:
    if prim(szam) and szam!=1:              # ha prím
        print(szam,end=" ")     # akkor kiírjuk (egymás mellé)
    szam+=1             # át kell lépni a következő számra
    
#------------------------------------------------------------------------
#4. FÉLE 50 ELSŐ PRÍM

# 50 első prím

import math

def prim(szam):         #a kapott szám prím-e vagy nem (True/False)
    for i in range(2,int(math.sqrt(szam))+1):
        if szam%i==0:   #vizsgálati egyenlőség jel "=="
            return False
    return True

db=0    #kedzetben még nincs prímszámunk
szam=2

while db<50:
    if prim(szam):              # ha prím
        print(szam,end=" ")     # akkor kiírjuk (egymás mellé)
        db+=1                   # találtunk prímet, ezért növeljük
    szam+=1             # át kell lépni a következő számra
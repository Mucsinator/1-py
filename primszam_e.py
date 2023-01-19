import math

def prim(szam):         #a kapott szám prím-e vagy nem (True/False)
    for i in range(2,int(math.sqrt(szam))+1):
        if szam%i==0:   #vizsgálati egyenlőség jel
            return False
    return True

print("Prímszám vizsgálat")
szam=int(input("\nKérek egy számot: "))

if prim(szam):     #True - igaz eset
    print("A megadott szám prím.")
else:               #False - hamis eset
    print("A megadott szám NEM prím.")

#Számok kiírása intervallumon, lépésközzel

i=2  #intervallum alsó határa (mettől)
while i<=100:   #intervallum felső határa (meddig)  
    print(i,end=' ')
    i+=2        #i növelése lépésközzel

#---------------------------------------------------------
#Véletlen szám generálása (kockadobások)

from random import randint # véletlen szám generálásához kell!

print("\n\nKockadobások:")
#addig dobálunk a 2 kockával, amíg mind a 2 nem lesz 6-os

elso_kocka=randint(1,6)    #generál 1 egész számot 1 és 6 között
masodik_kocka=randint(1,6)
#while elso_kocka+masodik_kocka!=12:
while elso_kocka!=6 or masodik_kocka!=6:
    print(f"{elso_kocka},{masodik_kocka}")
    elso_kocka=randint(1,6)
    masodik_kocka=randint(1,6)
print(f"{elso_kocka},{masodik_kocka}")
print("Mindkét kockával 6-ost dobtál, VÉGE.")
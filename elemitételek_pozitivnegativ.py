import random

szamok = []
pozitiv = 0
negativ = 0
for i in range(20):
    szam = random.randint(-50, 50)
    szamok.append(szam)
    if szam > 0:
        pozitiv += 1
    elif szam < 0:
        negativ += 1
if pozitiv > negativ:
    print("Pozitív számból több van, mint negatívból.")
elif pozitiv == negativ:
    print("Negatív számokból van több.")
else:
    print("Ugyanannyi pozitív van mint negatív.")

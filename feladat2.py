
def ez_prim(szam):
    oszto_db = 0
    for osztó in range(1, szam + 1):
        if szam % osztó == 0:
            oszto_db += 1

    if oszto_db == 2:
        return True
    else:
        return False


lista = [4, 3, 5, 6, 2, 8, 1]
for i in range(len(lista)):
    if ez_prim(i):
        print(lista[i])

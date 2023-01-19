import random
homersekletek = []
for item in range(20):
    szam = random.random()
    homersekletek.append(round(szam*50-10,2))
print(homersekletek)
index = 6
max = -11
for index in range(6, len(homersekletek)):
    if index % 7 == 6:
        if max < homersekletek[index]:
            max = homersekletek[index]
print(f"A legmelegebb vasárnapi hő: {max}")

# a <= b <= c
# a2 + b2 = c2 -> derékszögű háromszög
# a2 + b2 > c2 -> hegyesszögű háromszög
# a2 + b2 < c2 -> tompaszögű háromszög

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a**2 + b**2 > c**2:
    print("Hegyesszögű háromszög")
elif a**2 + b**2 == c**2:
    print("Derékszögű háromszög")
else:
    print("Tompaszögű háromszög")

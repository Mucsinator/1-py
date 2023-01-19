import math

a = float(input("Kérem adja meg az a értékét: "))
b = float(input("Kérem adja meg a b értékét: "))
c = float(input("Kérem adja meg a c értékét: "))

d=b*b-4*a*c

if d > 0:
    x1 = (-1*b + math.sqrt(d))/2*a
    x2 = (-1*b - math.sqrt(d))/2*a
    print(f"A megoldások: {x1, x2}")

else:
    if d < 0:
        print("Nincs megoldás!")
    else:
        x1 = (b-math.sqrt(d))/2*a
        print(f"Egy megoldás: { x1}")
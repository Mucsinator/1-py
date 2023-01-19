a= float(input("Kérem az a együtthatót"))
b= float(input("Kérem a b együtthatót"))
c= float(input("Kérem a c együtthatót"))

diszkriminans= b**2 - 4*a*c
if diszkriminans==0:
    print("Az egyenletnek egy megoldása van")
elif diszkriminans <0:
    print("Az egyenletnek nincs megoldása ")
else:
    print("Az egyenletnek két megoldása van")

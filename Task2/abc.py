from math import sqrt

a = float(input("Please enter the value of a."))
b = float(input("Please enter the value of b."))
c = float(input("Please enter the value of c."))

D = b**2 -4*a*c

if D < 0 or a == 0:
    print("No solutions.")
if D == 0:
    print(f"The solution isx = {-(b)/(2*a)}")
if D > 0:
    x1 = (-b + (sqrt(D)))/(2*a)
    x2 = (-b - (sqrt(D)))/(2*a)
    print(f"The first solution is x = {x1}")
    print(f"The second solution is x = {x2}")

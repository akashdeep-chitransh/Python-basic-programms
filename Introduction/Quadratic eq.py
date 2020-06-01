# This programm will find the Roots os quadratic equation...
# ax^2 + bx + c = 0
import cmath

# coefficient of equation
a =1
b =5
c =6
# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions.
root1 = (-b - cmath.sqrt(d))/(2*a)
root2 = (-b + cmath.sqrt(d))/(2*a)
print("Thhe roots are:")
print(root1)
print(root2)
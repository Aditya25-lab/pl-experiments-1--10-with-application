# Biodata
name = input("Enter name: ")
age = int(input("Enter age: "))
print("\nName:", name, "Age:", age)

# Arithmetic
a = int(input("\nEnter two numbers: "))
b = int(input())
print("Add:", a+b, "Sub:", a-b, "Mul:", a*b, "Div:", a/b)

# Swap
a, b = b, a
print("After swap: a =", a, "b =", b)

# Simple Interest
p = float(input("\nPrincipal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
print("SI =", (p*r*t)/100)

# Temperature
c = float(input("\nCelsius: "))
print("Fahrenheit:", (c*9/5)+32)

# Rectangle
l = float(input("\nLength: "))
w = float(input("Width: "))
print("Area:", l*w, "Perimeter:", 2*(l+w))

# Number check
n = int(input("\nEnter number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# Days conversion
d = int(input("\nDays: "))
print("Years:", d//365, "Weeks:", (d%365)//7, "Days:", (d%365)%7)

# Square & Cube
x = int(input("\nNumber: "))
print("Square:", x**2, "Cube:", x**3)

# Relational & Logical
y = int(input("\nEnter another number: "))
print("x > y:", x > y)
print("x > 0 and y > 0:", x > 0 and y > 0)

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
#----Logic 1 (Using Arithmetic)------------
print("Using Arithmetic")
print(x, y)
x = x+y
y = x - y
x = x - y
print(x, y)

#----Logic 2 (Using Boolean)---------------
print("Using Boolean")
x = x^y
y = x^y
x = x^y
print(x, y)

s = input("Enter a number: ")
n = int(s)
def factorial(n):
	if (n==1):
		return 1
	elif (n==0):
		return 1
	else:
		x = n * factorial(n-1)
		return x
print(factorial(n))

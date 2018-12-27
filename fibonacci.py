s = input("Enter a number: ")
n = int(s)

a = 1
b = 1
'''for i in range(n):
	 c = b + a
	 a = b
	 b = c
	 print(c)'''

def fib(n):
	if (n==0):
		return 0
	if (n ==1):
		return 1
	else:
		return(fib(n-1) + fib(n-2))

for i in range(n):
	print(fib(i))

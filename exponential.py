x = float(input("Enter a number: "))
n = int(input("Enter the degree of accuracy: "))

def fact(i):
	if(i==1):
		return 1
	else:
		x = i*fact(i-1)
		return x
ex = 1
print(fact(n))

for i in range(1,n):
	ex = ex + ((x**i)/fact(i))
print(ex)

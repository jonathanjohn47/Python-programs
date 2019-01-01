def prime(n):
	x = []
	for i in range(2,n):
		if n%i==0:
			x.append(i)
	if x == []:
		return True
	else:
		return False

def primefactor(n):
	pf = []
	for i in range(2,n+1):
		if prime(i)==True:
			if(n%i==0):
				pf.append(i)
	return pf

print(primefactor(842))

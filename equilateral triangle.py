n = int(input("Enter a number: "))

for i in range(1, n):
	print(' '*n, end = '')
	print('* '*i)
	n = n-1

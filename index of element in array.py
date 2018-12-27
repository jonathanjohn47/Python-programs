import numpy as np
import random
x = []
for i in range(100):
	x.append(random.randint(1,1000))

print('Original List is: ')
print(x)
n = int(input("Enter a number you want to search the index of: "))
if(n in x):
	for i in range(0, len(x)):
		if(x[i]==n):
			print("the index is: ", i)
			break
		else:
			pass
else:
	print("The number is not in the list")

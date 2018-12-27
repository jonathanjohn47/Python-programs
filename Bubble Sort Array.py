import numpy as np
import random
x = []
for i in range(100):
	x.append(random.randint(1,1000))

print('Original List is: ')
print(x)

flag = False
for i in range(len(x)):
	for j in range(len(x)-1 - i):
		if (x[j] > x[j+1]):
			t = x[j]
			x[j] = x[j+1]
			x[j+1] = t
			flag = True
		else:
			pass

print('Sorted List is: ')
print(x)

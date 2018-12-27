import numpy as np
x = np.arange(100,0,-1)

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
	if (flag == False):
		break
	else:
		flag = False
		

print('Sorted List is: ')
print(x)

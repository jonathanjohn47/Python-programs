import random
#-------Check for even numbers in a list--------------
lst = []
for i in range(10):
	lst.append(random.randint(0,100))

print(lst)
f = lambda x: x%2==0
lst1 = []
for i in range(len(lst)):
	if(f(lst[i])==True):
		lst1.append(lst[i])
	else:
		pass
print(lst1)

#-------add consecutive elements in list--------------
f = lambda x, y: x + y
lst2 = []
for i in range(len(lst)-1):
	lst2.append(f(lst[i], lst[i+1]))
print(lst2)
#-------calculate product of two lists--------------
l1 = []
l2 = []
for i in range(10):
	l1.append(random.randint(0,100))
	l2.append(random.randint(0,100))
l3 = []
f = lambda x, y: x*y
for i in range(len(l1)):
	l3.append(f(l1[i], l2[i]))
print(l3)

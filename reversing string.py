s = input("Enter a sentence: ")
a = s.split()

print(s[::-1])
print(a[::-1])

for i in range(len(a)):
    print(a[len(a) -1 -i], end = ' ')

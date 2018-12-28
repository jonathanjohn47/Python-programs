def prime(n):
    if n==1:
        print('Neither prime nor composite')
    elif n<1:
        print('Enter a valid Natural Number')
    else:
        prime = []
        for i in range(2,n):
            if(n%i==0):
                prime.append('N')
            else:
                prime.append('P')
        if('N' in prime):
            print("Not Prime")
        else:
            print("Prime")
n = int(input("Enter a number: "))
prime(n)

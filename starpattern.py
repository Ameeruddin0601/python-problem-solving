#print stars in right angled triangle

n= int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
    
#print stars in hollow right angled triangle
n= int(input("Enter a number: "))

for row in range(n):
    for col in range(n):
        if(col==0 or row==(n-1) or row==col):
            print("*", end="")
        else:
            print(end=" ")
    print()

#vertical flip of star pattern
n= int(input("Enter a number: "))

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*", end=" ")
    print()

#horizontal flip of star pattern
n=int(input("Enter number of rows: "))
for i in range (1,n+1):
    print((n-i) * ' ' + i * '*')

#vertical flip of horizontal flip
n=int(input("Enter number of rows: "))
for i in range (n,0,-1):
    print((n-i) * ' ' + i * '*')

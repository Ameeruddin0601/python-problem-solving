#printing number in right angle triangle

n = int(input("Enter The Number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

n = int(input("Enter The Number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()
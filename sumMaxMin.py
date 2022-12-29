#take inpput for number of elements
#take input numbers
#give sum of max and min of that elements
#55 87 46 21 34 79
num = int(input())
elements = list(map(int,input().split()))

print(max(elements)+min(elements))
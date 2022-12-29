#GCD
#greatest number which divides both the numbers completely

def GCD(num1,num2):
    if(num1 > num2):
        min = num2
    else:
        min = num1
    for i in range(1,min+1):
        if num1%i==0 and num2%i==0:
            hcf = i
    return hcf
print(GCD(20,85))

#subtracting the smaller no. from bigger no. till they become equal
def GCD(a,b):      
    while a!=b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
print(GCD(20,85))

# 20,85 -> 85-20=65
# 20,65 -> 65-20=45
# 20,45 -> 45-20=25
# 20,25 -> 25-20=5
# 20,5  -> 20-5=15
# 15,5  -> 15-5=10
# 10,5  -> 10-5=5
# 5,5 GCD=>5


import math
print(math.gcd(20,85))
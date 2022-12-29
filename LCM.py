#Lowest Common Multiplier

#normally it's not allowed in exam to use math module
#so you have to make GCD function first for this approach
import math
def LCM(a,b):
    return (a*b) / math.gcd(a,b) 
print(LCM(20,85))

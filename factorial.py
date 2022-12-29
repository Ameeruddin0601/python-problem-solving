#factorial
#eg: 8 -> 8*7*6*5*4*3*2*1

#1.find factorial of given number
#2.find no. of trailing zeros in that factorial

def factorial(number):
    fact = 1
    for i in range(number, 0, -1):
        fact = fact*i
    return fact
print(factorial(8)) 

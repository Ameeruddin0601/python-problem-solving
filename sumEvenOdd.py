#display sum of odd and even number in a digit
#eg: 2569 -> 2+6=8 and 5+9=14

def sumOfOddEven(input_num):
    sumOfEven = 0
    sumOfOdd = 0
    for num in str(input_num):
        if int(num)%2 == 0:
            sumOfEven += int(num)
        else:
            sumOfOdd += int(num)
    return sumOfEven,sumOfOdd
print(sumOfOddEven(2569))
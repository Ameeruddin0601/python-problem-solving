#input: 24319587
#sum of odd numbers
#sum of even numbers 
#difference between sum of both odd and even
#This question could be asked by giving a 2D Matrix as an input

input_num = input()
sumOfEven = 0
sumOfOdd = 0

for i in input_num:
    #if(int(i)%2==0):
    if(not int(i)%2):
        sumOfEven += int(i)
    else:
        sumOfOdd += int(i)

print(abs(sumOfEven - sumOfOdd))      

#input: 24319587
#odd numbers ka sum nikaal
#even numbers ka sum nikaal 
#aur dono sum ka difference nikaal

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

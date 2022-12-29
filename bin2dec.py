#hands on binary to decimal conversion
#eg: 101
#logic: sum of all digit*(2^placevalue)
#soln: right to left
# 1 * 2^0 = 1
# 0 * 2^1 = 0
# 1 * 2^2 = 4

#therefore, decimal is 5
#OR
#int(101, 2)
#binary h islie 2 lere, uski jaga koi b base rehta jaise
#octa raha to 2 ki jaga 8 aaaega
#17 raha to 17 aaega,etc.

#q: 17 ka base ka number diya hai,usko decimal me convert karna h
#INPUT: 23GF
#OUTPUT: 10980

# input_num = input()
#print(int(input_num,17)) #SHORTCUT #valid base values:0 and 2-36
# dictOfBase17 = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16}
# input_num = input_num[::-1]
# sum = 0

# for x in range(len(input_num)):
#     sum += dictOfBase17[input_num[x]] * (17**x)
# print(sum)

#binary array to decimal
def binary_array_to_number(arr):
    bin=" "
    for x in arr:
        bin +=str(x)
    return (int(bin,2))
print(binary_array_to_number([0,0,0,1]))

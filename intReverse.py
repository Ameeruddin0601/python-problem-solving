#Reverse a positive integer number
#eg: 587 -> 785, 140 -> 41

def intRev(input_num):
    return int(str(input_num)[::-1]) 
print(intRev(140))

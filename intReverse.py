#Reverse a positive integer number
#eg: 587 -> 785, 140 -> 41

def intRev(input_num):
    return int(str(input_num)[::-1]) #pehle int ko str me convert kia fir usko licing se reverse kia fir str ko int me convert kia fir return kia
print(intRev(140))

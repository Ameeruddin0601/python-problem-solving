#number of n digits which are equal to sum of nth power of its digits

#eg:

#step 1: Take input
input_value=int(input("Enter The Number: \n"))

#step 2: Set variables
result = 0 #isme final result store hoga
copy_input_value=input_value #input value jo b hogi wo me isme safe karke rakhraha
order = len(str(input_value)) #ye length dega input ki jisko hum as a power use karege

#step3: while loop chalaaege
while(input_value>0):
    digit = input_value % 10 #ye meko ek ek digit dega input ka
    result += digit ** order #every digit raise to order ka addition yaha hoga
    input_value=input_value//10 #every last digit will be removed : truncated division

if(result==copy_input_value):
    print(f"{copy_input_value} is an Armstrong Number")
else:
    print(f"{copy_input_value} is NOT an Armstrong Number")

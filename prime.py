#check if number is prime

#Logic: Hum input lege aur uss input ko Usse chote jitne b number hai unse divide karege except 1
        #agar division hone pr zero aaya samjho wo prime number nahi hai, agar zero nai aaya then it is PRIME NUMBER

input_value = int(input("Enter any number: \n"))

def check_prime(input_value):
    for x in range(2,(input_value//2)+1):
        if input_value%x==0:
            return False
    return True
print(check_prime(input_value))

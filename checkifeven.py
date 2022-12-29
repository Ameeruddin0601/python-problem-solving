#check if given number is even or not

input_value = int(input("Enter Your Number: \n"))

if(input_value % 2 == 0):
    print(f"{input_value} is an even number")
else:
    print(f"{input_value} is NOT an even number")
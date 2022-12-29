#take the string and reverse it

input_string = input("Enter Your String: ")
new_str=""
for i in input_string:
    new_str= i + new_str
print(new_str)
print(input_string[::-1]) #used slicing
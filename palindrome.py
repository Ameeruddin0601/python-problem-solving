#check if palindrome

def palindrome(input_str):
    return input_str.lower() == input_str[::-1].lower() #case sensitive
print(palindrome("Nitin"))
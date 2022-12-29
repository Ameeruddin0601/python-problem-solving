# def swap_case(s):
#     # return s.swapcase()
#     res = ""
#     for char in s:
#         if char.isupper():
#             res += char.lower()
#         if char.islower():
#             res += char.upper()
#     return res

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


#convert first letter of every word in a string
def to_jaden_case(string):
    return ' '.join (char.capitalize() for char in string.split())
print(to_jaden_case("Ammy bhai hard hai"))
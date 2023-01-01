# if __name__ == '__main__':
#     s = input()
#     print(any(c.isalnum() for c in s))
#     print(any(c.isalpha() for c in s))
#     print(any(c.isdigit() for c in s))
#     print(any(c.islower() for c in s))
#     print(any(c.isupper() for c in s))
       


#learn string alignment
#rjust ljust center

#textwrap
# import textwrap

# def wrap(string, max_width):
#     string = string
#     max_width = max_width
#     return textwrap.fill(string,max_width)
    
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

# def abbrev_name(name):
#     first, last = name.upper().split(' ')
#     return first[0] + '.' + last[0]
#     #return '.'.join(w[0] for w in name.split()).upper()
# print(abbrev_name('Ameer Bagdadi'))

#letters should not repeat in an string
# def no_rep(string):
#     str_list = []
#     string = string.lower()
#     for i in string:
#         if i in str_list:
#             return False
#         str_list.append(i)
#     return True
# print(no_rep("moOse"))

#check if string is pangram...means every letter from a-z appears in it atleast once
# def is_pangram(s):
#     alphabets = "abcdefghijklmnopqrstuvwxyz"
#     for char in alphabets:
#         if char not in s:
#             return False
#     return True
# print(is_pangram("The quick, brown fox jumps over the lazy dog!"))


#replace every letter with its position in the alphabet.
# def alphabet_position(text):
#     alphabets = ".abcdefghijklmnopqrstuvwxyz"
#     text_num = ""
#     if type(text)==str:
#         text = text.lower()
#     for char in text:
#         if char.isalpha() == True:
#             text_num = text_num + " " + str(alphabets.index(char))
#     return text_num.strip(" ")
# print(alphabet_position("The sunset sets at twelve o' clock."))

# A "word" is a sequence of alphabetical characters. 
# By this definition, any other character like a space or hyphen (eg. "elephant-ride") will split up a series of letters into two words
# (eg. "elephant" and "ride").
# The abbreviated version of the word should have the first letter, then the number of removed characters, 
# then the last letter (eg. "elephant ride" => "e6t r2e")
# def abbreviate(s):
#     word=""
#     word_list=[]
#     for i in s:
#         if i.isalpha():
#             word+=i
#         else:
#             word_list.append(word)
#             word=""
#             continue
#     if word:
#         word_list.append(word)

#     for i in word_list:
#         if len(i)>3 and i.isalpha()==True:
#             s=s.replace(i,i[0]+str(len(i[1:-1]))+i[-1])
#     return s
# print(abbreviate("elephant:ride"))

# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters 
# then it should replace the missing second character of the final pair with an underscore ('_')
# def solution(s):
#     word=""
#     sp=[]
#     for i in range(len(s)):
#         word+=s[:2]
#         if word!="":
#             if len(word)==1:
#                     word+="_"
#             sp.append(word)
#             word=""
#             s=s[2:]    
#     return sp
#     # result = []
#     # if len(s) % 2:
#     #     s += '_'
#     # for i in range(0, len(s), 2):
#     #     result.append(s[i:i+2])
#     # return result
# print(solution("x"))

# Title Case- Codewars
# def title_case(title, minor_words=''):
#     title=title.lower().split()
#     for i in range(len(title)):
#         if title[i] not in minor_words.lower().split() or i==0:
#             title[i]=title[i].capitalize()
#     return " ".join(title)

# print(title_case('THE WIND IN THE WILLOWS', 'The In'))

#Question
#input- a3b2c4 
#output- aaabbcccc
st="a3b2c4"
def charnum(st):
    output=""
    for i in st:
        if i.isalpha():
            var=i
        else:
            num=int(i)
            output += var*num
    return output
print(charnum(st))
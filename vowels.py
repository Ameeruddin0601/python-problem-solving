# #occurence of vowels in input string
# #eg: Hello Welcome
# #Output: e:3 
# #        o:2
# #Hllo Wlcm
# #if no vowels
# #Output: 0
# #if nothing in input string
# #Output: INVALID STRING

# input_str = input("Enter String: ") #input lia
# input_str = input_str.strip() #input me se spaces hataya
# VowelsPresent = False #flag concept use kia, vowels hai k nahi check karne
# if(len(input_str)>0): #input string me koi character h k nahi check kia
#     vowels = ['a','e','i','o','u'] #vowels ki list banaya
#     vowel_count = {'a':0,'e':0,'i':0,'o':0,'u':0} #vowels k count ki dictionary banake, har vowel ko 0 se initialise kia
    
#     for character in input_str.lower(): #input string ko lower karke usme character by character iterate kia
#         if character in vowels: #check kia k input string ka koi character vowels k list me present h k nahi
#             vowel_count[character] += 1 #agar input string ka koi character  vowels k list me present h, to uss character ka count vowel_count wali dictionary me badha diya
#             VowelsPresent = True #flag concept se mene check kia k vowels input string me present hai, islie True kardia usko
    
#     if VowelsPresent == False: #flag concept: agar input string me vowels present nahi h to ye False hi rahega
#         print(0) #Agar flase hai to direct 0 print karega
#     else:
#         for key,value in vowel_count.items(): #vowel count k items se key value uthaya
#             print(key,value,sep=":") #aur ye format me print kia eg: e:3

#         for vowel in vowels: #vowels wali list ko vowel by vowel iterate kia
#             input_str = input_str.replace(vowel,"") #aur input string me har vowel ko hataane k lie unko empty string se replace kia

#         print(input_str)    #orint kia input string
    
# else:
#     print("Invalid Input") #Agar input string khaali hai to ye print kia



#input me kch words milege
#uss input k har word me kitne vowels h count karna h
#jiss word me even no. of vowels aare unko 2 pts
#naito 1 pt
#aur last me pure pts add karke dene h

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y'] #vowels store kia

def score_words(words):
    score = 0 #0 se init kia
    for word in words: #words me se har word ko iterate kia
        num_vowels = 0 #number of vowels ka count h 0 se init kia
        for letter in word: #word me se har letter ko iterate kia
            if is_vowel(letter): #agar wo letter vowel h
                num_vowels += 1 #to no. of vowels me count badhaya
        if num_vowels % 2 == 0: #agar no. of vowels even h
            score += 2 #score me 2 add kia
        else:
            score +=1 #naito score me 1 add kia
    return score


n = int(input())
words = input().split()
print(score_words(words))
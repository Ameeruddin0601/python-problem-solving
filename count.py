#count the words in input string
# input_string = input().split() #splits acc to any white space and discards empty string
# print(len(input_string))

# #take input string, chose a target word and then count the appearance of that word in that string
# input_string  = input().lower().split()
# target_word = input()

# print(input_string.count(target_word))

'''
Q.
If inputs 2 512
Write a python program for following requirements 2* 2 = 4*2=8*2 =. .=512
Output =8
exp: -
#2*2=4 4*2=8 8*2-16 16*2=32 32*2=64
64*2=128 128*2=256 256*2=512
result=512
count=8
'''

input_lst = list(map(int, input().split()))
result = input_lst[0]
final = input_lst[1]
count = 0
while result<=final:
    count+=1    
    result = result * input_lst[0]
print(count-1)
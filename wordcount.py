#count the words in input string
input_string = input().split() #splits acc to any white space and discards empty string
print(len(input_string))

#take input string, chose a target word and then count the appearance of that word in that string
input_string  = input().lower().split()
target_word = input()

print(input_string.count(target_word))
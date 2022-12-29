#most occuring character in a string
#eg: string="aaaaabbbbbcccccc"

# def maxoccuring(string):
#     frequency_count = {}
#     string_set = set(string)
#     for i in string_set:
#         frequency_count[i] = string.count(i) #i->key count(i)->value
#     frequency_keys = list(frequency_count.keys()) #gets keys of dict
#     frequency_keys.sort() #sorted keys
#     max_value, max_key = 0, None
#     for i in frequency_keys:
#         if frequency_count[i] > max_value:
#             max_value = frequency_count[i]
#             max_key = i
#     return max_key, max_value
# print(maxoccuring("aaaaabbbbbccccc"))
# print(maxoccuring("aaaaabbbbbbbccccc"))

#no. of occuring substring in a string
#eg: string="ABCDCDC"
def count_substring(string,sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    print(count)
count_substring("AABCDCDC","CDC")        

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)
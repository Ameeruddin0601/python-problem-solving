'''Q1
An e-commerce site has a series of advertisements to display. 
Links to the ads are stores in a data structure 
and they are displayed or not is based on the value at bit position in a number. 
The sequence of ads being displayed at this time can be represented as a binary value. 
Where 1 means the ad is displayed and 0 means ad is not displayed. 
The ads should rotate. So, when the next page loads, ads that are displayed now are hidden and vice versa.'''
#Sample Input:
#>50
#Sample Output:
#>13
#Explaination: 50 in binary is 110010. Negate each bit in the sequence to get 001101 i.e. 13 in decimal.

# input_val=50
# input_val_bin = bin(input_val)[2:]
# output_val_bin = ""
# for bit in input_val_bin:
#     if bit=="1":
#         output_val_bin += "0"
#     else:
#         output_val_bin += "1"
        
# output_val = int(output_val_bin,2) #binary to decimal
# print(output_val)

'''
Q2
Write a program for finding pair of highest product
Input arr= [5,3,1,4,3,7,6,9,2]
Output-> 7,9
'''

# def maxprodpair(arr):
#     max_prod = 0
#     a=0
#     b=0
#     for i in range(len(arr)-1):
#         for j in range(i+1,len(arr)):
#             if arr[i]*arr[j]>max_prod:
#                 max_prod = arr[i]*arr[j]
#                 a=arr[i]
#                 b=arr[j]
#     return a,b
# print(maxprodpair([5,3,1,4,3,7,6,9,2]))

''''
Q3
You are given 'N' sticks each of negligible thickness and the ith stick has length A[i]. 
You have to form rectangles by choosing any four sticks.
Find the maximum area of rectangle that is possible.

notes: -
1) rectangle is a figure having opposite sides equal. 
2) A square is also a rectangle.

write a function rectangle which has following parameters.
1) number of sticks (integer)
2) integer array denoting length of sticks.
return value: integer denoting maximum possible area.

example1: 
Input: 5,[1 8 1 8 8]
Output: 8
Output description:- We can create a rectangle of 8*1 and it has maximum area.
example2: 
Input: 8,[4,2,3,2,3,4,5,1]
Output:- 12
'''

#Simple approach: remove sticks which do not have pair
#Sort the list
#multiply the second last and third last element

# def max_area_rect(n,arr):
#     newarr = []
#     for i in arr:
#         if arr.count(i)>=2 and i not in newarr:       
#             newarr.append(i)
#     max_area = 0
#     for i in range(len(newarr)-1):
#         for j in range(i+1,len(newarr)):
#             if arr[i]*arr[j]>max_area:
#                 max_area = arr[i]*arr[j]
#     return max_area
# print(max_area_rect(5,[1,8,1,8,8])) 


'''
Q4
You are given a string s of length n and an array of strings t containing m strings each of length n-1.
you need to remove one character from s such that s become equals to any of m strings.
find the total number of strings from the m given strings which can be obtained by 
removing one character from s.

input:-
length of string s (n): 5
enter string (s): 'abcde'

number of strings in t (m):- 4
enter strings (t):- ['abcd', 'abcc', 'cddd', 'acde']

output:- 2

explanation: - abcd - after removing 'e'
               acde - after removing 'b'
'''

# def match(n,str,m,arr):
#     count=0
#     newstr=[]
#     for i in str:
#         newstr.append(i)
#     for i in range(n):
#         chr = newstr.pop(i)
#         for word in arr:
#             if "".join(newstr)==word:
#                 count+=1
#         newstr.insert(i,chr)
#     return count
# print(match(5,'abcde',4,['abcd', 'abcc', 'cddd', 'acde']))

'''
Q5
Given an array of integers 'nums' and an integer 'target'. 
return indices of two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return answer in any order.

ex1.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
exp: nums[0]+nums[1]==target

ex2. nums = [3,2,4], target = 6
Output: [1,2]

ex3. nums [3,3], target = 6
Output: [0,1]
'''
def find_target(nums,target):
    output=[]
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target and len(output)==0:
                output.append(i)
                output.append(j)

    return output
print(find_target([3,3,2,4],6))
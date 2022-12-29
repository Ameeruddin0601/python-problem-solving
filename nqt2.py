# {1,2,3,7,5}
# brute force
# def subArraySum(arr, n, s):
#     for x in range(len(arr)):
#         summ=0
#         for y in range(x,len(arr)):
#             summ+=arr[y]
#             if summ==s:
#                 return x+1,y+1
#     return [-1]
# print(subArraySum([1,2,3,7,5],5,12))

# def plus_one(arrr):
#     string = ""
#     for i in arrr: # [1,2,3]
#         string+=str(i)
#     integer=int(string)
#     integer+=1 #124
#     new_arrrr=[]
#     for i in str(integer): #"124"
#         new_arrrr.append(int(i))
#     return new_arrrr
# print(plus_one([1,2,3]))

# sum of n numbers
# 1,2,3,4,5,6,7
# 28
# 1,2,3,5,6,7 ->4
# 24
# 4
# ans->4
# (n + 1)*(n + 2)/2
# def missing(arr):
#     n = len(arr)
#     total = (n + 1)*(n + 2)/2 #28
#     sum_a = sum(arr) #24
#     return int(total - sum_a)
# print(missing([1,2,3,5,6,7]))

# arr=[1,3,2,5]
# n=5
# for i in range(1,n+1):
#     if i not in arr:
#         print(i)
#         break

#len of last word of a string
# name = "Ameer Bagdadi"
# print(type(name))
# .strip() -> str ka method
# .split()
# len() -> str ka func
# string = "Hello World"
# li = string.split()
# print(len(li[-1]))

# li = [1, 8, 7, 56, 90]
# kchbhi = sorted(li) #sort sorted -> nlogn
# print(kchbhi[-1])

#[-6,-5,-4,1,2,3] -> -6,-5,3
# def maximumProduct(nums):
#     nums.sort()
#     neg_prod = nums[0] * nums[1] * nums[-1]
#     pos_prod = nums[-1] * nums[-2] * nums[-3]
#     return max(neg_prod,pos_prod)
# print(maximumProduct([-6,-2,1,2,3,4]))

# def isMonotonic(nums):
#     return sorted(nums)==nums or sorted(nums,reverse=True)==nums
# print(isMonotonic([1,3,2]))

# from itertools import accumulate
# def subArraySum(arr):
#     summ=0
#     res_arr=[]
#     for x in arr: 
#         summ+=x 
#         res_arr.append(summ)
#     return res_arr
# #print(list(accumulate([1,2,3,7,5])))
# print(subArraySum([1,2,3,7,5]))

# from collections import Counter
# def findDuplicates(nums):
#     freq = {}
#     # freq = Counter(nums)    
#     for x in nums: 
#         if x in freq: 
#             freq[x]+=1
#         else:
#             freq[x]=1
#         # freq[x]=freq.get(x,0)+1        
#     ans=[]
#     for x in freq:
#         if freq[x]==2:
#             ans.append(x)
#     return ans
# print(findDuplicates([4,3,2,7,8,2,3,1]))

# def revString(input_arr):
#     n=len(input_arr)
#     for i in range(len(input_arr)//2):
#         input_arr[i],input_arr[~i]=input_arr[~i],input_arr[i]
#     return input_arr
# print(revString(["h","e","l","l","o"]))

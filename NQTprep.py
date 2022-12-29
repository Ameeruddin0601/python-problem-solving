#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
# def subArraySum(arr, n, s):
#     for x in range(len(arr)):
#         for y in range(x,len(arr)):
#             if sum(arr[x:y+1])==s:
#                 return x+1,y+1
#     return [-1]
# print(subArraySum([1,2,3,7,5],5,12))
# def subArraySum(arr, n, s):
#     for x in range(len(arr)):
#         summ=0
#         for y in range(x,len(arr)):
#             summ+=arr[y]
#             if summ==s:
#                 return x+1,y+1
#     return [-1]
# print(subArraySum([1,2,3,7,5],5,12))

#https://leetcode.com/problems/plus-one/
# def plus_one(arrr):
#     string = ""
#     for i in arrr:
#         string+=str(i)
#     integer=int(string)
#     integer+=1
#     arrrr=[]
#     for i in str(integer):
#         arrrr.append(int(i))
#     return arrrr
# print(plus_one([1,2,3]))

#https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1
# arr=[1,3,2,5]
# n=5
# for i in range(1,n+1):
#     if i not in arr:
#         print(i)
#         break
# print(arr)

# def missing(arr):
#     n = len(arr)
#     total = (n + 1)*(n + 2)/2
#     sum_a = sum(arr)
#     return total - sum_a
# print(missing([1, 2, 3, 5]))

#https://leetcode.com/problems/maximum-product-of-three-numbers/
#[-6,-5,-4,1,2,3] -> -6,-5,3
# def maximumProduct(nums):
#     nums.sort()
#     neg_prod = nums[0] * nums[1] * nums[-1]
#     pos_prod = nums[-1] * nums[-2] * nums[-3]
#     return max(neg_prod,pos_prod)
# print(maximumProduct([-6,-2,1,2,3,4]))

#https://leetcode.com/problems/monotonic-array/
# def isMonotonic(nums):
#     return sorted(nums)==nums or sorted(nums,reverse=True)==nums
# print(isMonotonic([1,2,3]))

# https://leetcode.com/problems/running-sum-of-1d-array/
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

#https://leetcode.com/problems/find-all-duplicates-in-an-array/
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
# print(findDuplicates([1,2,2,3,3]))

# https://practice.geeksforgeeks.org/problems/largest-element-in-array4009/0/
#max func

#https://practice.geeksforgeeks.org/problems/first-repeating-element4018/1
# def first_rep(arr):
#     for i in range(len(arr)):
#         if arr[i] in arr[i+1:]:
#             return i+1
#     return -1
# print(first_rep([1, 5, 3, 4, 3, 5, 6]))

# from collections import Counter
# def first_rep(arr):
#     freq = Counter(arr)
#     for ind,x in enumerate(arr):
#         if freq[x] > 2:
#             return ind+1
#     return -1
# print(first_rep([1, 5, 3, 4, 3, 5, 6]))

#https://practice.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1
# def search(self,arr, N, X):
#     for i in range(len(arr)):
#         if arr[i]==X:
#             return i
#     return -1 

#STRING
#https://leetcode.com/problems/implement-strstr/
# haystack = "hello"
# needle = "ll"
# try:
#     print(haystack.index(needle))
# except:
#     print(-1)
#print(haystack.find(needle))

#https://leetcode.com/problems/length-of-last-word/
# string = "Hello World"
# li = list(string.split())
# print(len(li[-1]))

#https://leetcode.com/problems/add-binary/
# num1= "1010"
# num2 = "1011"
# print(bin(int(num1,2)+int(num2,2))[2:])

#https://leetcode.com/problems/reverse-string/
# def revStr(input_arr):
#     for i in range(len(input_arr)//2):
#         input_arr[i],input_arr[~i]=input_arr[~i],input_arr[i]
#     return input_arr
#     # input_arr.reverse()
#     # return input_arr
#     # return input_arr[::-1]
# print(revStr(["h","e","l","l","o"]))

#https://leetcode.com/problems/valid-anagram/
# from collections import Counter
# def validAnagram(s,t):
#     # return sorted(s) == sorted(t)
#     return Counter(s) ==  Counter(t)
# print(validAnagram("anagram","nagaram"))

#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
# def checkEquiv(word1,word2):
#     return "".join(word1) == "".join(word2)
# print(checkEquiv(["ab", "c"],["a", "bc"]))

#https://leetcode.com/problems/valid-palindrome/
# def isPalindrome(s):
#     temp = ""
#     for i in s.lower():
#         if i.isalnum() == True:
#             temp+=i
#     return temp == temp[::-1]

# print(isPalindrome("A man, a plan, a canal: Panama"))

#https://leetcode.com/problems/capitalize-the-title/
# def capitalizeTitle(s):
#     arr=s.split()
#     for x in range(len(arr)):
#         if len(arr[x])>2:
#             arr[x]=arr[x].capitalize()
#         else:
#             arr[x]=arr[x].lower()
#     return " ".join(arr)
# print(capitalizeTitle("mY NamE iS AmeEruDDin"))

#https://practice.geeksforgeeks.org/problems/union-of-two-sorted-arrays/1
# def unionSet(a,b):
#     seta=set(a)
#     setb=set(b)
#     ans = seta.union(setb)
#     return sorted(ans)
# print(unionSet([1, 2, 3, 4, 5],[1, 2, 3]))

#https://leetcode.com/problems/ransom-note/
# from collections import Counter
# def ransomNote(a,b):
#     counta = Counter(a)
#     countb = Counter(b)
#     for x in counta:
#         if counta[x] > countb[x]:
#             return False
#     return True
# print(ransomNote("aa","aba"))

#https://leetcode.com/problems/uncommon-words-from-two-sentences/
from collections import Counter
def unCommon(a,b):
    temp = a.split() + b.split()
    freq = Counter(temp)
    ans = []
    for key,val in freq.items():
        if val==1:
            ans.append(key)
    return ans

print(unCommon("this apple is sweet","this apple is sour"))

'''Q1
ebay wants to sell several products
price of products are given
shipping distance is given from fulfillment zone to delivery point
SKUs- ordered product is available or not in fulfilment zone
Find max discount price if certain product can be shipped'''

# num_of_products = int(input())
# products_price= list(map(int,input().split()))
# distance = list(map(int,input().split()))
# sku =list(map(int,input().split()))

# for product in range(num_of_products):
#     if sku[product] > 0:
#         print(products_price[product]*distance[product],end=" ")

##or using zip method
# for product_price, dist, s in zip(products_price, distance, sku):
#     if s > 0:
#         print(product_price * dist, end=" ")

##use zip for iterating in multiple lists
##search ennumerate


'''Q2
Write a program to display the words that are repeated 
more than or equal to N times in the text.
if no word is repeated N times then return NA
words are case sensitive'''

# sentence = input("Enter a sentence: ")
# n= int(input("Enter a number: "))

# sentence = sentence.split()
# wordCount = {}

# for i in sentence:
#     if i in wordCount:
#         wordCount[i]+=1
#     else:
#         wordCount[i]=1

# result=[]

# for i in wordCount:
#     if wordCount[i]>=n:
#         result.append(i)

# print(result if result else "NA")

'''Q3
Write a program to sort characters and numbers
so that first alphabets and then numbers are 
printed'''

# input_str="B7A1R3"
# alphabets=[]
# nums=[]
# for ch in input_str:
#     if ch.isalpha():
#         alphabets.append(ch)
#     else:
#         nums.append(ch)

# print("".join(sorted(alphabets)+sorted(nums)))
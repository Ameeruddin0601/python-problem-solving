# #find second largest number from the array/list
# #eg: li=[1,3,4,5,8,9,78] -> 9
# #sort approach. PS: sort method kch return nai karta, balki di gayi list ko wahi pe sort karke rakh deta h
# def secondMax(li):
#     li.sort()
#     return li[-2] #second last element
# print(secondMax([1,56,78,98,45,6]))


# #what if sort method is not allowed
# #using max function
# def secondMax(li):
#     maxvalue = max(li)
#     li.remove(maxvalue)
#     return max(li)
# print(secondMax([1,56,78,98,45,6]))

#time limit exceeds in both above approach
#use loops
# def secondMax(li):
#     li.sort()
#     maxvalue = li[0]
#     secondMaxValue = li[0]
#     #first for loop to find max value
#     for i in range(len(li)):
#         if li[i]>maxvalue:
#             maxvalue = li[i]
#     #second for loop to find second max value
#     for i in range(len(li)):
#         if li[i]>secondMaxValue and li[i]!=maxvalue:
#             secondMaxValue = li[i]
#     return secondMaxValue
# print(secondMax([57,57,-57,57]))

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr.sort()
#     winner = arr[0]
#     runnerup = arr[0]
#     for i in range(len(arr)):
#         if(arr[i]>winner):
#             winner=arr[i]
#     # print(winner)
#     for i in range(len(arr)):
#         if(arr[i]>runnerup and arr[i]!=winner):
#             runnerup=arr[i]
#     print(runnerup)


#like system: Implement the function which takes an array containing the names of people that like an item. 
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# def likes(names):
#     x=len(names)
#     if x==0:
#         return f'no one likes this'
#     elif x==1:
#         return f'{names[0]} likes this'
#     elif x==2:
#         return f'{names[0]} and {names[1]} like this'
#     elif x==3:
#         return f'{names[0]}, {names[1]} and {names[2]} like this'
#     else:
#         return f'{names[0]}, {names[1]} and {x-2} others like this'
# print(likes(['Ameer','Sameer','Tameer','Kameer','Zameer']))


# You live in the city of Cartesia where all roads are laid out in a perfect grid. 
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
# The city provides its citizens with a Walk Generating App on their phones -- 
# everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
# You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, 
# so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) 
# and will, of course, return you to your starting point. Return false otherwise.
# def is_valid_walk(walk):
#     if len(walk)==10:
#         if(walk.count("n")==walk.count("s") and walk.count("w")==walk.count("e")):
#             return True
#     return False
# print(is_valid_walk(['n', 's', 'n', 's', 'w', 'w', 'e', 'w', 'n', 's']))


#Given an array of integers your solution should find the smallest integer.
# def find_smallest_int(arr):
#     return min(arr)
# print(find_smallest_int([78, 56, 232, 12, 11, 43]))

#2 arrays are given, return true if all the numbers of second arr are eqaul to the squares of all th enumbers of first array
# def comp(array1, array2):
    # if array1!=None and array2!=None:
    #     return sorted([i ** 2 for i in array1]) == sorted(array2) 
    # return False

#     array1.sort()
#     array2.sort()
#     for i in range(len(array1)):
#         if array1[i]**2==array2[i]:
#             return True
#     return False
# print(comp([121, 144, 19, 161, 19, 144, 19, 11],[121, 144, 19, 161, 19, 144, 19, 11]))


# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order.
# def array_diff(a, b):
#     return [i for i in a if i not in b]
# print(array_diff([1,2,2,2,3],[2]))

# def to_jaden_case(string):
#     # ...
#     li = string.split()
#     return " ".join(i.capitalize() for i in li)
# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

#first repeat
# def first_rep(arr):
#     # li=[]
#     for i in range(1,len(arr)):
#         if arr[i] in arr[i-1:0:-1]:
#             # li.append(arr[i])
#             print(arr[i],arr.index(arr[i]),sep="->")
#             break
#     # print(li)
# first_rep([1,2,3,4,4,3,2,5,8,6])

#iterate a list without using loops
lst=[10,20,30,40,50,60]
start_idx = 0
end_idx = len(lst)
def iterate(lst,start_idx,end_idx):
    if start_idx<0 or start_idx>=end_idx:
        return
    print(lst[start_idx],start_idx,end_idx)
    iterate(lst,start_idx+1,end_idx)
    
print(iterate(lst,start_idx,end_idx))
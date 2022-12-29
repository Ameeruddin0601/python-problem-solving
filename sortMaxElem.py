#take 1 array with 2 param
#1 param-> size of array
#2 param-> elements of array

#take 2nd array with 2 param
#1 param-> size of array
#2 param-> elements of array

#print max element from both the arrays

size1=int(input())
array1=list(map(int, input().split()))
size2=int(input())
array2=list(map(int, input().split()))

def arraySort(size,array):
    array.sort()

def findMax(array1,array2):
    return max(max(array1),max(array2))

print(findMax(array1,array2))
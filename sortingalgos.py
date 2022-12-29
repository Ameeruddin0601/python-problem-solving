arr=[2,6,5,1,3,4]

#insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    print(arr)
#insertion_sort(arr)

def selection_sort(arr):
    for i in range(len(arr)-1):
        curr_min_idx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[curr_min_idx]:
                curr_min_idx = j
        arr[i],arr[curr_min_idx] = arr[curr_min_idx],arr[i]
    print(arr)
#selection_sort(arr)

def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i,j,k = 0,0,0

        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1
        
        while i<len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        
        while j<len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1
        
    
# merge_sort(arr)
# print(arr)

def quickSort(arr,start,end):
    if start<end:
        pi = partition(arr,start,end)
        quickSort(arr,start,pi-1)
        quickSort(arr,pi+1,end)

def partition(arr,start,end):
    pivot_idx = start
    pivot = arr[pivot_idx]

    while start<end:
        while start<len(arr) and arr[start]<=pivot:
            start+=1
        while arr[end]>pivot:
            end-=1
        
        if start<end:
            arr[start],arr[end] = arr[end],arr[start]

    arr[pivot_idx],arr[end] = arr[end],arr[pivot_idx]
    return end

# quickSort(arr,0,len(arr)-1)
# print(arr)

def bubbleSort(arr):
    swapped = False
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
# bubbleSort(arr)
# print(arr)

#binary search
arr=[25,15,78,96,56,24,69,12]
arr.sort()
def binarySearch(arr,target):
    left_idx = 0
    right_idx = len(arr)-1
    mid_idx = 0

    while left_idx<=right_idx:
        mid_idx = left_idx + right_idx // 2
        mid_term = arr[mid_idx]

        if mid_term == target:
            return mid_idx
        
        elif mid_term < target:
            left_idx = mid_idx+1
        
        else:
            right_idx = mid_idx-1

# print(binarySearch(arr,69))

            


#Given an integer array, find all the unique pairs that 
#sum upto a specific value "k"
def sum_pair(arr,k):
    seen={}
    output=set()

    for index,value in enumerate(arr):
        if k - value in seen:
            output.add((value, k - value))
        else:
            seen[value] = index
    return len(output)  
print(sum_pair([1,1,1,1,2,2],4))

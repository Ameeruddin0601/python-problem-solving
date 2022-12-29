#take 2 inputs 
#in between these 2 inputs how many number are divisible by 3 and 5
#give the sum of those numbers
m = int(input('m : '))
n = int(input('n : '))

def sumNumberDivisible(m,n):
    total_sum=0
    for i in range(m,n+1):
        if i%3==0 and i%5==0:
            total_sum += i
    return total_sum

    #using list comprehension
    # return sum([i for i in range(m,n+1) if i%3==0 and i%5==0])

print(sumNumberDivisible(m,n))



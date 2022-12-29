def square_sum(numbers):
    res = 0
    for i in numbers:
        res += i**2
    return res
    #return sum(x ** 2 for x in numbers)
print(square_sum([0,3,4,5]))

#fibonnacci series
#starts with 0 and 1
#every next element will be addition of prev 2 elements
#0 1 1 2 3 5 8 13 21......

# def fibonacci(input_num):    
#     a, b = 0, 1
#     if input_num==1:
#         print(a,b)
#     elif input_num>1:
#         print(a,b ,end=" ")
#         for x in range(input_num - 2):
#             c = a + b
#             print(c, end=" ")
#             a , b = b , c
#     else:
#         print(0)
# fibonacci(0)
# fibonacci(1)
# fibonacci(5)

#print nth number of fibonacci series
# def ntermfibonacci(input_num):    
#     a, b = 0, 1
#     for x in range(input_num - 2):
#         c = a + b
#         a , b = b , c
#     return c
# print(ntermfibonacci(5))

def tribonacci(signature,n):    
    a, b, c = signature
    if n==0:
        return []
    elif n==1:
        return [a]
    elif n==2:
        return [a,b]
    elif n==3:
        return [a,b,c]
    elif n>3:
        for x in range(n-3):
            d= a+b+c
            signature.append(d)
            a,b,c=b,c,d
    return signature
print(tribonacci([5,7,8], 1))
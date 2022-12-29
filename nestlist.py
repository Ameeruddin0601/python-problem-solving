data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    print('data',m)
    v = m[0][0]
    print('v',v)
 
    for row in m:
        for element in row:
            print('elements:',element)
            if v < element: v = element
 
    return v
print(fun(data[0]))
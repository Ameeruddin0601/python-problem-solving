#pehle 3 input lege
#1st input is-> length of list
#2nd input is -> starting range
#3rd input is -> ending range
#fir 6 input lege-> wo distance hoge
#apneko starting range aur ending range k beech me jitne bhi distances hai unka index print karna h

size, startrange, endrange = map(int, input().split())
employee = list(map(int, input().split()))

print(*[x for x in range(size) if employee[x] in range(startrange, endrange)])

# for x in range(size):
#     if employee[x] in range(startrange, endrange):
#         print(x, end=" ")

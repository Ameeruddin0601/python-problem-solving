#ek number diya rahega
#uske even position pe jo number h wo nikaalna h
#uske odd position pe jo number h wo nikaalna h
#dono ko subtract kardena h

input_num = input()

numateven = list(input_num[1::2])
for num in range(len(numateven)):
    numateven[num] = int(numateven[num])

numatodd = list(input_num[0::2])
for num in range(len(numatodd)):
    numatodd[num] = int(numatodd[num])

print(abs(sum(numateven) - sum(numatodd)))

#OR
input_num = input()
even,odd=0,0
for num in range(len(input_num)):
    if num%2==0:
        even += int(input_num[num])
    else:
        odd += int(input_num[num])

print(abs(even - odd))

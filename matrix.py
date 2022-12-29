#pehle number of rows and cols lena h
#fir matrix k inputs lena h
#fir har row k numbers ka addition karna h
#fir jo row ka max sum aaega usko display karna h

rows, cols = map(int,input().split())
sum_of_matrix_rows = []

for i in range(rows):
    sum_of_matrix_rows.append(sum(list(map(int,input().split()))))
    #input lia split karke, fir map se int me convert kia, fir list me convert kia, fir sum nikaal k dusri list me append kardia

for i in range(1,rows+1):
    print('Row '+str(i)+" : "+str(sum_of_matrix_rows[i-1]))

print('Row',sum_of_matrix_rows.index(max(sum_of_matrix_rows))+1,' is having the maximum sum : ',max(sum_of_matrix_rows))


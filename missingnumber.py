#array dega jisme 1 to N numbers honge, unordered
#lekin ek number overriden hoga, wo overriden number print karao
#1<=N<=500
#eg: input 5
#1 2 100 5 3
#output: 4
#normally array me 1,2,3,4,5 hona chahiye
#but 4 ki jaga 100 override hua h
#so output me 4 aaega

maxNum = int(input()) #array kitna bada ho, wo value
numbers = [] #array

for x in range(maxNum): #jitna bada array utna iteration
    numbers.append(int(input())) #array me values bhara

for missingNum in range(1,maxNum+1): #fir se jitna bada array utni baar iterate kia
    if missingNum not in numbers: #check kia k konsa number missing hai numbers k array me se
        print(missingNum) #missing number print kia
        break



'''Q1
An e-commerce site has a series of advertisements to display. 
Links to the ads are stores in a data structure 
and they are displayed or not is based on the value at bit position in a number. 
The sequence of ads being displayed at this time can be represented as a binary value. 
Where 1 means the ad is displayed and 0 means ad is not displayed. 
The ads should rotate. So, when the next page loads, ads that are displayed now are hidden and vice versa.'''
#Sample Input:
#>50
#Sample Output:
#>13
#Explaination: 50 in binary is 110010. Negate each bit in the sequence to get 001101 i.e. 13 in decimal.

input_val=50
input_val_bin = bin(input_val)[2:]
output_val_bin = ""
for bit in input_val_bin:
    if bit=="1":
        output_val_bin += "0"
    else:
        output_val_bin += "1"
        
output_val = int(output_val_bin,2) #binary to decimal
print(output_val)
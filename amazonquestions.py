def amazonq1(sw,rw):
    p=0
    q=0
    while p<len(sw):
        if sw[p]==rw[q]:
            q+=1
            if q==len(rw):
                return 0
        p+=1
    return len(rw)-q

print(amazonq1("armate","amazon"))

#greyness popular question
def amazonq2(pixels):
    maxgreyness=0
    n=len(pixels)
    m=len(pixels[0])
    for i in range(n):
        for j in range(m):
            white=0
            black=0
            for k in range(m):
                if pixels[i][k]==0:
                    white+=1
                else:
                    black+=1
            
            for k in range(n):
                if pixels[k][j]==0:
                    white+=1
                else:
                    black=+1
        greyness=black-white
        if i==0 and j==0 or greyness>maxgreyness:
            maxgreyness = greyness
    return maxgreyness
print(amazonq2(["011","101","001"]))
    
 
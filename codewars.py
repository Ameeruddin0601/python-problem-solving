#Range Extraction
def solution(args):
    res=[]
    tmp=args[0]
    i,j=0,0
    n=len(args)
    if args:
        while i<n:
            tmp=args[i]
            j=i
            while j<n-1 and args[j+1] == args[j]+1:
                j+=1
            if j-i>1:
                tmp = str(args[i])+"-"+str(args[j])
                i=j+1
            else:
                i= (j if j>i else i+1)
            res.append(tmp)
    return ",".join(str(x) for x in res)
print(solution([-6,-5,-4,-1,0,1,3,4,6,7,9,10,11]))
#Contest solutions

# tc=int(input())

# for j in range(tc):
#     x,y=map(int, input().split())
#     z=x*y
#     if z<100:
#         print(0,z)
#     else:
#         print(z//100,z)

# tt=50
# x=10
# y=5
# z=tt%x
# if tt%x==0:
#     print(tt//x)
# elif((tt//x)*x+(tt%x//y)*y)==tt:
#     print((tt//x)+(tt%x//y))
# else:
#     print(-1)

# tb=4
# cost=2
# z=tb//3
# tb=tb-z
# print(tb*cost)

# a=str(10) 
# li=[]

# for i in a:
#     if int(i)%2==0:
#         li.append(int(i))

# if len(li)>=2:
#     print("Yes")
# else:
#     print("No")  

# tc=int(input())
# for j in range(tc):
#     x,y=map(int, input().split())
#     if x>y:
#         print("Yes")
#     else:
#         print("No")

# tc=int(input())
# for j in range(tc):
#     x,y,m=map(int, input().split())
#     z=x*m
#     if z>=y:
#         print("No")
#     else:
#         print("Yes")
#         tc=int(input())

# tc=int(input())
# for j in range(tc):
#     x,y=map(int, input().split())
#     z=y//x
#     while z*x<y:
#         z+=1
#     print(z-1)

# tc=int(input())
# for j in range(tc):
#     x,y=map(int, input().split())
#     if x%2==0:
#         if x+2<=y:
#             print(x,x+2)
#         else:
#             print(-1)
#     else:
#         if x+3<=y:
#             if x%3==0:
#                 print(x,x+3)
#             else:
#                 print(x+1,x+3)
#         else:
#             print(-1)

# tc=int(input())
# for j in range(tc):
#     x,y,z=map(int, input().split())
#     if x>=y+(z*2):
#         print("Yes")
#     else:
#         print("No")

# tc=int(input())
# for j in range(tc):
#     x,y,z=map(int, input().split()) 
#     ans = 0
#     for i in range(x+1):
#         if y>x:
#             ans=z
#         elif x%y==0 and y*i<=x:
#             ans=i*z
#         else:
#             if x%y!=0 and y*i<=x:
#                 ans=(i+1)*z
#     print(ans)

# tc=int(input())
# for j in range(tc):
#     x=int(input())
#     totalattempt=0
#     wrongattempts = 0
#     if x%3!=0:
#         totalattempt = x//3+1
#         wrongattempts = totalattempt*3-x
#     else:
#         wrongattempts = 0
# print(wrongattempts)

tc=int(input())
for j in range(tc):
    x,y,z=map(int, input().split())
    arr=list(map(int, input().split()))
    
    for i in range(len(arr)+1):
        if i not in arr[i:y+1] and i==z:
            print("Yes")
        else:
            print("No")


# li = [int(x) for x in input().split()]
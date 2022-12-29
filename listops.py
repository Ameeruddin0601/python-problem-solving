# if __name__ == '__main__':
#     N = int(input())
#     li = []
#     for _ in range(N):
#         # li.append(i)
#         e = input().split()
#         if(e[0]=='insert'):
#             li.insert(int(e[1]),int(e[2]))
#         elif(e[0]=='remove'):
#             li.remove(int(e[1]))
#         elif(e[0]=='append'):
#             li.append(int(e[1]))
#         elif(e[0]=='sort'):
#             li.sort()
#         elif(e[0]=='pop'):
#             li.pop()
#         elif(e[0]=='reverse'):
#             li.reverse()
#         else:
#             print(li)
        

#filter list
# def filter_list(l):
#     li=[]
#     for i in l:
#         if type(i)==int:
#             li.append(i)
#     return li
# print(filter_list([1,2,'aasf','1','123',123]))

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1+value2
    if operator == '-':
        return value1-value2
    if operator == '*':
        return value1*value2
    if operator == '/':
        return value1/value2
print(basic_op('+', 4, 7))
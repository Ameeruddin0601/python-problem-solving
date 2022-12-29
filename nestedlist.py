#ek students ki list hai
#uss list me har ek student ki list hai
#uss list me student ka naam sur marks h
#apneko secondlowest marks walw bacche print karne h
#agar do log k marks same h to unko alphbetically print karna h

if __name__ == '__main__':
    students = []
    scoresheet = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scoresheet.append(score)

    second_lowest = sorted(set(scoresheet))[1]
    for name,score in students:
        if score==second_lowest:
            print(name)
        
#list comprehension use kia
#jitne b score h wo lia students me se aur uska set banaya
#set ko sort kardia

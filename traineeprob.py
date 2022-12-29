#fitness test of trainees
#3 rounds. Record oxygen lvl after every rounds
#Calculate avg oxygen lvl of every trainee
#jiska highest hoga wo first
#2 log ka same aaya to dono ko select karna hai

#oxygen lvl between 1-100
#avg oxygen lvl below 70 will be unfit
#avg oxygen value shud be rounded

oxygen = []

for x in range(9):
    oxygenLvl = int(input())
    if oxygenLvl not in range(1,100):
        oxygen.append(0)
    else:
        oxygen.append(oxygenLvl)

trainee1 = round(sum(oxygen[0::3]) / 3)
trainee2 = round(sum(oxygen[1::3]) / 3)
trainee3 = round(sum(oxygen[2::3]) / 3)

if trainee1>=trainee2 and trainee1>=trainee3:
    if trainee1<70:
        print("Trainee is unfit")
    else:
        print("Trainee Number:", 1)
if trainee2>=trainee1 and trainee2>=trainee3:
    if trainee2<70:
        print("Trainee is unfit")
    else:
        print("Trainee Number:", 2)
if trainee3>=trainee1 and trainee3>=trainee2:
    if trainee3<70:
        print("Trainee is unfit")
    else:
        print("Trainee Number:", 3)


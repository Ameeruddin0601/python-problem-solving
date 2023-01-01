'''
Suppose, There is an analog Clock having second hand only. User has 3 attempts to stop second hand. User will be awarded with points a/c to following:-
If second hand stops at [1,5,9,11] - 10 points
If second hand stops at [4,7,8,10]: 20 points
If second hand stops at [3,2,6,12] - 30 points Also, consider there are three players, declare the winner of the game.
-
note:- Imagine second hand stops only at digit of clock.
sample run: -
Press 'Enter' to continue and 'ctrl+c' to stop seconds hand of clock: Enter}
1
2
3
stopped and points are added
5
6
7 8
9
10
stopped and points are added
12
1
2
3
4
5
stopped and points are added
Total score: 50
'''
from time import sleep

def run():
    print("Press 'Enter' to comtinue and 'ctrl+c' to stop")
    attempts=1
    points=0
    points_table={}
    name=input("Enter the player name: ")
    while True:
        try:
            for digit in range(1,13):
                print(digit)
                sleep(0.2)
        except KeyboardInterrupt:
            print(f"Time Stopped at {digit}")
            
            if digit in [1,5,9,11]:
                points=points+10
            elif digit in [4,7,8,10]:
                points=points+20
            else:
                points=points+30
            print(f"Points are added: {points}")
            sleep(2)
            attempts+=1
            if attempts==4:
                print(f"{name} has scored {points} points")
                points_table[name]=[points]
                ans=input("Is there any other player? (y/n): ").lower()
                if ans=='y':
                    name=input("Enter the player name: ")
                    points=0
                    attempts=1
                else:
                    print(points_table)
run()
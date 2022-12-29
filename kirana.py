#Kirana Store Calcy & Reciept Generator
#keep adding stream of input values untill user presses q
total = 0
while(True):
    price = input("Enter The Price Or Press 'q' to exit: ")
    if(price != 'q'):
        total += int(price)
        print(f"Total So Far: {total}")
    else:
        print(f"Your total amount is {total}. Thank You!")
        break
mainMenu = input()
subMenu = int(input())

Menu = {'c':{
    1:'Expresso Coffee',
    2:'Cappucino Coffee',
    3:'Latte Coffee'
},'t':{
    1:'Plain Tea',
    2:'Assam Tea',
    3:'Ginger Tea'
},'s':{
    1:'Hot & Sour Soup',
    2:'Veg Corn Soup',
    3:'Tomato Soup'
},'b':{
    1:'Hot Chocolate',
    2:'Badam Drink',
    3:'Badam Pista Drink'
}}

if mainMenu not in Menu.keys() or subMenu not in Menu[mainMenu].keys():
    print("Invalid Order")
else:
    print("Welcome To CCD")
    print("Enjoy Your ",Menu[mainMenu][subMenu])

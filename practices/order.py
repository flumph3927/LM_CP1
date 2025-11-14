#LM 2nd Order Up

#set MENU to dictionary containing dictionaries of other types
#create function display
#   set OUT to empty string
#   loop through dictionary
#       add name of sub-dictionary to OUT
#       loop through sub-dictionary
#           add item and price to OUT
#   display welcome
#   display OUT
#create function get order
#   loop until DRINK is valid input:
#       set DRINK to user input
#   loop until MAIN is valid input:
#       set MAIN to user input
#   loop until SIDES are valid inputs:
#       set SIDES to user inputs
#   return DRINK, MAIN, SIDES
#create function price, pass DRINK, MAIN, SIDES
#   add prices of DRINK, MAIN and SIDES to new variable PRICE
#   display PRICE
#   set TOTAL to PRICE and tax
#   display TOTAL
#call function display
#set ITEMS to function get order
#call function price on ITEMS

#set MENU to dictionary containing dictionaries of other types
menu={
    'Drinks:': {
        'water': 2.35,
        'mud': 1.23
    },
    'Main Courses:': {
        'soot': 3.22,
        'gravel': 3.98,
        'dirt': 5.78,
        'sand': 6.65,
        'permafrost': 9.65
    },
    'Sides:':{
        'silt': 1.45,
        'loam': 1.64,
        'ash': 1.38,
        'iron filings': 3.89,
        'salt': 1.97,
    }
}

#create function display
def display(menu):
#   set OUT to empty string
    out=''
#   loop through dictionary
    for i in menu:
#       add name of sub-dictionary to OUT
        out+=i+'\n'
#       loop through sub-dictionary
        for x in menu[i]:
#           add item and price to OUT
            out+=x+' '+str(menu[i][x])+'\n'
#   display welcome
    print('Welcome to Hoomin\'s Dirt Eat Place')
#   display OUT
    print(out)

#create function get order
def getOrder(all):
#   loop until DRINK is valid input:
    drink=''
    while drink not in all['Drinks:'].keys():
#       set DRINK to user input
        drink = input('What drink would you like? ')
#   loop until main is valid input:
    main=''
    while main not in all['Main Courses:'].keys():
#       set MAIN to user input
        main = input('What main course would you like? ')
#   loop until Sides are valid inputs:
    sides=[]
    for i in range(2):
        side=''
        while side not in all['Sides:'].keys():
#           set SIDES to user inputs
            side = input('What side would you like? (you will choose two) ')
        sides.append(side)
#   return DRINK, MAIN, SIDES
    return [drink, main, sides]

#create function price, pass DRINK, MAIN, SIDES
def price(grid, foods):
#   add prices of DRINK, MAIN and SIDES to new variable PRICE
    pric=grid['Drinks:'][foods[0]]+grid['Main Courses:'][foods[1]]+grid['Sides:'][foods[2][0]]+grid['Sides:'][foods[2][1]]
#   display PRICE
    print(f'Subtotal: ${pric}')
#   set TOTAL to PRICE and tax
    total=round(pric*1.085,2)
#   display TOTAL
    print(f'Total: ${total}')

#call function display
display(menu)
#set ITEMS to function get order
items=getOrder(menu)
#call function price on ITEMS
price(menu, items)
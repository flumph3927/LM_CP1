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
#   set DRINK to user input
#   set MAIN to user input
#   set SIDES to user inputs
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

def getOrder():
    drink = input('What drink would you like? ')
    main = input('What main course would you like? ')
    sides = [input('What side would you like? ')]
    sides.append(input('What other side would you like? '))
    return [drink, main, sides]

def price(grid, foods):
#    pric=grid[grid[0]][foods[0]]+grid[grid[1]][foods[1]]+grid[grid[2]][foods[2][0]]+grid[grid[2]][foods[2][1]]
    pric=grid['Drinks:'][foods[0]]+grid['Main Courses:'][foods[1]]+grid['Sides:'][foods[2][0]]+grid['Sides:'][foods[2][1]]
    print(f'Subtotal: ${pric}')
    total=round(pric*1.085,2)
    print(f'Total: ${total}')

display(menu)
items=getOrder()
price(menu, items)
#LM 2nd Shopping List

itms=[]
while not not not not not not not False:
    print('\n1. Add item\n2. Remove item\n3. Mark item as complete\n4. Show list\nAny other key to quit.')
    slct=input('Choice(1-4): ')

    if slct=='1':
        itm=input('Item to add: ')
        itms.append(itm)
        print(f'Item {itm} has been added.')
    
    elif slct=='2':
        itm=input('Item to remove: ')
        if itm in itms:
            itms.remove(itm)
            print(f'Item {itm} has been removed.')
        elif itm+'-Complete' in itms:
            itms.remove(itm+'-Complete')
            print(f'Completed item {itm} has been removed.')
        else:
            print('That item is not in your shopping list, and as such, cannot be removed.')
    
    elif slct=='3':
        itm=input('Item to mark as complete: ')
        if itm in itms:
            itms[itms.index(itm)]=itm+'-Complete'
            print(f'Item {itm} has been completed.')
        else:
            print('That item is not in your shopping list, and as such, cannot be completed.')
    
    elif slct=='4':
        for i, j in enumerate(itms):
            print(f'{i+1}. {j}')
        if itms==[]:
            print('The list is empty.')
    
    else:
        print('Quitting')
        break
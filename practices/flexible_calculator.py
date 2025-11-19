#LM 2nd Flexible Calculator
'''
define function calculate, NUMBERS
    set OPERATION to first in NUMBERS and NUMBERS to second in NUMBERS
    if OPERATION is sum return NUMBERS added together
    else if OPERATION is average return NUMBERS added together, divided by number of NUMBERS
    else if OPERATION is max return largest number in NUMBERS
    else if OPERATION is min return smallest number in NUMBERS
    else if OPERATION is product return NUMBERS multiplied together
define function check, get INPUT
    try to make INPUT a float and return it, if error, return False
display enter numbers, done to stop entering numbers
set NUMS to empty list and INPUT to user input
loop while INPUT not done:
    if function check passed INPUT is not false, add INPUT to NUMS, else display invalid input
    set INPUT to user input
display operation options
set TYPE to user input
loop while TYPE not valid
    display invalid input
    set TYPE to input
display results of calling function calculate on TYPE and NUMS
'''

#define function calculate, get NUMBERS
def calculate(*nm):
#    set OPERATION to first in NUMBERS and NUMBERS to second in NUMBERS
    op=nm[0]
    nm=nm[1]
#    if OPERATION is sum return NUMBERS added together
    if op == 'sum':
        return sum(nm)
#    else if OPERATION is average return NUMBERS added together, divided by number of NUMBERS
    elif op == 'average':
        return sum(nm)/len(nm)
#    else if OPERATION is max return largest number in NUMBERS
    elif op=='max':
        return max(nm)
#    else if OPERATION is min return smallest number in NUMBERS
    elif op=='min':
        return min(nm)
#    else if OPERATION is product return NUMBERS multiplied together
    elif op=='product':
        pdct=1
        for i in nm:
            pdct*=i
        return pdct

#define function check, get INPUT
def check(vlu):
#    try to make INPUT a float and return it, if error, return False
    try:
        return float(vlu)
    except:
        return False

#display enter numbers, done to stop entering numbers
print('Enter numbers, or "done" to stop entering numbers.')
#set NUMS to empty list and INPUT to user input
nms=[]
inpt=input('Number: ')
#loop while INPUT not done:
while inpt.lower() != 'done':
#    if function check passed INPUT is not false, add INPUT to NUMS, else display invalid input
    if check(inpt):
        nms.append(check(inpt))
    else:
        print('Invalid input. Try again.')
#    set INPUT to user input
    inpt=input('Number: ')

#display operation options
print('Possible operations: sum, average, max, min, product.')
#set TYPE to user input
typ=input('What operation would you like to preform? ').lower()
#loop while TYPE not valid
while typ not in ['sum','average','max','min','product']:
#    display invalid input
    print('Invalid operation. Try again.')
#    set TYPE to input
    typ=input('What operation would you like to preform? ').lower()

#display results of calling function calculate on TYPE and NUMS
print(f'The result is: {calculate(typ, [x for x in nms])}')
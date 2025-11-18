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
    set TYPE to input2
display results of calling function calculate on TYPE and NUMS(but seperated)
'''

#define function calculate, get OPERATION and NUMBERS
def calculate(*nm):
#    set OPERATION to first in NUMBERS and NUMBERS to second in NUMBERS
    op=nm[0]
    nm=nm[1]
#    if OPERATION is sum return NUMBERS added together
    if op == 'sum':
        return sum(nm)

    elif op == 'average':
        return sum(nm)/len(nm)

    elif op=='max':
        return max(nm)

    elif op=='min':
        return min(nm)

    elif op=='product':
        pdct=1
        for i in nm:
            pdct*=i
        return pdct


def check(vlu):

    try:
        return float(vlu)
    except:
        return False


print('Enter numbers, or "done" to stop entering numbers.')

nms=[]
inpt=input('Number: ')

while inpt.lower() != 'done':

    if check(inpt):
        nms.append(check(inpt))
    else:
        print('Invalid input. Try again.')

    inpt=input('Number: ')

print('Possible operations: sum, average, max, min, product.')

typ=input('What operation would you like to preform? ').lower()

while typ not in ['sum','average','max','min','product']:

    print('Invalid operation. Try again.')

    typ=input('What operation would you like to preform? ').lower()


print(f'The result is: {calculate(typ, [x for x in nms])}')
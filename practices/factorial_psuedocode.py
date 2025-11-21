#LM 2nd Factorial Psuedocode

#                                                                                    Any modifications I made appear as lines below this
#define function factorial calcualator
def factorialCalc():
#print: Hello welcome to the factorial calculator
    print('Hello welcome to the factorial calculator')
#input: enter the number you want to be a factorial
    user=input('enter the number you want to be a factorial')
#loop(to check and make sure they enter something valid)
    while True:
#if input is equal to integer(using try-except)
        try:
            user=int(user)
            #break loop and move on
            break
        except:
            #else: print invalid character try again
            print('Invalid character try again.')
            #had to add next line to prevent infinite loop if wrong input                         ----------------
            user=input('enter the number you want to be a factorial')
#continue and loop
            continue
#for loop to loop over the numbers in range of the user input iclusive, of 1,5 when is 0,4
    dn=1#had to add to make my logic work                                                         -------------
    for i in list(map(lambda x: x+1, range(user))):
#multiply the numbers in the user
        dn*=i# could not understand so useed my own logic                                        -----------------
#inputleading up to the user number
    input('Leading up to user number')
#print: the original number and then the multiplied munber
    print(f'{user}! = {dn}')#modified formatting                                                  --------------
#run factorial calculator
factorialCalc()
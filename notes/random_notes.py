#LM 2nd RANDOM NUMBERS NOTES

#produces numbers close to one, closer if run is larger. runs nearly instantly if run=1000000 takes 2 minutes to run if run = 1000000000
number=0
import random
run=1000000000
for i in range(run):
    x=random.random()
    number += x
print(number*2/run)
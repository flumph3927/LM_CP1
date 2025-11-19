#LM 2nd Mapping
import random

'''number=[54,64,7,54,3,64,44,36,65,66,5,36,68]

def divide(it):
    return it/2

div=list(map(divide, number))

for i, num in enumerate(number):
    print(f'{num}/2={div[i]}')'''


list=[]
for i in range(40):
    list.append([])
    list[i].append(random.randint(0,1))
    list[i]=tuple(list[i])
print(tuple(list))
print(tuple(map(lambda lst: tuple(map(lambda num: 1 if num == 0 else 0, lst)), list)))
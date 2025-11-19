#LM 2nd Squared Numbers

#loop through number list using index and value, every iteration print the value and then the index of a squaring function run on every item in the list
for i,v in enumerate([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]): print(f'{v} squared is {list(map(lambda num: num*num, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]))[i]}')
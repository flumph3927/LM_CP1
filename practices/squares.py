#LM 2nd Squared Numbers

#loop through number list using index and value, every iteration print the value and then the index of a squaring function run on every item in the list
for i,v in enumerate([3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]): print(f'{v} squared is {list(map(lambda num: num*num, [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]))[i]}')
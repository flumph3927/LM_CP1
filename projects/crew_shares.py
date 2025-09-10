#LM 2nd Crew Shares

money=float(input('How much was earned? ')) #gets inputs for earnings and crew
crew=int(input('How many crew is there, excluding the captian and first mate? '))

share=money/(10+crew) #calculates share value(rounds later)

print(f'The captain gets ${round((share*7),2):,}\nThe first mate gets ${round((share*3),2):,}\nEach memebr of the crew gets an additional ${round(share,2)-500:,}') #computes the amount of money per person and outputs it in the proper format.
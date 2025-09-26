#LM 2nd Fix the Game
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: ")) #Logic error, input was not int format, which created problems when comparing using > or <, as string and number cannot be compared using those. Added int() around the input.
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess >100 or guess <1: #Logic Error. The user could guess outside of the range. I added this elif to check. (Note: attempts-=1 makes the guess not count.)
            print("Your guess is not within the possible range and will not be counted. Try again.")
            attempts-=1
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        attempts+=1 #Logic Error. Number of guesses was not increasing, so the user could guess infinitely. Added this peice of code.
    print("Game Over. Thanks for playing!")#Logic Error. removed continue, because it was unnecessary code.
start_game()
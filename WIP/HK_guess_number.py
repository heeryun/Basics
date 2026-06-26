import random
# Here's your first challenge!
# Make a game that generates a random number from 0 - 10
# Make the user guess the number, and give a response depending on whether they are right or wrong

# Challenge 1: Make the program say higher or lower based on the guess accurately
# Challenge 2: Limit the number of guesses that the player gets

number = random.randint(1,10)
count_guess = 0
guess_threshold = 5

print(f"Guess what number I'm thinking of from 1-10. You have {guess_threshold} guesses!")
while count_guess < guess_threshold:
    guess = input("Guess the Number: ") # Captures user typing (always reads as a string)
    count_guess += 1
    if int(guess) == number:
        print(f'Congrats! {number} was the number I was thinking of!')
        break
    elif int(guess) < number:
        print(f'Higher!')
    elif int(guess) > number:
        print(f'Lower!')
    #else:
    #    print(f'Oops, try again!')
    #    print(f'This is guess number {count_guess}')
if count_guess == guess_threshold:
    print(f"Too bad, you've run out of luck!")
    print(f"The number I was thinking of was {number}!")



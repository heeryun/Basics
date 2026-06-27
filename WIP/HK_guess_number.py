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
    try:
        guess = int(guess)
    except ValueError:
        # This block runs ONLY if the conversion fails
        print("This is NOT a valid input.")
        continue
    count_guess += 1
    if guess == number:
        print(f'Congrats! {number} was the number I was thinking of!')
        print(f'You got it in {count_guess} guesses!')
        break

    elif count_guess == guess_threshold:
        print(f"Too bad, you've run out of luck!")
        print(f"The number I was thinking of was {number}!")

    elif guess < number:
        print(f'Higher!')
        print(f'You have {guess_threshold - count_guess} guesses left!')
    elif guess > number:
        print(f'Lower!')
        print(f'You have {guess_threshold - count_guess} guesses left!')
    



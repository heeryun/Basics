# Loops!
# kinda sounds like what it does, this is how you repeat code and not write it over and over again.
# there are two kinds of loops, 'for' loops and 'while' loops.
# here's an example of both

#for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits: # notice the colon commonly left out (typo)
    print(fruit)

# while loop
count = 0
while count < 3:
    print(count)
    count += 1 # adds one to the count every loop. can also do -= to subtract every loop

# if, elif (else if), and else statements:
# within a loop, you can use if, elif, and else statement

numbers = [10, 6, 4, 1, 3]
for number in numbers:
    if number > 4:
        print(f'{number} is big')
    elif number < 4:
        print(f'{number} is small')
    else:
        print(f'{number} is four!')

# other loop commands

for num in range(1, 10):
    if num == 3: # if the number is equal to (==). Not equal to is (!=)
        continue  # Skips 3
    if num == 6:
        break     # Stops the loop entirely at 6
    print(num)

# you can also put loops inside of loops!

for fruit in fruits:
    for letter in fruit:
        print(letter)

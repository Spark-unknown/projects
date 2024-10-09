import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Number of lives
lives = 6

# Clues
clues = [
    "The number is an even number",
    "The number is greater than 50",
    "The number is a multiple of 4",
    "The number is less than 75",
    "The number is a multiple of 3"
]

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

while lives > 0:
    # Ask the user to guess a number
    guess = int(input("Guess a number: "))

    # Check if the guess is correct
    if guess == number_to_guess:
        print("Correct! You won!")
        break
    elif guess < number_to_guess:
        print("Higher!")
    else:
        print("Lower!")

    # Give a clue
    if lives == 5:
        print(clues[0])
    elif lives == 4:
        print(clues[1])
    elif lives == 3:
        print(clues[2])
    elif lives == 2:
        print(clues[3])
    elif lives == 1:
        print(clues[4])

    # Decrease lives by 1
    lives -= 1
    print(f"Lives remaining: {lives}")

# If lives run out, game over
if lives == 0:
    print(f"Game over! The number was {number_to_guess}")
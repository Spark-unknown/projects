import random

# List of words to guess with their clues
words_with_clues = {
    "apple": [
        "A type of fruit",
        "Often red or green",
        "Grows on trees",
        "Popular in pies",
        "Has a core"
    ],
    "banana": [
        "A yellow curved fruit",
        "Grows in tropical climates",
        "High in potassium",
        "Often eaten for breakfast",
        "Comes in a peel"
    ],
    "cherry": [
        "A small round stone fruit",
        "Often red or purple",
        "Grows on bushes",
        "Popular in pies and smoothies",
        "Has a pit"
    ],
    "date": [
        "A sweet brown fruit",
        "Grows on palm trees",
        "Often eaten dried",
        "Popular in Middle Eastern cuisine",
        "High in sugar"
    ],
    "elderberry": [
        "A type of berry used in jams and wines",
        "Grows on shrubs",
        "Often used in medicine",
        "Popular in European cuisine",
        "Has a distinctive taste"
    ],
    "mango": [
        "A sweet and juicy fruit",
        "Grows on trees in tropical climates",
        "Often eaten fresh or used in smoothies",
        "Popular in Indian and Mexican cuisine",
        "Has a pit"
    ],
    "orange": [
        "A round and juicy fruit",
        "Grows on trees in warm climates",
        "Often eaten fresh or squeezed for juice",
        "Popular in breakfast and snacks",
        "Has a peel"
    ],
    "grape": [
        "A small round fruit",
        "Grows in clusters on vines",
        "Often eaten fresh or used in wine",
        "Popular in snacks and desserts",
        "Has seeds"
    ],
    "watermelon": [
        "A refreshing and sweet fruit",
        "Grows on vines in warm climates",
        "Often eaten fresh or used in salads",
        "Popular in summer and picnics",
        "Has a rind"
    ]
}

# Choose a random word and its clues
word, clues = random.choice(list(words_with_clues.items()))

# Create a list to store the guessed letters
guessed_letters = ["_"] * len(word)

# Number of lives
lives = 6

# Current clue index
clue_index = 0

print("Welcome to Hangman!")
print("Word to Guess:", " ".join(guessed_letters))
print("Lives:", lives)
print("Clue:", clues[clue_index])

while lives > 0:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the letter is in the word
    if guess in word:
        # Reveal the letter in the word
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_letters[i] = guess
    else:
        # Decrease lives by 1
        lives -= 1
        print(f"Incorrect! You have {lives} lives left.")
        # Show the next clue
        clue_index += 1
        if clue_index < len(clues):
            print("Clue:", clues[clue_index])
        else:
            print("No more clues!")

    # Print the updated word
    print("Word to Guess:", " ".join(guessed_letters))
    print("Lives:", lives)

    # Check if the word is fully guessed
    if "_" not in guessed_letters:
        print("Congratulations! You won!")
        break

# If lives run out, game over
if lives == 0:
    print("Game over! The word was " + word)
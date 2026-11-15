
import random

words = ["python", "engineering", "computer", "soccer", "college", "programming", "Hangman", "university"]

word = random.choice(words)

guessed_letters = []

incorrect_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses > 0:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses remaining:", incorrect_guesses)

    if "_" not in display_word:
        print("\nCongratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Incorrect guess!")
        incorrect_guesses -= 1

else:
    print("\nYou lost!")
    print("The word was:", word)


# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  TYLER BAKER
#.       DANIEL BROWN
#        WILLIAM SCHOENNBERGER
#        NOAH DOUGHERTY
# Section: 571
# Assignment: Lab 9 team
# Date: 20 October 2026
#

# Return letters with no repeats
def get_valid_letters(a):
    valid_letters = ""
    for letter in a:
        if letter.isalpha() and letter not in valid_letters:
            valid_letters += letter
    return valid_letters
# Checks for validity of input
def is_valid_guess(a, b):
    if len(b) != 10 or len(set(b)) != 10:
        return False
    for letter in b:
        if letter not in a:
            return False
    return True
# Checks for symmetry
def check_user_guess(a, b, c, d):
    return a == b * c + d
# Turns characters into num equivalents
def make_number(a, b):
    int_equiv = 0
    for letter in a:
        int_equiv = int_equiv * 10 + b.index(letter)
    return int_equiv
# Uses make_number to turn all parts of puzzle into nums
def make_numbers(a, b):
    puzzle_parts = a.split(",")
    dividend = make_number(puzzle_parts[1].split("|")[1].strip(), b)
    quotient = make_number(puzzle_parts[0].strip(), b)
    divisor = make_number(puzzle_parts[1].split("|")[0].strip(), b)
    remainder = make_number(puzzle_parts[-1].strip(), b)
    return dividend, quotient, divisor, remainder
# Prints out the puzzle
def print_puzzle(puzzle):
    """ Print puzzle as a long division problem. """
    puzzle = puzzle.split(",")
    for i in range(len(puzzle)):
        if i == 1:
            print(f"{len(puzzle[i].split('|')[1]) * '_': >16}")
        print(f"{puzzle[i]: >16}")
        if i > 1 and i % 2 == 0:
            print(f"{'-' * len(puzzle[i]): >16}")
# Main runloop
def main():
    puzzle = input("Enter a word arithmetic puzzle: ")
    print()
    print_puzzle(puzzle)
    valid_letters = get_valid_letters(puzzle)
    guess = input("\nEnter your guess, for example ABCDEFGHIJ: ")

    if not is_valid_guess(valid_letters, guess):
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
        return

    numbers = make_numbers(puzzle, guess)
    if check_user_guess(numbers[0], numbers[1], numbers[2], numbers[3]):
        print("Good job!")
    else:
        print("Try again!")

if __name__ == "__main__":
    main()

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  TYLER BAKER
#.       DANIEL BROWN
#        WILLIAM SCHOENNBERGER
#        NOAH DOUGHERTY
# Section: 571
# Assignment: Lab 7 team
# Date: 5 October 2026
#

board_dict = {}
rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
white_turn = False
for x in range(81):
    board_dict[f"{rows[x//9]}{(x%9)+1}"] = '.'
def print_board():
    counter = 0
    for x in board_dict.keys():
        counter += 1
        if counter % 9 != 0:
            print(board_dict[x], end="")
        else:
            print(board_dict[x], end="\n")

while True:
    print_board()
    if not white_turn:
        placement = input("It is black's turn. Please enter your selection as a letter\nfor the row and number for the column such as 'A1'\nfor the first place\n").upper()
        try:
            if board_dict[placement] == '.':
                board_dict[placement] = chr(9679)
                white_turn = True
        except KeyError:
            pass
    else:
        placement = input("It is white's turn. Please enter your selection as a letter\nfor the row and number for the column such as 'A1'\nfor the first place\n").upper()
        try:
            if board_dict[placement] == '.':
                board_dict[placement] = chr(9675)
                white_turn = False
        except KeyError:
            pass
    if placement == "STOP":
        break

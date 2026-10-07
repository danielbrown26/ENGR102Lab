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

rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
board = []
for _ in range(9):
    row = []
    for _ in range(9):
        row.append(".")
    board.append(row)
white_turn = False

def print_board():
    for row in board:
        print("".join(row))

while True:
    print_board()
    if not white_turn:
        placement = input("It is black's turn. Please enter your selection as a letter\nfor the row and number for the column such as 'A1'\nfor the first place\n").upper()
    else:
        placement = input("It is white's turn. Please enter your selection as a letter\nfor the row and number for the column such as 'A1'\nfor the first place\n").upper()

    if len(placement) == 2 and placement[0] in rows and placement[1] in "123456789":
        row_index = rows.index(placement[0])
        column_index = int(placement[1]) - 1
        if board[row_index][column_index] == ".":
            if white_turn:
                board[row_index][column_index] = chr(9675)
            else:
                board[row_index][column_index] = chr(9679)
            white_turn = not white_turn

    if placement == "STOP":
        break

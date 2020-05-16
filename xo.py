import os
import time
import random

board =
[
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
]
def print_board():
    print (" "+board[0]+" | "+board[1]+" | "+board[2]+" ")
    print ("---|---|---")
    print (" "+board[3]+" | "+board[4]+" | "+board[5]+" ")
    print ("---|---|---")
    print (" "+board[6]+" | "+board[7]+" | "+board[8]+" ")

while True:
    os.system("clear")
    print_board()

    choice = input("\nTIC TAC TOE: write the numbre you want to replace it with x.\n")
    choice = int(choice)-1

    if board[choice] != "x" and board[choice] != "o":
        board[choice] = "x"
    else:
        print("Sorry, that space is not empty")
        time.sleep(1)

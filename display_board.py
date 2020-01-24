# 1
from IPython.display import clear_output


def display_board(board):
    clear_output()  # Remember, this only works in jupyter!

    #print(' ' + board[12] + ' | ' + board[11] + ' | ' + board[10])
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


board = ['#','X','O','X','O','X','O','X','O','X']
#board = [' ']*10   #empty board ex
display_board(board)
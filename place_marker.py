# 1
from IPython.display import clear_output


def display_board(board):
    clear_output()  # Remember, this only works in jupyter!

    #print(' ' + board[12] + ' | ' + board[11] + ' | ' + board[10])
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


#board = ['#','X','O','X','O','X','O','X','O','X']
#board = [' ']*10   #empty board ex
#display_board(board)

# 2
def player_input():
    marker = ''

    while not (marker == 'X' or marker == '0'):
        marker = input('Player 1: Do you want to be X or 0? ').upper()

    if marker == 'X':
        return ('IKS', 'NOL')
    else:
        return ('NOL', 'IKS')
theBoard = [' '] * 10
print(player_input())

def place_marker(board, marker, position):
    board[position] = marker

marker = "$"
#place_marker(board,marker,2)
#place_marker(board,marker,5)
place_marker(theboard,marker,8)
#display_board(board)

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

display_board(theBoard)
print(win_check(theBoard,'X'))

import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

turn = choose_first()
#while True:
#print(turn + ' will go first.')

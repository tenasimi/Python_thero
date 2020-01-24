# 1
import random
from IPython.display import clear_output


def display_board(board):  #board is a list with indexes
    clear_output()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


board=["#","X","O","X","O","X","O","X","O","X"]
# 2
def player_input():
    marker = ''
    while not (marker == 'X' or marker == '0'):
        marker = input('Player 1: Do you want to be X or 0? ').upper()
    if marker == 'X':
        return ('X', '0')
    else:
        return ('0', 'X')
    # 3


def place_marker(board, marker, position):
    board[position] = marker



# 4
def win_check(board, mark):
    return (
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark)
            or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark)
            or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark)
    )
#print(place_marker(board,'$',6))
#display_board(board)
#print(win_check(board, "O"))
#print(win_check(board, "O"))
# 5
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# 6
def space_check(board, position):
    return board[position] == ' '        #for itself going a boolean - reurn used


# print(space_check(board, 7))
# 7                                 proverka na nalicie pustogo mesta + #6 dlya proverki Nicyi
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# 8
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


# 9
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


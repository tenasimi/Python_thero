#Step 1: Write a function that can print out a board. Set up your board as a list,
# where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.

def display_board(board):
    print('\n' * 100)
    print('   |   |')
    print(' ' + board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
#display_board(test_board)
#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
# Think about using while loops to continually ask until you get a correct answer.
def player_input():

    '''
    Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
    Think about using while loops to continually ask until you get a correct answer.
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    #print(player_input.__doc__)
    marker = ''
    # keep asking player 1 to choose x or 0

    while marker != 'X' and marker != '0':
        marker = input('Player 1, choose X or 0: ').upper()  #balaca x olsa qebul etsin

    # assign player 2 , the opposite marker
    player1 = marker

    if player1 == 'X':
        player2 = '0'
    else:
        player2 = 'X'

    return (player1, player2)

#player_input()
print(player_input())

player1_marker, player2_marker = player_input()

print(player1_marker)
print(player2_marker)

#Step 3: Write a function that takes in the board list object,
# a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker

place_marker(test_board,'$',9)
display_board(test_board)
#help(player_input())

# Step 4: Write a function that takes in a board and checks to see if someone has won. (all marks are same -x or y)
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


display_board(test_board)
print(win_check(test_board,'X'))

# Step 5 .write a func that use the random module to randomly decide which player goes first

import random

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return  'Player 2'

print(choose_first())

#Step 6: proveryaem nalicie pustogo mesta v boarde
def space_check(board, position):
    return board[position] == ' '

#print(space_check(board=test_board,position=9))

#Step 7: func that checks if the board is full
def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
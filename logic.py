
# 10
from win_check import *

print('Welcome to Tic Tac Toe!')

while True:

    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()                                         #var turn = func, i output string verir Player1 ili 2
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')  #adi variable
    if play_game.lower()[0] == 'y':
        game_on = True                                    # sozdali variable
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':                                                 #----------------if___for Player 1
            #show the board
            display_board(theBoard)
            #choose a position
            position = player_choice(theBoard)
            #place the marker on the position
            place_marker(theBoard, player1_marker, position)
                      #check if they wor
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!','Player 1 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!','Nicya, nikto ne viiqral')
                    break #ili game_on = False
                else:
                    turn = 'Player 2'

        else:                                                             #-----------------else /for Player 2
            # Player2's turn.  toje samoe cto i dlya 1-qo
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!','Nicya, nikto ne viiqral')
                    break  #ili game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
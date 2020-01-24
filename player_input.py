# 2
def player_input():
    marker = ''

    while not (marker == 'X' or marker == '0'):
        marker = input('Player 1: Do you want to be X or 0? ').upper()

    if marker == 'X':
        return ('X', '0')
    else:
        return ('0', 'X')

print(player_input())
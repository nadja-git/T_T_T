#Step 1: Write a function that can print out a board.
# Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, 
# so you get a 3 by 3 board representation.

def display_board(board):
    
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
# Think about using while loops to continually ask until you get a correct answer.
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'),
#  and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position] = marker

#Step 4: Write a function that takes in a board and checks to see if someone has won.
ef win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

#Step 1: Write a function that can print out a board.
# Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, 
# so you get a 3 by 3 board representation.
pass







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








#Step 4: Write a function that takes in a board and checks to see if someone has won.


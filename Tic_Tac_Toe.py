#Step 1: Write a function that can print out a board.
# Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, 
# so you get a 3 by 3 board representation.


#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
# Think about using while loops to continually ask until you get a correct answer.


#Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'),
#  and a desired position (number 1-9) and assigns it to the board.


#Step 4: Write a function that takes in a board and checks to see if someone has won.
def win_check(board, mark): 

    check_result = False 

    if mark == board[1] == board[2] == board[3]: 

        check_result = True 

    elif mark == board[4] == board[5] == board[6]: 

        check_result = True 

    elif mark == board[7] == board[8] == board[9]: 

        check_result = True 

    elif mark == board[1] == board[4] == board[7]: 

        check_result = True 

    elif mark == board[2] == board[5] == board[8]: 

        check_result = True 

    elif mark == board[3] == board[6] == board[9]: 

        check_result = True     

    elif mark == board[1] == board[5] == board[9]: 

        check_result = True 

    elif mark == board[3] == board[5] == board[7]: 

        check_result = True 

    return check_result 

#5  Function to choose who plays first (MOHAMMED) 

import random 

def choose_first(): 

    if random.randint(1,2) == 1: 

        return 'Player 1' 

    else: 

        return 'Player 2' 

#Step 5: Write a function that uses the random module to randomly decide which player goes first.
#  You may want to lookup random.randint() Return a string of which player went first.


#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.


#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.



#Step 8: Write a function that asks for a player's next position (as a number 1-9)
#  and then uses the function from step 6 to check if its a free position.
#  If it is, then return the position for later use.


#Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.

#Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
#Game Logic
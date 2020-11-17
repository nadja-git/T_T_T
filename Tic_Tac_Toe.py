# T_T_T
# this is function to check if board is full
def full_board_check(board): 
    count = 0 
    for i in range (1,10): 
        if board[i] == ' ': 
            count += 1 
    if count == 0: 
        return True 
    else: 
        return False 
def player_choice(board): 
    ref = False 
    while ref == False: 
        pos = int(input("Choose your cell (between 1-9): ")) 
        if pos<1 and pos>9: 
            print('Number out of range') 
            continue 
        if space_check(board, pos): 
            ref = True 
            return pos 
        else: 
            print('The cell is already filled! Choose another one') 
# Function to replay the game 

def replay(): 

    reply = input("Do you want to play again? (Y or N): ").upper() 

    return reply == 'Y' 
#added a new comment
#Now in Nadja_Branch
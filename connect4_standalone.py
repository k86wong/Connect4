#Memo
#Player 1 is 1's. Player 2 is 2's. Empty slots are 0's.

def main():
    #Initialize win condition.
    win = 0 
    while win == 0:
        #player 1 starts the game.
        player_turn = 1

        #initialize board state
        board_state = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

        #ask for a col number to put the token into
        col_number = input(f'It is now player {player_turn}''s turn. Which column do you want to put your token into?')

        #add the token to the board
        board_state = add_token(player_turn, col_number, board_state)
        #check if anyone has won
        win = check_win(board_state)

        #print board state
        for array in board_state:
            print array

        if player_turn == 1:
            player_turn = 2
        elif player_turn == 2:
            player_turn = 1
    
    if win == 1:
        print('Congrats! Player 1 has won.')
    else:
        print('Congrats! Player 2 has won.')

    return 3


def add_token(player_turn, col_number, board_state):
    if player_turn == 1:
        for i in range(5:-1:-1):
            if board_state[i][col_number] == 0:
                board_state[i][col_number] == 1
                break
    else:
        for i in range(5:-1:-1):
            if board_state[i][col_number] == 0:
                board_state[i][col_number] == 2
                break
    return board_state

def check_win(board_state):
    #return 0 if no one has won, return 1 if player 1 has won, return 2 if player 2 has won.
    # check vertical win condition
    ones_inarow = 0
    twos_inarow = 0
    board_width = 7
    board_height = 6

    for i in range(board_width):
        ones_inarow = 0
        twos_inarow = 0
        for j in range(board_height):
            if board_state[j][i] == 1:
                ones_inarow = ones_inarow + 1
                if ones_inarow == 4:
                    return 1
            elif board_state[j][i] == 2:
                twos_inarow = twos_inarow + 1
                if twos_inarow == 4:
                    return 2
            else:
                ones_inarow = 0
                twos_inarow = 0

    # check horizontal win condition
    ones_inarow = 0
    twos_inarow = 0
    for array in board_state:
        ones_inarow = 0
        twos_inarow = 0    
        for i in range(len(array)):
            if array(i) == 1:
                ones_inarow = ones_inarow + 1
                if ones_inarow == 4:
                    return 1
            elif array(i) == 2:
                twos_inarow = twos_inarow + 1
                if twos_inarow == 4:
                    return 2
            else:
                ones_inarow = 0
                twos_inarow = 0
    # check diagonal win condition "\". Use try - except to get through indexing errors. 
    ones_inarow = 0
    twos_inarow = 0
    for i in range(board_height):
        for j in range(board_width):
            try:
                if (board_state[i][j] == 1) and (board_state[i+1][j+1]) == 1 and (board_state[i+2][j+2] == 1) and (board_state[i+3][j+3] == 1):
                    return 1
                if (board_state[i][j] == 2) and (board_state[i+1][j+1] == 2) and (board_state[i+2][j+2] == 2) and (board_state[i+3][j+3] == 2):
                    return 2
            except IndexError:
                break

    # check diagonal win condition "/". Use try - except to get through indexing errors. 
    ones_inarow = 0
    twos_inarow = 0
    for i in range(board_height):
        for j in range(board_width):
            try:
                if (board_state[i][j] == 1) and (board_state[i+1][j-1]) == 1 and (board_state[i+2][j-2] == 1) and (board_state[i+3][j-3] == 1):
                    return 1
                if (board_state[i][j] == 2) and (board_state[i+1][j-1] == 2) and (board_state[i+2][j-2] == 2) and (board_state[i+3][j-3] == 2):
                    return 2
            except IndexError:
                break


if __name__ == '__main__':
    main()


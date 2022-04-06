#Memo
#Player 1 is 1's. Player 2 is 2's. Empty slots are 0's.

def main():
    #welcome message
    print('Thanks for playing connect4! Player 1 will be the O\'s and player 2 will be the X\'s. Player 1 will go first!')

    #Initialize win condition.
    win = 0 
    #player 1 starts the game.
    player_turn = 1
    #initialize board state
    board_state = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    #print initial board state
    print('\n col 0  1  2  3  4  5  6')
    for array in board_state:
        array_copy = array.copy()
        for i in range(len(array_copy)):
            if array_copy[i] == 0:
                array_copy[i] = '-'
            elif array_copy[i] == 1:
                array_copy[i] = 'O'
            else:
                array_copy[i] = 'X'
        print('     ', end='')
        print(*array_copy, sep='  ')


    while win == 0:
        #ask for a col number to put the token into
        while True:
            try:
                col_number = int(input(f'\nIt is now player {player_turn}\'s turn. Which column do you want to put your token into? '))
                assert 0 <= col_number <= 6
                #add the token to the board
                board_state = add_token(player_turn, col_number, board_state)
            except ValueError:
                print("Not an integer! Please enter an integer between 0 and 6.")
            except AssertionError:
                print("Please enter an integer between 0 and 6.")
            except TypeError:
                print("No more tokens can be put into this column!")
            else:
                break
        
        #check if anyone has won
        win = check_win(board_state)

        #print board state
        print('\n col 0  1  2  3  4  5  6')
        for array in board_state:
            array_copy = array.copy()
            for i in range(len(array_copy)):
                if array_copy[i] == 0:
                    array_copy[i] = '-'
                elif array_copy[i] == 1:
                    array_copy[i] = 'O'
                else:
                    array_copy[i] = 'X'
            print('     ', end='')
            print(*array_copy, sep='  ')

        if player_turn == 1:
            player_turn = 2
        elif player_turn == 2:
            player_turn = 1
    
    if win == 1:
        print('Congrats! Player 1 has won.')
    elif win == 2:
        print('Congrats! Player 2 has won.')

    return 3


def add_token(player_turn, col_number, board_state):
    if player_turn == 1:
        for i in range(5,-1,-1):
            if board_state[i][col_number] == 0:
                board_state[i][col_number] = 1
                return board_state
        raise TypeError
    else:
        for i in range(5,-1,-1):
            if board_state[i][col_number] == 0:
                board_state[i][col_number] = 2
                return board_state
        raise TypeError
        

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
                twos_inarow = 0
                if ones_inarow == 4:
                    return 1
            elif board_state[j][i] == 2:
                twos_inarow = twos_inarow + 1
                ones_inarow = 0
                if twos_inarow == 4:
                    return 2
            elif board_state[j][i] == 0:
                ones_inarow = 0
                twos_inarow = 0

    # check horizontal win condition
    ones_inarow = 0
    twos_inarow = 0
    for array in board_state:
        ones_inarow = 0
        twos_inarow = 0    
        for i in range(len(array)):
            if array[i] == 1:
                ones_inarow = ones_inarow + 1
                twos_inarow = 0
                if ones_inarow == 4:
                    return 1
            elif array[i] == 2:
                twos_inarow = twos_inarow + 1
                ones_inarow = 0
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
    #if no win conditions are found, return 0
    return 0


if __name__ == '__main__':
    main()


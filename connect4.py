import numpy as np

def play(player_turn, row_number, board_state):
    #add the token to the board
    add_token(player_turn, row_number, board_state)
    #check if anyone has won
    check_win(board_state)

    return board_state, win


def add_token(player_turn, row_number, board_state):
    if player_turn == 1:
        for i in range(5:0:-1):
            if board_state[i][row_number] == '-':
                board_state[i][row_number] == 'o'
                break
    else:
        for i in range(5:0:-1):
            if board_state[i][row_number] == '-':
                board_state[i][row_number] == 'x'
                break
    return board_state

def check_win(board_state):
    

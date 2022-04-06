#nested_array = [[1,2,3],[4,5,6]]
# nested_array = [1,2,3]
# print(len(nested_array))



#     for j in range(board_width - 3):        
#         ones_inarow = 0
#         twos_inarow = 0 
#         for a in [1, 2, 3]: 
#             for i in range(board_height - 3):
#                 if board_state[i][j] == 1:
#                     ones_inarow == ones_inarow + 1


# def add_token(player_turn, col_number, board_state):
#     if player_turn == 1:
#         for i in range(5,-1,-1):
#             if board_state[i][col_number] == 0:
#                 board_state[i][col_number] == 1
#                 return board_state
#     else:
#         for i in range(5,-1,-1):
#             if board_state[i][col_number] == 0:
#                 board_state[i][col_number] == 2
#                 return board_state


array = [1, 2, 0]
for i in range(len(array)):
    if array[i] == 0:
        array[i] = '-'
    elif array[i] == 1:
        array[i] = 'O'
    else:
        array[i] = 'X'

print(*array, sep=' ')

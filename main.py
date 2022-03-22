import random

game_running = False
win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
pos_dict = {1: ' ',
            2: ' ',
            3: ' ',
            4: ' ',
            5: ' ',
            6: ' ',
            7: ' ',
            8: ' ',
            9: ' '}


def new_table(players):
    global game_running
    game_running = True
    print(f'|{pos_dict[1]}|{pos_dict[2]}|{pos_dict[3]}|')
    print('-------')
    print(f'|{pos_dict[4]}|{pos_dict[5]}|{pos_dict[6]}|')
    print('-------')
    print(f'|{pos_dict[7]}|{pos_dict[8]}|{pos_dict[9]}|')
    if players == '1':
        single_player_game()
    elif players == '2':
        two_player_game()


def print_table():
    print(f'\n|{pos_dict[1]}|{pos_dict[2]}|{pos_dict[3]}|')
    print('-------')
    print(f'|{pos_dict[4]}|{pos_dict[5]}|{pos_dict[6]}|')
    print('-------')
    print(f'|{pos_dict[7]}|{pos_dict[8]}|{pos_dict[9]}|')


def computer_turn():
    global pos_dict, game_running
    if game_running:
        comp_pos = random.randint(1, 9)
        if pos_dict[comp_pos] == ' ':
            pos_dict[comp_pos] = 'O'
        else:
            try:
                computer_turn()
            except RecursionError:
                print('Tie game')
                game_running = False
        for combo in win_list:
            if pos_dict[combo[0]] == 'O' and \
                    pos_dict[combo[0]] == pos_dict[combo[1]] and \
                    pos_dict[combo[0]] == pos_dict[combo[2]]:
                print('You lose')
                game_running = False


def single_player_game():
    global pos_dict, game_running
    while game_running:
        user_input = int(input('Select a position to place an X (1-9)\n'))
        if pos_dict[user_input] == ' ':
            pos_dict[user_input] = 'X'
        else:
            print('Pos unavailable please try again')
            single_player_game()
        for combo in win_list:
            if pos_dict[combo[0]] == 'X' and \
                    pos_dict[combo[0]] == pos_dict[combo[1]] and \
                    pos_dict[combo[0]] == pos_dict[combo[2]]:
                print('You win')
                print_table()
                game_running = False
        if game_running:
            computer_turn()
            print_table()


def player_turn(player_move, symbol):
    global game_running
    if pos_dict[player_move] == ' ':
        pos_dict[player_move] = symbol
    else:
        print('Space occupied. Try again.')
        if symbol == 'X':
            player_num = 1
        else:
            player_num = 2
        player_move = int(input(f'Player {player_num}:\nSelect a position to place an X (1-9)\n'))
        player_turn(player_move, symbol)
    for combo in win_list:
        if pos_dict[combo[0]] == 'X' and \
                pos_dict[combo[0]] == pos_dict[combo[1]] and \
                pos_dict[combo[0]] == pos_dict[combo[2]]:
            print('Player 1 wins!')
            print_table()
            game_running = False
        elif pos_dict[combo[0]] == 'O' and\
                pos_dict[combo[0]] == pos_dict[combo[1]] and\
                pos_dict[combo[0]] == pos_dict[combo[2]]:
            print('Player 2 wins!')
            print_table()
            game_running = False


def two_player_game():
    while game_running:
        player1_pos = int(input('Player 1:\nSelect a position to place an X (1-9)\n'))
        player_turn(player1_pos, 'X')
        print_table()
        if game_running:
            player2_pos = int(input('Player 2:\nSelect a position to place an O (1-9)\n'))
            player_turn(player2_pos, 'O')
            print_table()


player_option = input('Press 1 for single player mode or 2 for two player mode.\n')
new_table(player_option)

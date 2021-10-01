import random

BOX_SIZE = 6
TOP_ROW = 0
EMPTY_SLOTH = "_"
USER_COIN = "X"
COMP_COIN = "W"
boxs = []

def create_box():
    for _ in range(BOX_SIZE):
        boxs.append([EMPTY_SLOTH, EMPTY_SLOTH, EMPTY_SLOTH, EMPTY_SLOTH, EMPTY_SLOTH, EMPTY_SLOTH])

def draw_box():
    print(f"   {'1':^5} {'2':^5} {'3':^5} {'4':^5} {'5':^5} {'6':^5}")
    for row in range(BOX_SIZE):
        print(f"{row+1} |  ", end="")
        for column in range(len(boxs[row])):
            print(f"{boxs[row][column]}  |  ", end="")
        print("") # for empty spaces
    print("="*39)

def insert_coin(select_column, coin):
    is_slot_empty = True
    current_row = BOX_SIZE - 1
    while is_slot_empty:
        if current_row < TOP_ROW:
            break
        for column in range(BOX_SIZE):
            if (column == select_column) and boxs[current_row][column] == EMPTY_SLOTH:
                boxs[current_row][column] = coin
                is_slot_empty = False
                break
        current_row += -1
    if not is_slot_empty:
        return True
    else:
        return False

###! search
def horizontal_search(coin):
    row = 0
    found = False
    while not found:
        if row > 5:
            break
        for column in range(len(boxs[row])-2):
            if boxs[row][column] is boxs[row][column+1] is boxs[row][column+2] == coin:
                print(f"{coin} was found on row {row+1} col {column+1}")
                found = True
                break
        row += 1
    return found

def vertical_search(coin):
    row = 0
    found = False
    while not found:
        if row > 3:
            break
        for column in range(0, len(boxs[row])):
            if boxs[row][column] is boxs[row+1][column] is boxs[row+2][column] == coin:
                print(f"{coin} was found on row {row+1} col {column+1}")
                found = True
                break
        row += 1
    return found

def cross_search_right(coin):
    row = 0
    found = False
    while not found:
        if row > 3:
            break
        for column in range(len(boxs[row])-2):
            if boxs[row][column] is boxs[row+1][column+1] is boxs[row+2][column+2] == coin:
                print(f"{coin} was found on row {row+1} col {column+1}")
                found = True
                break
        row += 1
    return found

def cross_search_left(coin):
    row = 0
    found = False
    while not found:
        if row > 3:
            break
        for column in range(2, len(boxs[row])):
            if boxs[row][column] is boxs[row+1][column-1] is boxs[row+2][column-2] == coin:
                print(f"{coin} was found on row {row+1} col {column+1}")
                found = True
                break
        row += 1
    return found
###!

def is_win(COIN):
    if horizontal_search(COIN) or vertical_search(COIN) or cross_search_right(COIN) or cross_search_left(COIN):
        return True
    else:
        return False

#! MAIN
create_box()
is_game_finished = False

while not is_game_finished:
    draw_box()
    correct_input = False
    while not correct_input:
        user_select = input(f"select column to drop (1-{BOX_SIZE}): ")
        try:
            if int(user_select) in range(BOX_SIZE+1) and insert_coin(int(user_select)-1, USER_COIN):
                break
            else:
                print(f"please choose column between 1-{BOX_SIZE}: ")
        except ValueError:
            print("please enter only number! ")
    print("\n")
    while True:
        bot_select = random.randint(0,5)
        if insert_coin(bot_select, COMP_COIN):
            break
    
    if is_win(USER_COIN):
        draw_box()
        print("You win !")
        is_game_finished = True
    elif is_win(COMP_COIN):
        draw_box()
        print("COMP WIN YOU LOSE !")
        is_game_finished = True

    if is_game_finished:
        play_again = input("Play Again? (Y/N) : ")
    else:
        play_again = 'n'
    
    if play_again.lower() == "y":
        is_game_finished = False
        boxs.clear()
        create_box()
        print("\n")
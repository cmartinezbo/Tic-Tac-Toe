import random

from termcolor import colored

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def game_figures():
    while True:
        user_1 = input("Which one do you want? X or O?: ").upper()

        if user_1 != "X" and user_1 != "O":
            print("Type a valid option!")
        else:
            break

    print("\nCOLORS:" + colored("\n> Red\n", "red")
          + colored("> Green\n", "green") + colored("> Yellow\n", "yellow") + colored("> Blue\n", "blue")
          + colored("> Magenta\n", "magenta") + colored("> Cyan\n", "cyan")
          + "> White")

    while True:
        color = input("\nPlayer 1, choose your color: ").lower()
        if is_valid_str(color):
            break
        else:
            print("Type a valid option!")

    while True:
        color_2 = input("Player 2, chose your color: ").lower()
        if is_valid_str(color_2):
            break
        else:
            print("Type a valid option!")

    user_2 = "O" if user_1 == "X" else "X"

    if color == "white":
        pass
    else:
        user_1 = colored(user_1, color)

    if color_2 == "white":
        pass
    else:
        user_2 = colored(user_2, color_2)

    return user_1, user_2


def who_start():
    num_user_1 = 0
    num_user_2 = 1
    random_number = random.randint(0, 1)
    if random_number == num_user_1:
        print("\nPlayer 1 starts!")
        num_user_1 = True
        num_user_2 = False
    else:
        print("\nPlayer 2 starts!")
        num_user_1 = False
        num_user_2 = True
    return num_user_1, num_user_2


def match_dev(player_figure, game_board):
    while True:
        place_num = input("Type a place to move: ")
        if is_valid_int(place_num):
            place_num = int(place_num)
            if is_valid_place(place_num):
                if game_board[place_num - 1] == " ":
                    game_board[place_num - 1] = player_figure
                    break
                else:
                    print("This place is currently filled!")
            else:
                print("Type a number between 1 - 9!")
        else:
            print("Type a number!")

    print("\n")
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])
    print("\n")


def print_board():
    print("\nPlaces:")
    print("1" + '|' + "2" + '|' + "3")
    print('-+-+-')
    print("4" + '|' + "5" + '|' + "6")
    print('-+-+-')
    print("7" + '|' + "8" + '|' + "9")
    print("\n")


def is_valid_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def is_valid_place(number):
    return True if 1 <= number <= 9 else False


def is_valid_str(string):
    try:
        int(string)
        return False
    except ValueError:
        return True


def winnings():
    if board[0] == board[1] == board[2] and board[0] and board[1] and board[2] != " ":
        print("WIN")
        return True
    elif board[3] == board[4] == board[5] and board[3] and board[4] and board[5] != " ":
        print("WIN")
        return True
    elif board[6] == board[7] == board[8] and board[6] and board[7] and board[8] != " ":
        print("WIN")
        return True
    elif board[0] == board[3] == board[6] and board[0] and board[3] and board[6] != " ":
        print("WIN")
        return True
    elif board[1] == board[4] == board[7] and board[1] and board[4] and board[7] != " ":
        print("WIN")
        return True
    elif board[2] == board[5] == board[8] and board[2] and board[5] and board[8] != " ":
        print("WIN")
        return True
    elif board[0] == board[4] == board[8] and board[0] and board[4] and board[8] != " ":
        print("WIN")
        return True
    elif board[2] == board[4] == board[6] and board[2] and board[4] and board[6] != " ":
        print("WIN")
        return True
    else:
        return False


def game():
    print_board()
    players = game_figures()
    positions = who_start()
    count = 0
    while True:
        if positions[0]:
            match_dev(players[0], board)
            count += 1
            if winnings() is True:
                break
            if count == 9 and winnings() is False:
                print("There's a tie!")
                break
            match_dev(players[1], board)
            count += 1
        else:
            match_dev(players[1], board)
            count += 1
            if winnings() is True:
                break
            if count == 9 and winnings() is False:
                print("There's a tie!")
                break
            match_dev(players[0], board)
            count += 1


print(colored("WELCOME TO ULTIMATE TIC-TAC-TOE\n{:^31}".format("made by Cristian\n"), "green"))
while True:
    game()
    repeat = input("Do you wanna exit? Yes/No: " + "\n").upper()
    if repeat == "Y" or repeat == "YES":
        print(colored("\nFollow @xtianmb on GitHub for more projects like this!", "yellow"))
        break
    elif repeat == "N" or repeat == "NO":
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    else:
        print("Type a valid option!")
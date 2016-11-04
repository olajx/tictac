
import random
import sys

player_character = None
computer_character = None


def welcome():
    print("\u001B[ 35m""Welcome to Tic-Tac-Toe game." "\u001B[0m")


def players():
    global player_character
    global computer_character

    player = input(
        "\u001B[ 33m" "Press 1 or 2 to choose single/multiplayer mode (or press any key to exit):""\u001B[0m")
    if player not in ["1", "2"]:
        sys.exit()
    player = int(player)

    player_character = input("\u001b[41m""Choose a character (X or O): ""\u001B[0m")
    while player_character.upper() not in ["X", "O"]:
        print("type X or O")
        player_character = input("Choose a character (X or O): ")

    player_character = player_character.upper()

    if player_character.upper() == "O":
        computer_character = "X"

    if player_character.upper() == "X":
        computer_character = "O"


# computer ellen

    if player == 1:
        show()
        game()

# kétjátékos mód

    if player == 2:
        show()
        multiGame()

    else:
        quit

# tábla
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

# tábla megjelenítés


def show():
    print()
    print()
    print("\u001b[31m" "*************""\u001B[0m")
    print("\u001b[31m" '|', board[0], '|', board[1], '|', board[2], '|'"\u001B[0m")
    print("\u001b[31m" "*************""\u001B[0m")
    print("\u001b[31m" '|', board[3], '|', board[4], '|', board[5], '|'"\u001B[0m")
    print("\u001b[31m" "*************""\u001B[0m")
    print("\u001b[31m" '|', board[6], '|', board[7], '|', board[8], '|'"\u001B[0m")
    print("\u001b[31m" "*************""\u001B[0m")

# tábla ellenőrzése


def check(character, s1, s2, s3):
    if board[s1] == character and board[s2] == character and board[s3] == character:

        if character == player_character:
                board[s1] = "\u001B[35m" + character + "\u001B[0m"
                board[s2] = "\u001B[35m" + character + "\u001B[0m"
                board[s3] = "\u001B[35m" + character + "\u001B[0m"
                show()
                print("\u001b[1;31m {} is the winner.\u001b[0m!".format(player_character))
                endGame()

        if character == computer_character:
                board[s1] = "\u001B[35m" + character + "\u001b[0m"
                board[s2] = "\u001B[35m" + character + "\u001b[0m"
                board[s3] = "\u001B[35m" + character + "\u001b[0m"
                show()
                print("\u001b[1;31m {} is the winner.\u001b[0m!".format(computer_character))
                endGame()


# hármasok vizsgálása
def fullCheck(character):
    check(character, 0, 1, 2)
    check(character, 1, 4, 7)
    check(character, 6, 7, 8)
    check(character, 3, 4, 5)
    check(character, 0, 1, 2)
    check(character, 2, 4, 6)
    check(character, 0, 4, 8)
    check(character, 2, 5, 8)

    num_filled = 0
    for i in range(0, 9):
        if board[i] != " ":
            num_filled = num_filled + 1
    if num_filled == 9:
        print("it's a tie")
        endGame()


def game():

    while True:

        data = input("\u001b[1;32mSelect a spot: \u001b[0m")

        while data not in spotlist:
            print("Not valid.")
            data = input("\u001b[1;32mSelect a spot: \u001b[0m")

        data = int(data)

        if board[data - 1] != player_character and board[data - 1] != computer_character:
            board[data - 1] = player_character
            fullCheck(player_character)
            finding = True

# gép
            while finding is True:
                random.seed()
                computer = random.randint(0, 8)

                if board[computer] != player_character and board[computer] != computer_character:
                    board[computer] = computer_character
                    fullCheck(computer_character)
                    finding = False
                    show()

                else:
                    print("You already selected this spot.")
                    show()

# multiplayer


def multiGame():
    while True:
        data = 9999
        while data > 9 or data < 1 or board[data - 1] == player_character or board[data - 1] == computer_character:
            data = input("\u001b[1;32m Player 1, select a spot: \u001b[0m")
            data = int(data)
            if data > 9 or data < 1:
                print("Not valid.")

        board[data - 1] = player_character
        fullCheck(player_character)
        show()

# player 2
        data2 = 9999
        while data2 > 9 or data2 < 1 or board[data2 - 1] == player_character or board[data2 - 1] == computer_character:
            data2 = input("\u001b[1;32mPlayer 2, select a spot: \u001b[0m")
            data2 = int(data2)
            if data2 > 9 or data2 < 1:
                print("Not valid.")

        board[data2 - 1] = computer_character
        fullCheck(computer_character)
        show()

# kilépés


def endGame():
    global board
    play_again = input("Would you like to play again? (y/n): ")
    if play_again == "y":
        board = [" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "]
        players()
        show()

    if play_again == "n":
        exit_game = input("Press q to quit: ")
        quit = "q"
        sys.exit()


def main():
    welcome()
    players()


if __name__ == "__main__":
    main()

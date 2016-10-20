import random
import sys

#választás
def welcome():
    print("Welcome to Tic-Tac-Toe game.")

def players():
    player = int(input("Press 1 or 2 to choose single/multiplayer mode (or press any key to exit): "))

#computer ellen

    if player == 1:
        show()
        game()

#kétjátékos mód

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
    print ("*************")
    print ( '|', board[0], '|', board[1], '|',board[2], '|')
    print ("*************")
    print ('|', board[3], '|', board[4], '|',board[5], '|')
    print ("*************")
    print ('|', board[6], '|', board[7], '|',board[8], '|')
    print ("*************")

# tábla ellenőrzése
def check(character,s1,s2,s3):
    if board[s1] == character and board[s2] == character and board[s3] == character:
        
        if character == "x":
                board[s1] = "\u001B[35m" + character + "\u001B[0m"
                board[s2] = "\u001B[35m" + character + "\u001B[0m"
                board[s3] = "\u001B[35m" + character + "\u001B[0m"
                show()
                print("\u001b[1;31m x is the winner.\u001b[0m!")
                endGame()
                
        if character == "o":
                board[s1] = "\u001B[35m" + character + "\u001b[0m"
                board[s2] = "\u001B[35m" + character + "\u001b[0m"
                board[s3] = "\u001B[35m" + character + "\u001b[0m"
                show()
                print(" \u001b[1;31m o is the winner. \u001b[0m.")
                endGame()
                

# hármasok vizsgálása
def fullCheck(character):
    if check(character, 0, 1, 2):
        True
    if check(character, 1, 4, 7):
        True
    if check(character, 6, 7, 8):
        True
    if check(character, 3, 4, 2):
        True
    if check(character, 0, 1, 2):
        True 
    if check(character, 2, 4, 6):
        True 
    if check(character, 0, 4, 8):
        True 

# hely választás
def game():
    while True:
        data = input("\u001b[1;32mSelect a spot: \u001b[0m")
        data = int(data)
        while data > 9 or data <1: 
            print("Not valid.")
            data = input("\u001b[1;32mSelect a spot: \u001b[0m")
            data = int(data)

        if board[data-1] !='x' and board[data-1] !='o':
           board[data-1] = 'x'
           fullCheck("x")
           finding = True

    
#gép
           while finding == True:
                random.seed()
                computer = random.randint(0,8)
                if board[computer] !='x' and board[computer] !='o':
                   board[computer] = 'o'
                   fullCheck("o")
                   finding = False
                   show()

        else:
             print("You already selected this spot.")
             show()

# multiplayer
def multiGame():
     while True:
        data = input("\u001b[1;32mSelect a spot: \u001b[0m")
        data = int(data)
        while data > 9 or data <1: 
            print("Not valid.")
            data = input("\u001b[1;32mSelect a spot: \u001b[0m")
            data = int(data)
 
        if board[data-1] !='x' and board[data-1] !='o':
            board[data-1] = 'x'
            fullCheck("x")
            finding = True
            show()

            while finding == True:
                    data2 = input("\u001b[1;32mSelect a spot: \u001b[0m")
                    data2 = int(data2)
                    while data > 9 or data <1: 
                        print("Not valid.")
                        data2 = input("\u001b[1;32mSelect a spot: \u001b[0m")
                        data2 = int(data)
                    if board[data2-1] !='x' and board[data2-1] !='o':
                        board[data2-1] = 'o'
                        fullCheck("o")
                        finding = False
                        show()
            
# kilépés
def endGame():
    play_again = input("Would you like to play again? (y/n): ")
    if play_again == "y": 
        board = [" ", " ", " ",                 
         " ", " ", " ",                 
         " ", " ", " "]    
        global board
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
#  MAKE CHECKERS


# 1  2  3  4

# [ ][b][ ][b][ ][b][ ][b][ ]
# [b][ ][b][ ][b][ ][b][ ][b]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ]



# b1 c2

letters = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}

board = [
    ["[ ]","[0]","[ ]","[0]","[ ]","[0]","[ ]","[0]"],
    ["[0]","[ ]","[0]","[ ]","[0]","[ ]","[0]","[ ]"],
    ["[ ]","[0]","[ ]","[0]","[ ]","[0]","[ ]","[0]"],
    ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    ["[1]","[ ]","[1]","[ ]","[1]","[ ]","[1]","[ ]"],
    ["[ ]","[1]","[ ]","[1]","[ ]","[1]","[ ]","[1]"],
    ["[1]","[ ]","[1]","[ ]","[1]","[ ]","[1]","[ ]"]
]

top = "   a  b  c  d  e  f  g  h"

player_names = []
player_indicators = []

#player names [0][0] is the character that will be used for their peices

#use {} to indicate the move that just happened, moves you can make, etc.

print("The first letter of your name will be the symbol of your piece.") #implement error checking to make sure nobody chooses numbers

player_names.append(input("Player one's name? "))

while True:
    player_two_name = input("Player two's name? ")
    if player_two_name[0] != player_names[0][0]:
        player_names.append(player_two_name)
        break
    else:
        print("names can't start with the same character!")

print(f"Player 1: {player_names[0]} symbol = {player_names[0][0]}")
print(f"Player 2: {player_names[1]} symbol = {player_names[1][0]}")

input("Press enter to start.")










who_move = 0 #this is not done

#ABOVE HERE IS SETUP  ^^^^

#THIS IS THE GAME LOOP vvvvv

while True:
    i = 0
    print(top)
    for row in board:
        to_draw = ""
        for space in row:
            if space == "[0]":
                to_draw = to_draw + "["+player_names[0][0]+"]"
            elif space == "[1]":
                to_draw = to_draw + "["+player_names[1][0]+"]"
            else:
                to_draw = to_draw + space
            
        print(str(i+1)+" "+to_draw) #puts the numbers to left of board
        i += 1

    print(f"It is {player_names[who_move]}'s turn.")

    while True:
        game_input = input()

        if game_input == "stop":
            break
        
        #The inpupt structure for a move is naming the target spaces. IE a6b5, or a6c4 if you are capturing.
        try:
            game_input
            move_to_try = [
                str(letters[game_input[1]]),
                int(game_input[2]),
                str(letters[game_input[3]]),
                int(game_input[4])
                ]
            break
        except:
            continue



        #THIS IS THE CODE FOR MAKING A MOVE.

        #use capital letter for kings.


    
        
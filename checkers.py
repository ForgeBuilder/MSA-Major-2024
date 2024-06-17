#  MAKE CHECKERS


# 1  2  3  4

# [ ][b][ ][b][ ][b][ ][b][ ]
# [b][ ][b][ ][b][ ][b][ ][b]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ]



# b1 c2

letters = ["a","b","c","d","e","f","g","h"]

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

top = "   1  2  3  4  5  6  7  8"

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










move = 0 #this is not done

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
            
        print(letters[i]+" "+to_draw)
        i += 1

    print(f"It is {move}'s turn.")
    if input() == "stop":
        break
  

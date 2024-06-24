import random
#import rare

#make snake????

class bcolors: # try to get this class from import?
    WHITE = '\033[0m' #clears all formatting.
    RED = '\033[91m'
    BLUE = '\033[94m'

def clamp(input,min,max):
    if input > max:
        return max
    if input < min:
        return min
    else:
        return input

def is_king(thing):
    if thing == thing.upper():
        return True
    else:
        return False

def draw_board():
    row_number = 0
    print(top)
    for row in board:
        to_draw = ""
        for space in row:
            if space == "[0]":                            
                to_draw = to_draw + f"[{bcolors.RED}{player_names[0][0]}{bcolors.WHITE}]"              #Where 0 and 1 become the colored player icons
            elif space == "[1]":
                to_draw = to_draw + f"[{bcolors.BLUE}{player_names[1][0]}{bcolors.WHITE}]"
            else:                                                                           
                to_draw = to_draw + space
            
        print(str(row_number+1)+" "+to_draw) #puts the numbers to left of board
        row_number += 1

    print(f"It is {player_names[who_move]}'s turn.")

#  MAKE CHECKERS

#https://www.happycodeclub.com/python-using-hex-colour-codes/ COLOR MORE HEX COLORS!!

# 1  2  3  4

abcd = [None,"a","b","c","d","e","f","g","h"]

# [ ][b][ ][b][ ][b][ ][b][ ]
# [b][ ][b][ ][b][ ][b][ ][b]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ]

allowed_first_characters = {"a":True,"b":True,"c":True,"d":True,"e":True,"f":True,"g":True,"h":True,"i":True,"j":True,"k":True,"l":True,"m":True,"n":True,"o":True,"p":True,"q":True,"r":True,"s":True,"t":True,"u":True,"v":True,"w":True,"x":True,"y":True,"z":True}

# b1 c2

letters = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}

board = [
    ["   ","[0]","   ","[0]","   ","[0]","   ","[0]"],
    ["[0]","   ","[0]","   ","[0]","   ","[0]","   "],
    ["   ","[0]","   ","[0]","   ","[0]","   ","[0]"],
    ["[ ]","   ","[ ]","   ","[ ]","   ","[ ]","   "],
    ["   ","[ ]","   ","[ ]","   ","[ ]","   ","[ ]"],
    ["[1]","   ","[1]","   ","[1]","   ","[1]","   "],
    ["   ","[1]","   ","[1]","   ","[1]","   ","[1]"],
    ["[1]","   ","[1]","   ","[1]","   ","[1]","   "]
]

top = "   a  b  c  d  e  f  g  h"

player_names = []
player_indicators = []

#player names [0][0] is the character that will be used for their peices

#use {} to indicate the move that just happened, moves you can make, etc.

print("The first letter of your name will be the symbol of your piece.") #implement error checking to make sure nobody chooses numbers

while True:
    player_one_name = input("Player one's name? ").lower()
    try:
        if allowed_first_characters[player_one_name[0]]:
            player_names.append(player_one_name)
            break
    except:
        print("First character must be a letter!")
        continue



while True:
    player_two_name = input("Player two's name? ").lower()
    if player_two_name[0] != player_names[0][0]:
        try:
            if allowed_first_characters[player_two_name[0]]:
                player_names.append(player_two_name)
                break
        except:
            print("First character must be a letter!")
            continue
    else:
        print("names can't start with the same character!")

print(f"Player 1: {player_names[0]} symbol = {player_names[0][0]}")
print(f"Player 2: {player_names[1]} symbol = {player_names[1][0]}")

input("Press enter to start.")


who_move = 0
who_not_move = 1

#ABOVE HERE IS SETUP  ^^^^

# BIG BREAK IN FUNCTIONALITY HERE (not boken just diffrent stuff)

#THIS IS THE GAME LOOP vvvvv

rand = False
rand_tries = 0

while True:
    #Theses two loops are important bc of stuff further down. The stuff for changing turn only should happen if the inner loop is broken (with break its not like.. broken broken.).

    while True:

        if (not rand) or rand_tries > 500:
            rand_tries = 0
            draw_board()
            game_input = input()
        else:
            game_input = "rand"
            rand_tries += 1

        if game_input == "stop":
            break
        
        #The inpupt structure for a move is naming the target spaces. IE a6b5, or a6c4 if you are capturing.

        if game_input == "rand": # this functionality is bad and terrible and a joke lmao
            rand = True

            xy = [random.randint(1,8),random.randint(1,8)]
            plus_minus = [1,-1]
            plus_minus = plus_minus[random.randint(0,1)]

            one_or_two = random.randint(1,2)

            

            game_input = abcd[clamp(xy[0],1,8)] + str(clamp(xy[1],1,8)) + abcd[clamp(xy[0]+(one_or_two*plus_minus),1,8)] + str(clamp(xy[1]+(one_or_two*plus_minus),1,8))

            print(game_input)
        try:
            move_to_try = [                 #Checking for a valid input syntax
                (letters[game_input[0]])-1,
                int(game_input[1])-1,
                (letters[game_input[2]])-1,
                int(game_input[3])-1
                ]
            
            # print(move_to_try[0])
            # print(move_to_try[1])
            # print(move_to_try[2])
            # print(move_to_try[3])

        except:
            print("Bad move syntax. Example: b3a4")
            continue

        # print(board[move_to_try[1]][move_to_try[0]][1])

        if board[move_to_try[1]][move_to_try[0]][1] == str(who_move): # Check if you own the peice #the one bracket at the end of the first expression [1] is for getting the middle symbol of [0] or [1] on the board. second character is [1].
            
            if (who_move == 0) != (move_to_try[1] > move_to_try[3]) or is_king(player_names[who_move][1]): #Are you trying to move backwards? (the != acts as an xor gate right now.) move_to_try[1] is the first y value, move_to_try[3] is where peice is going.

                if abs(move_to_try[0]-move_to_try[2]) == 1 and abs(move_to_try[1]-move_to_try[3]) == 1: # Is this a regular (1 space) move? (computer can't stop u from going backwards yet)

                    if board[move_to_try[3]][move_to_try[2]] == "[ ]": # Is the target space empty?

                        board[move_to_try[3]][move_to_try[2]] = board[move_to_try[1]][move_to_try[0]] # place your peice where it goes
                        board[move_to_try[1]][move_to_try[0]] = "[ ]" # remove your peice from where it was
                        break
                    
                elif abs(move_to_try[0]-move_to_try[2]) == 2 and abs(move_to_try[1]-move_to_try[3]) == 2: # Is this a taking move (2 spaces)?

                    if board[move_to_try[3]][move_to_try[2]] == "[ ]": #Is the target space empty?

                        if board[int((move_to_try[3]+move_to_try[1])/2)][int((move_to_try[2]+move_to_try[0])/2)] == "["+str(who_not_move)+"]": # Is the space inbetween an enemy?

                            board[int((move_to_try[3]+move_to_try[1])/2)][int((move_to_try[2]+move_to_try[0])/2)] = "[ ]" # kill enemy
                            board[move_to_try[3]][move_to_try[2]] = board[move_to_try[1]][move_to_try[0]] # place your peice where it goes
                            board[move_to_try[1]][move_to_try[0]] = "[ ]" # remove your peice from where it was
                            break

                                #Need to change stuff with is_king()
                else:
                    print("You can't move here!")
            else:
                print("This peice can't move backwards!")
        else:
            print("This is not your peice!")

#All this code is for if the move is successfull vvv the inner loop breaks and this happens when move works.



#SUPER BIG ISSUE HERE: THE GAME'S DATA IS THE 1s and 0s, NOT LETTERS, THERFORE CAPITALISATION WILL NOT WORK. EITHER USE LIKE, 2 and 3 OR JUST MAKE LETTERS HOW THE GAME WORKS INTERPRETER IS GOOBER AHH SORTA


    promo_y = board[move_to_try[3]] # This is for promoting peices

    if (who_move == 0 and promo_y == 7) or (who_move == 1 and promo_y == 0): # This is for promoting peices
        board[move_to_try[3]] = board[move_to_try[3]].upper() # This is for promoting peices



    rand = False #If the move is successfull we stop trying to do random by changing this

    if who_move == 0: #change who's turn it is
        who_move = 1
        who_not_move = 0
    else:
        who_move = 0
        who_not_move = 1
    if game_input == "stop":
        break

        


        #THIS IS THE CODE FOR MAKING A MOVE.

        #use capital letter for kings.
    
        
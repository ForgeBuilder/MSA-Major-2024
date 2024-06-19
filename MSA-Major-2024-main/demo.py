


def print_type(var):
  print(var)
  print(type(var))
  if type(var) == "<class 'str'>":
    print(f"Variable {var} is a string.")



((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

def hello_world():
  
  print("Hello world!")
  #create a variable to store my name

  
  name = input("What is your first name? ")

  lastName = input("What is your last name? ")
  
  print("Hello", name, lastName) 

  hello_world = "hi" #This way of naming variables is called snake case,
                     #I should probably change my names from nameOne to name_one
  
  print("What is your name? ( ͡^ ͜ʖ ͡^)")

  #the input() function creates an input in the conEsole and the code will wait untill console code is updated.
  name = input()

  print(name + " Is a stupid name!  ):<  ")

  #print the data type of name

  print(type(name))

  #f uses the format function to insert the variable into the string.
  #Basicly u need f in order for these vv brackets to work.
  print(f"My name is not {name} {lastName}, and I am a goober!")
  print("My name is not {name} {lastName}, and I am a goober!")
  #See the diffrence? ^^

  #/n is new like in ftype
  
  age = 16
  weight = "2 billion"

  print(f"name is a {type(name)}string \n age is a {type(age)} int \n weight is another {type(weight)} bozo hahahahah")

 


  



def game():
    position = [100, 100]

    world_def = ["[ ]",]
  
    world = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]

    print("Game started!")

    ready = False
    while not ready:
        character_name = input("Name: ")
        if len(character_name) == 1:
            ready = True
  
    while True:
    #This is the game loop. it never ends!!! muahahahahahahahahahahahahahahahahahahahaha
    

    
    #this draws the world
        toDraw = ""
        for j in range(len(world)):
            toDraw = ""
            for i in range(len(world[j])):
                toDraw = toDraw + world_def[world[j][i]]
            print(toDraw)
        gameinput = input()

#beggining of main function

hello_world()

print("Play game?")
if input() == "Yes":
  game()
  if input() == "No":
    print("die")


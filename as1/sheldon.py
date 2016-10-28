import random
game_option = ['rock','lizard','spock','paper','scissor']
scissor = ['paper','lizard']
paper = ['rock', 'spock']
rock = ['lizard','scissor']       
lizard = ['spock','paper']
spock = ['scissor','rock']

def input_user():
  user_option = raw_input("\nYour choice ")
  return user_option

def random1():
  return random.choice(game_option)

def decide_result(user,comp):

  if user == comp:
    return "draw"

  elif user == 'scissor':
    for element in scissor:
        if comp == element:
            return 'win'
    return 'lose'

  elif user == 'paper':
    for element in paper:
        if comp == element:
            return 'win'
    return 'lose'

  elif user == 'rock':
    for element in rock:
        if comp == element:
            return 'win'
    return 'lose'


  elif user == 'spock':
    for element in spock:
        if comp == element:
            return 'win'
    return 'lose'

  if user == 'lizard':
    for element in lizard:
        if comp == element:
            return 'win'
    return 'lose'

def checkValidInput(user_opt):
  if user_opt in game_option:
    return True
  return False

  
def play_game():
  user_opt = input_user()
  if user_opt == "exit":
    quit()

  elif checkValidInput(user_opt):
    computer = random1()
    print "computer chooses: " + computer
    result = decide_result(user_opt,computer)
    print "\nyou " + result
  else:
    print "\nError!!!Choose Again\n"
    basic_info()

  play_game()

def basic_info():
  print("Select your choices: ")
  for element in game_option:
    print " " + element
  print("\n Quit game: exit")

def main():

  print("\n\tWelcome to Sheldon's Game\n")
  basic_info()
  play_game()

if __name__ == '__main__': 
    main()















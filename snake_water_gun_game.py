"""This Python script simulates the classic "Snake, Water, Gun" game where the computer randomly chooses one option, and the user inputs their choice; 
it then determines and prints the outcome (win, lose, or draw) based on the game's rules."""

import random
l=random.randint(1,3)
a=int(input("""enter your choice
1.snake 2.water 3.gun :"""))
if l==1:
  print("computer choice is snake")
  if a==1:
    print("draw")
  elif a==2:
    print("u won")
  else:
    print("u lost")
if l==2:
  print("computer choice is water")
  if a==1:
    print("u win")
  elif a==2:
    print("draw")
  else:
    print("u lost")

if l==3:
  print("computer choice is gun")
  if a==1:
    print("u lost")
  elif a==2:
    print("u won")
  else:
    print("draw")

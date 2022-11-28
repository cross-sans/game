import random as ran
from files import game
def attack():
  enemList = ["skeleton","goblin","orc"]
  enemy = ran.choice(enemList)
  if enemy == "orc":
    game.cash += 200
    game.hp -= ran.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32])
    game.inventory = list(game.inventory)
    game.inventory.append("sword")
    print(enemy,"attacked you")
  if enemy == "goblin":
    game.cash+=ran.choice([1,2,3,4])*10
    game.hp -= 4
    print(enemy, 'attacked you')
  if enemy == "skeleton":
    game.cash+=ran.choice([1,2,3,4])*20
    game.hp -= 6
    game.inventory = list(game.inventory)
    game.inventory.append("bone ")
    print(enemy, 'attacked you')
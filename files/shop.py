from files import shopFiles
from files.shopFiles import potions
from files import game

potions = potions.potions
def shop():
  print(potions)
  ev =''
  while ev != "close":
    print("chose one")
    ev = input()
    if ev == "1" and game.cash >= 10:
      print("you got healing potion")
      game.cash -= 10
      game.items.append("potion")
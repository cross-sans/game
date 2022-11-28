def main():
  from files import enemys, shop
  from files.shop import shop
  print("""this is a free game
your hp will be drained constantly
""")

  def saveHP():
    with open('hp.txt', 'w+') as h:
      h.write(str(hp))

  def saveCash():
    with open('cash.txt', 'w+') as h:
      h.write(str(cash))

  def saveInv():
    with open('inventory.txt', 'w+') as h:
      h.write(str(inventory))

  def saveItem():
    with open('items.txt', 'w+') as h:
      h.write(str(items))

  def loadItem():
    with open('items.txt') as h:
      global items
      items = h.read()
      items = list(items)

  def loadHP():
    with open('hp.txt') as h:
      global hp
      hp = h.read()
      hp = int(hp)

  def loadCash():
    with open('cash.txt') as h:
      global cash
      cash = h.read()
      cash = int(cash)

  def loadInv():
    with open('inventory.txt') as h:
      global inventory
      inventory = h.read()

  try:
    loadHP()
    loadCash()
    loadInv()
    loadItem()

  except:
    global items
    items = []
    global inventory
    inventory = ''
    global cash
    cash = 0
    global hp
    hp = 100
    saveHP()
    saveCash()
    saveInv()
    saveItem()
  while hp > 0:
    hp -= 1
    print('your hp:', hp, '\nyour cash:', cash, '\nyour inventory:', inventory,
          '\nconsumables:', items)
    act = input('next action: ')
    if act == "save":
      saveHP()
      saveCash()
      saveInv()
      saveItem()
    if act == "load":
      loadCash()
      loadHP()
      loadInv()
      loadItem()

    if act == "sell":
      for item in inventory:
        inventory = list(inventory)
        inventory.remove(item)
        if item != "sword":
          cash += 10
        if item == "sword":
          cash += 100
        if inventory == []:
          inventory = ''

    if act == "heal" and items != []:
      hp += 10
      items.remove('potion')
        
    if act == "shop":
      sho = True
      shop()

    if act == "attack":
      enemys.attack()
    if hp == 0:
      hp = 100
      saveHP()
      print("dead")
      break

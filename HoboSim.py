from random import randint
hp = 20
money = 3
burger = 2
water = 1
bandage = 0
medkit = 0
sanity = 10
hunger = 20
thirst = 15
time = 12
beg_passive = 5
beg_agressive = 8
ripped_shirt = False
ripped_pants = False
bandage = 0
medkit = 0
main_menu_bool = False
has_items = True

def main_menu():
  print("-")
  print("Hobo Sim 0.01")
  print("1) Play")
  print("2) Info")
  print("3) Exit")
  player_input = input()
  return player_input

def main_menu_info():
  print("-\nIn Hobo Sim, you are a Hobo\nYour goal is to become the richest man alive\nHow you get there is your choice....")
  

def main():
  global hp
  global money
  global sanity
  global hunger
  global thirst
  global time
  print("-")
  print("-- Health: " + str(hp) + " -- Hunger: " + str(hunger) + " -- Thirst: " + str(thirst) + " -- Sanity: " + str(sanity) + " --")
  print("-- Time: " + str(time) + " --")
  print("-- Money: " + str(money) + " --")
  print("What will you do?")
  print("1) Beg Passively")
  print("2) Beg Agressively")
  print("3) Go to Store")
  print("4) Open Backpack")
  print("5) Go to Sleep")
  player_input = input()
  if player_input == "1": #Beg Passively
    beg_passively()
    print("-")
    print("You decide to Beg Passively!")
    print("You gain " + str(beg_passive) + " Dollars")
    print("You lose 2 Hunger")
    print("You lose 1 Thirst")
    print("You lose 2 Sanity")
    print("The Time is now " + str(time))
  elif player_input == "2": #Beg Agressively
    beg_agressively()
    print("-")
    print("You decide to Beg Agressively!")
    print("You gain " + str(beg_agressive) + " Dollars")
    print("You lose 1 Hunger")
    print("You lose 0 Thirst")
    print("You lose 1 Sanity")
    print("The Time is now " + str(time))
  elif player_input == "3": #Store
    go_to_store()
  elif player_input == "4":
    backpack()
  elif player_input == "5":
    sleep()
  else:
    main()  

def beg_passively():
  global time
  global money
  global hunger
  global thirst
  global sanity
  global beg_passive
  time += 2
  money += beg_passive
  hunger -= 2
  thirst -= 1
  sanity -= 2

def beg_agressively():
  global time
  global money
  global hunger
  global sanity
  global hp
  time += 1
  money += beg_agressive
  hunger -= 1
  hp -= 8
  sanity -= 1

def go_to_store():
  global money
  global time
  if time >= 0 and time <= 6:  #If Closed
    print("-")
    print("Torgot is Closed")
    print("Hours: 7 to 23")
  else:  #Is Open
    print("-")
    print("Welcome to Torgot")
    print("You will find all of your item needs here!")
    print("You have " + str(money) + " Dollars!")
    print("Where would you like to go?")
    print("1) Food and Beverages")
    print("2) Clothes")
    print("3) Medical")
    print("4) Leave Torgot")
    player_input = input()
    if player_input == "1": #Food
      store_food()
    elif player_input == "2": #Clothes
      store_clothes()
    elif player_input == "3": #Medical
      store_medical()
    elif player_input == "4": #Leave Store (takes 1 hour)
      time += 1
    else:
      go_to_store()
      
     
def store_food():
  global burger
  global water
  global money
  global has_items
  burger_cost = 15
  water_cost = 15
  print("-")
  print("You have " + str(money) + " Dollars!")
  print("You read a sign, it says Food")
  print("You assume you are now in the food section of the store")
  print("What will you do?")
  print("1) Buy Burger")
  print("2) Buy Water")
  print("3) Go Back")
  player_input = input()
  if player_input == "1" and money >= burger_cost: #If can buy Burger
    burger += 1
    money -= 15
    has_items = True
    print("You buy a Burger")
    print("You gain 1 Burger")
    print("You lose " + str(burger_cost) + " Dollars")
    store_food()
  elif player_input == "2" and money >= water_cost: #If can buy Water
    water += 1
    money -= 15
    has_items = True
    print("You buy a Water")
    print("You gain 1 Water")
    print("You lose" + str(water_cost) + " Dollars")
    store_food()
  elif player_input == "1" and money < burger_cost or player_input == "2" and money < water_cost: #If cant buy Burger/Water
    print("-")
    print("You do not have enough Money to buy this item!")
    store_food()
  elif player_input == "3": #Go back
    go_to_store()
  else:   #Invalid command
    store_food()

def store_clothes():
  global money
  global ripped_pants
  global ripped_shirt
  ripped_pants_cost = 75
  ripped_shirt_cost = 60
  print("-")
  print("You have " + str(money) + " Dollars!")
  print("You read a sign, it says Clothes")
  print("You assume you are now in the clothes section of the store")
  print("What will you do?")
  print("1) Buy Ripped Shirt")
  print("2) Buy Ripped Pants")
  print("3) Go Back")
  player_input = input()
  if player_input == "1" and money >= ripped_shirt_cost:  #If has enough money for Shirt
    if ripped_shirt:  #If already have Shirt
      print("-")
      print("You already have a Ripped Shirt!")
      store_clothes()
    else:  #If doesnt have shirt and has enough money
      ripped_shirt = True
      money -= ripped_shirt_cost
      print("You buy a Ripped Shirt")
      print("You gain 1 Ripped Shirt")
      print("You lose " + str(ripped_shirt_cost) + " Dollars")
      store_clothes()
  elif player_input == "2" and money >= ripped_pants_cost:  #If has enough money for Pants
    if ripped_pants: #If already have Pants
      print("-")
      print("You already have Ripped Pants!")
      store_clothes()
    else: #If doesnt have Pants and has enough money
      ripped_pants = True
      money -= ripped_pants_cost
      print("You buy a Ripped Pants")
      print("You gain 1 Ripped Pants")
      print("You lose " + str(ripped_pants_cost) + " Dollars")
      store_clothes()
  elif player_input == "3":  #Go back
    go_to_store()
  else:  #Invalid command
    store_clothes()


def store_medical():
  global money
  global bandage
  global medkit
  bandage_cost = 8
  medkit_cost = 25
  print("-")
  print("You have " + str(money) + " Dollars!")
  print("You read a sign, it says Medical")
  print("You assume you are now in the Medical section of the store")
  print("What will you do?")
  print("1) Buy Bandage")
  print("2) Buy Medkit")
  print("3) Go Back")
  player_input = input()
  if player_input == "1" and money >= bandage_cost: #If can buy Bandage
    bandage += 1
    money -= bandage_cost
    print("You buy a Bandage")
    print("You gain 1 Bandage")
    print("You lose" + str(bandage_cost) + " Dollars")
    store_medical()
  elif player_input == "2" and money >= medkit_cost: #If can buy Medkit
    medkit += 1
    money -= medkit_cost
    print("You buy a Medkit")
    print("You gain 1 Medkit")
    print("You lose" + str(medkit_cost) + " Dollars")
    store_medical()
  elif player_input == "1" and money < bandage_cost or player_input == "2" and money < medkit_cost: #If cant buy Bandage/Medkit
    print("-")
    print("You do not have enough Money to buy this item!")
    store_medical()
  elif player_input == "3": #Go back
    go_to_store()
  else:   #Invalid command
    store_medical()


def backpack():
  print("-")
  print("You open your backpack, somehow it orginizes itself into different sections")
  print("What will you do?")
  print("1) Food")
  print("2) Beverages")
  print("3) Clothing")
  print("4) Medical")
  print("5) Go Back")
  player_input = input()
  if player_input == "1":
    backpack_food()
  elif player_input == "2":
    backpack_beverages()
  elif player_input == "3":
    backpack_clothing()
  elif player_input == "4":
    backpack_medical
  elif player_input == "5":
    main()
  else:
    backpack()

def backpack_food():
  global burger  #put all food items under here
  global hunger
  global thirst
  global has_items
  #steak = 0
  #bigmac = 2

  number_of_items = []
  if not(has_items):
    number_of_items.append("1) ")
    number_of_items.append("Go Back")
  print("-")
  if not(has_items):
    print("You have no Food items")
  if burger >= 1: 
    print("Burgers: " + str(burger))
    number_of_items.append("1) ")
    number_of_items.append("Use Burger")
  #if steak >= 1:
    #print("Steaks: " + str(steak))
    #if len(number_of_items) == 0:
      #number_of_items.append("1) ")
      #number_of_items.append("Use Steak")
    #else:
      #number_of_items.append("2) ")
      #number_of_items.append("Use Steak")
  #if bigmac >= 1:
    #print("BigMacs: " + str(bigmac))
    #if len(number_of_items) == 0:
      #number_of_items.append("1) ")
      #number_of_items.append("Use BigMac")
    #elif len(number_of_items) == 2:
      #number_of_items.append("2) ")
      #number_of_items.append("Use BigMac")
    #else:
      #number_of_items.append("3) ")
      #number_of_items.append("Use BigMac") 
  print("What will you do?")
  if len(number_of_items) >= 2:
    print(number_of_items[0] + number_of_items[1])
  if len(number_of_items) >= 4:
    print(number_of_items[2] + number_of_items[3])
  if len(number_of_items) >= 6:
    print(number_of_items[4] + number_of_items[5])
  else:
    has_items = False
    backpack_food()
  player_input = input()
  if player_input == "1":
    if number_of_items[1] == "Use Burger":
      burger -= 1
      hunger += 7
      print("-")
      print("You eat a Burger")
      print("You lose a Burger")
      print("You gain 7 Hunger")
      backpack_food()
    elif number_of_items[1] == "Go Back":
      backpack()
    
def sleep():
  print("LOL")
  
while True:
  while not(main_menu_bool):
    main_menu_input = main_menu()
    if main_menu_input == "1":
      main_menu_bool = True
      break
    elif main_menu_input == "2":
      main_menu_info()
    elif main_menu_input == "3":
      break
    else:
      main_menu()

  while hp > 0 and time < 24 and hunger > 0 and thirst > 0 and sanity > 0 and main_menu_bool:
    main()

  if hp <= 0 or hunger <= 0 or thirst <= 0:
    print("You have died!")
    hp = 20
    money = 3
    burger = 2
    water = 1
    bandage = 0
    medkit = 0
    sanity = 10
    hunger = 20
    thirst = 15
    time = 12
    beg_passive = 5
    beg_agressive = 8
    main_menu_bool = False
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
name = ""
ripped_shirt = False
ripped_pants = False
cat = False
dog = False
rat = False
cockroach = 0
cup_of_change = False
god_bless_sign = False
bike = False
main_menu_bool = False


def main_menu():
  global hp 
  global money
  global burger
  global water
  global bandage
  global medkit
  global sanity
  global hunger
  global thirst
  global time
  global beg_passive
  global beg_agressive
  global ripped_shirt
  global ripped_pants
  global bandage
  global medkit
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
  print("-")
  print("Hobo Sim 0.07")
  print("1) New Game")
  print("2) Load Game")
  print("3) Info")
  print("4) Exit")
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
  global main_menu_bool
  global name
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
  print("6) Save Game")
  print("7) Main Menu")
  player_input = input()
  if player_input == "1": #Beg Passively
    beg_passively()
  elif player_input == "2": #Beg Agressively
    beg_agressively()
  elif player_input == "3": #Store
    go_to_store()
  elif player_input == "4":
    backpack()
  elif player_input == "5":
    sleep()
  elif player_input == "6":
    save_game()
  elif player_input == "7":
    go_to_menu()
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
  print("-")
  print("You decide to Beg Passively!")
  print("You gain " + str(beg_passive) + " Dollars")
  print("You lose 2 Hunger")
  print("You lose 1 Thirst")
  print("You lose 2 Sanity")
  print("The Time is now " + str(time))
  

def beg_agressively():
  global time
  global money
  global hunger
  global thirst
  global sanity
  global hp
  global beg_agressive
  time += 1
  money += beg_agressive
  hunger -= 1
  hp -= 8
  sanity -= 1
  print("-")
  print("You decide to Beg Agressively!")
  print("You gain " + str(beg_agressive) + " Dollars")
  print("You lose 1 Hunger")
  print("You lose 0 Thirst")
  print("You lose 1 Sanity")
  print("The Time is now " + str(time))


def go_to_store():
  global money
  global time
  if time >= 0 and time <= 6:  #If Closed
    print("-")
    print("Torgot is Closed")
    print("Hours: 7 to 23")
    main()
  else:  #Is Open
    print("-")
    print("Welcome to Torgot")
    print("You will find all of your item needs here!")
    print("You have " + str(money) + " Dollars!")
    print("Where would you like to go?")
    print("1) Food and Beverages")
    print("2) Clothes")
    print("3) Medical")
    print("4) Props")
    print("5) Pets")
    print("6) Leave Torgot")
    player_input = input()
    if player_input == "1": #Food
      store_food()
    elif player_input == "2": #Clothes
      store_clothes()
    elif player_input == "3": #Medical
      store_medical()
    elif player_input == "4": #Props
      store_props()
    elif player_input == "5":
      store_pets()
    elif player_input == "6": #Leave Store (takes 1 hour)
      time += 1
    else:
      go_to_store()
      
     
def store_food():
  global burger
  global water
  global money
  burger_cost = 5
  water_cost = 5
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
    money -= burger_cost
    print("You buy a Burger")
    print("You gain 1 Burger")
    print("You lose " + str(burger_cost) + " Dollars")
    store_food()
  elif player_input == "2" and money >= water_cost: #If can buy Water
    water += 1
    money -= water_cost
    print("You buy a Water")
    print("You gain 1 Water")
    print("You lose " + str(water_cost) + " Dollars")
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
  global beg_agressive
  global beg_passive
  ripped_pants_cost = 50
  ripped_shirt_cost = 45
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
    elif not(ripped_shirt) and money < ripped_shirt_cost:
      print("-")
      print("You do not have enough Money to buy this item!")
      store_clothes()
    else:  #If doesnt have shirt and has enough money
      ripped_shirt = True
      money -= ripped_shirt_cost
      beg_agressive += 4
      beg_passive += 4
      print("You buy a Ripped Shirt")
      print("You gain 1 Ripped Shirt")
      print("You will now gain 4 more dollars when Begging!")
      print("You lose " + str(ripped_shirt_cost) + " Dollars")
      store_clothes()
  elif player_input == "2" and money >= ripped_pants_cost:  #If has enough money for Pants
    if ripped_pants: #If already have Pants
      print("-")
      print("You already have Ripped Pants!")
      store_clothes()
    elif not(ripped_pants) and money < ripped_pants:
      print("-")
      print("You do not have enough Money to buy this item!")
      store_clothes()
    else: #If doesnt have Pants and has enough money
      ripped_pants = True
      money -= ripped_pants_cost
      beg_agressive += 4
      beg_passive += 4
      print("You buy a Ripped Pants")
      print("You gain 1 Ripped Pants")
      print("You will now gain 4 more dollars when Begging!")
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
  bandage_cost = 6
  medkit_cost = 20
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
    print("-")
    print("You buy a Bandage")
    print("You gain 1 Bandage")
    print("You lose " + str(bandage_cost) + " Dollars")
    store_medical()
  elif player_input == "2" and money >= medkit_cost: #If can buy Medkit
    medkit += 1
    money -= medkit_cost
    print("-")
    print("You buy a Medkit")
    print("You gain 1 Medkit")
    print("You lose " + str(medkit_cost) + " Dollars")
    store_medical()
  elif player_input == "1" and money < bandage_cost or player_input == "2" and money < medkit_cost: #If cant buy Bandage/Medkit
    print("-")
    print("You do not have enough Money to buy this item!")
    store_medical()
  elif player_input == "3": #Go back
    go_to_store()
  else:   #Invalid command
    store_medical()

def store_props():
  global money
  global god_bless_sign
  global cup_of_change
  global bike
  global beg_passive
  global beg_agressive
  god_bless_sign_cost = 25
  cup_of_change_cost = 35
  bike_cost = 100
  print("-")
  print("You have " + str(money) + " Dollars!")
  print("You read a sign, it says Props")
  print("You assume you are now in the props section of the store")
  print("What will you do?")
  print("1) Buy God Bless Sign")
  print("2) Buy Cup Of Change")
  print("3) Buy Bike")
  print("4) Go Back")
  player_input = input()
  if player_input == "1" and money >= god_bless_sign_cost:  #If has enough money for God Bless Sign
    if god_bless_sign:  #If already have God Bless Sign
      print("-")
      print("You already have a God Bless Sign!")
      store_props()
    elif not(god_bless_sign) and money < god_bless_sign_cost:
      print("-")
      print("You do not have enough Money to buy this item!")
      store_props()
    else:  #If doesnt have god bless sign and has enough money
      god_bless_sign = True
      money -= god_bless_sign_cost
      beg_agressive += 1
      beg_passive += 1
      print("You buy a God Bless Sign")
      print("You gain 1 God Bless Sign")
      print("You will now gain 1 more dollar when Begging!")
      print("You lose " + str(god_bless_sign_cost) + " Dollars")
      store_props()
  elif player_input == "2" and money >= cup_of_change_cost:  #If has enough money for Cup of Change
    if cup_of_change: #If already have Cup of Change
      print("-")
      print("You already have a Cup of Change")
      store_props()
    elif not(cup_of_change) and money < cup_of_change_cost:
      print("-")
      print("You do not have enough Money to buy this item!")
      store_props()
    else: #If doesnt have Cup of Change and has enough money
      cup_of_change = True
      money -= cup_of_change_cost
      beg_agressive += 2
      beg_passive += 2
      print("You buy a Cup of Change")
      print("You gain 1 Cup of Change")
      print("You will now gain 2 more dollars when Begging!")
      print("You lose " + str(cup_of_change_cost) + " Dollars")
      store_props()
  elif player_input == "3" and money >= bike_cost:  #If has enough money for Bike
    if cup_of_change: #If already have Bike
      print("-")
      print("You already have a Bike")
      store_props()
    elif not(bike) and money < bike_cost:
      print("-")
      print("You do not have enough Money to buy this item!")
      store_props()
    else: #If doesnt have Bike and has enough money
      bike = True
      money -= bike_cost
      beg_agressive += 4
      beg_passive += 4
      print("You buy a Bike")
      print("You gain 1 Bike")
      print("You will now gain 4 more dollars when Begging!")
      print("You lose " + str(bike_cost) + " Dollars")
      store_props()
  elif player_input == "4":  #Go back
    go_to_store()
  else:  #Invalid command
    store_props()

def store_pets():
  global money
  global dog
  global cat
  global rat
  global cockroach
  global beg_passive
  global beg_agressive
  dog_cost = 85
  cat_cost = 35
  rat_cost = 15
  cockroach_cost = 1
  print("-")
  print("You have " + str(money) + " Dollars!")
  print("You read a sign, it says Pets")
  print("You assume you are now in the pets section of the store")
  print("What will you do?")
  print("1) Buy Dog")
  print("2) Buy Cat")
  print("3) Buy Rat")
  print("4) Buy Cockroach")
  print("5) Go Back")
  player_input = input()
  if player_input == "1" and money >= dog_cost:  #If has enough money for Dog
    if dog:  #If already have Dog
      print("-")
      print("You already have a Dog!")
      store_pets()
    elif not(dog) and money < dog_cost:
      print("-")
      print("You do not have enough Money to buy this item!")
      store_pets()
    else:  #If doesnt have Dog and has enough money
      dog = True
      money -= dog_cost
      beg_agressive += 4
      beg_passive += 4
      print("You buy a Dog")
      print("You gain 1 Dog")
      print("You will now gain 4 more dollars when Begging!")
      print("You lose " + str(dog_cost) + " Dollars")
      store_pets()
  elif player_input == "2" and money >= cat_cost:  #If has enough money for cat
    if cat:  #If already have cat
      print("-")
      print("You already have a Cat!")
      store_pets()
    elif not(cat) and money < cat_cost:
      print("-")
      print("You do not have enough Money to buy this item!")
      store_pets()
    else:  #If doesnt have cat and has enough money
      cat = True
      money -= cat_cost
      beg_agressive += 3
      beg_passive += 3
      print("You buy a Cat")
      print("You gain 1 Cat")
      print("You will now gain 3 more dollar when Begging!")
      print("You lose " + str(cat_cost) + " Dollars")
      store_pets()
  elif player_input == "3" and money >= rat_cost:  #If has enough money for rat
    if rat:  #If already have rat
      print("-")
      print("You already have a Rat!")
      store_pets()
    elif not(rat) and money < rat_cost:
      print("-")
      print("You do not have enough Money to buy this item!")
      store_pets()
    else:  #If doesnt have rat and has enough money
      rat = True
      money -= rat_cost
      beg_agressive += 2
      beg_passive += 2
      print("You buy a Rat")
      print("You gain 1 Rat")
      print("You will now gain 2 more dollars when Begging!")
      print("You lose " + str(rat_cost) + " Dollars")
      store_pets()
  elif player_input == "4" and money >= cockroach_cost:  #If has enough money for Cockroach
    if cockroach == 2:  #If already have 2 cockroaches
      print("-")
      print("You already have 2 Cockroaches!")
      store_pets()
    elif cockroach < 2 and money < cockroach_cost:
      print("-")
      print("You do not have enough Money to buy this item!")
      store_pets()
    else:  #If doesnt have cockroach and has enough money
      cockroach += 1
      money -= cockroach_cost
      beg_agressive += 1
      beg_passive += 1
      print("You buy a Cockroach")
      print("You gain 1 Cockroach")
      print("You will now gain 1 more dollar when Begging!")
      print("You lose " + str(cockroach_cost) + " Dollars")
      store_pets()
  
  
def backpack():
  print("-")
  print("You open your backpack, somehow it orginizes itself into different sections")
  print("What will you do?")
  print("1) Food")
  print("2) Beverages")
  print("3) Medical")
  print("4) Go Back")
  player_input = input()
  if player_input == "1":
    backpack_food()
  elif player_input == "2":
    backpack_beverages()
  elif player_input == "3":
    backpack_medical()
  elif player_input == "4":
    main()
  else:
    backpack()

def backpack_food():
  global burger  #put all food items under here
  global hunger
  has_burger = False
  print("-")
  if burger > 0: 
    print("You have " + str(burger) + " Burgers") 
    has_burger = True
  print("What will you do?")
  if has_burger:
    print("1) Use Burger")
  print("2) Go Back")
  player_input = input()
  if player_input == "1" and has_burger and hunger < 26:
    burger -= 1
    hunger += 7
    has_burger = False
    print("-")
    print("You eat a Burger")
    print("You lose a Burger")
    print("You gain 7 Hunger")
    backpack_food()
  elif player_input == "1" and hunger > 25 and has_burger:
    print("-")
    print("You are not hungry")
    backpack_food()
  elif player_input == "2":
    backpack()
  else:
    backpack_food()

def backpack_beverages():
  global water  #put all beverage items under here
  global thirst
  has_water = False
  print("-")
  if water > 0: 
    print("You have " + str(water) + " Waters") 
    has_water = True
  print("What will you do?")
  if has_water:
    print("1) Use Water")
  print("2) Go Back")
  player_input = input()
  if player_input == "1" and has_water and thirst < 26:
    water -= 1
    thirst += 5
    has_water = False
    print("-")
    print("You drink a Water")
    print("You lose a Water")
    print("You gain 5 Thirst")
    backpack_beverages()
  elif player_input == "1" and thirst > 25 and has_water:
    print("-")
    print("You are not thirsty")
    backpack_beverages()
  elif player_input == "2":
    backpack()
  else:
    backpack_beverages()

def backpack_medical():
  global bandage  #put all medical items under here
  global medkit
  global hp
  has_bandage = False
  has_medkit = False
  print("-")
  if bandage > 0: 
    print("You have " + str(bandage) + " Bandages") 
    has_bandage = True
  if medkit > 0: 
    print("You have " + str(medkit) + " Medkits") 
    has_medkit = True
  print("What will you do?")
  if has_bandage:
    print("1) Use Bandage")
  if has_medkit:
    print("2) Use Medkit")
  print("3) Go Back")
  player_input = input()
  if player_input == "1" and has_bandage and hp < 17:
    bandage -= 1
    hp += 4
    has_bandage = False
    print("-")
    print("You apply a Bandage")
    print("You lose a Bandage")
    print("You gain 4 Health")
    backpack_medical()
  elif player_input == "1" and has_bandage and hp > 16:
    print("-")
    print("You do not need a Bandage")
    backpack_medical()
  elif player_input == "2" and has_medkit and hp < 5:
    medkit -= 1
    hp += 16
    has_medkit = False
    print("-")
    print("You apply a Medkit")
    print("You lose a Medkiy")
    print("You gain 16 Health")
    backpack_medical()
  elif player_input == "2" and has_medkit and hp > 4:
    print("-")
    print("You do not need a Medkit")
    backpack_medical()
  elif player_input == "3":
    backpack()
  else:
    backpack_medical()

def sleep():
  global time
  global hp
  global hunger
  global thirst
  global sanity
  if time <= 17 and time > 6:
    if sanity < 16:
      time += 5
      sanity += 5
      hunger -= 4
      thirst -= 3 
      print("-")
      print("You decide to sleep for the day")
      print("You gain 5 Sanity")
      print("You lose 4 Hunger")
      print("You lose 3 Thrist")
      print("The time is now " + str(time)) 
    else:
      print("-")
      print("You are not tired")
  else:
    if sanity < 16:
      time += 9
      sanity += 9
      hunger -= 5
      thirst -= 4 
      print("-")
      print("You decide to sleep for the night")
      print("You gain 9 Sanity")
      print("You lose 5 Hunger")
      print("You lose 4 Thrist")
      print("The time is now " + str(time))
    else:
      print("-")
      print("You are not tired")

def save_game():
  global hp 
  global money
  global burger
  global water
  global bandage
  global medkit
  global sanity
  global hunger
  global thirst
  global time
  global beg_passive
  global beg_agressive
  global ripped_shirt
  global ripped_pants
  global bandage
  global medkit
  print("-")
  print("Are you sure you want to Save?")
  print("You will lose all previous Saves under your Hobo name")
  print("1) Yes")
  print("2) No")
  player_input = input()
  if player_input == "1":
    save = open(name + ".txt", "w+")
    save.writelines([str(hp) + "\n", str(money) + "\n", str(burger) + "\n", str(water) + "\n", str(bandage) + "\n", str(medkit) + "\n", str(sanity) + "\n", str(hunger) + "\n", str(thirst) + "\n", str(time) + "\n", str(beg_passive) + "\n", str(beg_agressive) + "\n", str(cockroach) + "\n", str(ripped_pants) + "\n", str(ripped_shirt) + "\n", str(cat) + "\n", str(dog) + "\n", str(rat) + "\n", str(cup_of_change) + "\n", str(god_bless_sign) + "\n", str(bike) + "\n", "CHANGING THE VALUES IN THIS FILE MAY LEAD TO UNEXPECTED RESULTS OR MAY CORRUPT YOUR SAVE FILE!"])
    save.close()
  
def go_to_menu():
  global main_menu_bool
  print("-")
  print("Are you sure you want to go to the Main Menu?")
  print("You will lose any unsaved progress")
  print("1) Yes")
  print("2) No")
  player_input = input()
  if player_input == "1":
    main_menu_bool = False
  elif player_input == "2":
    main()
  else:
    go_to_menu()

while True:
  while not(main_menu_bool):
    main_menu_input = main_menu()
    if main_menu_input == "1":
      print("-")
      print("What will your name your Hobo?")
      name = input()
      name = name.lower()
      main_menu_bool = True
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
      cat = False
      dog = False
      rat = False
      cockroach = 0
      cup_of_change = False
      god_bless_sign = False
      bike = False
      break
    if main_menu_input == "2":
      print("-")
      print("Enter the name of your Hobo")
      save_name = input()
      save_name = save_name.lower()
      try:
        load = open(save_name + ".txt", "r")
        hp = int(load.readline())
        money = int(load.readline())
        burger = int(load.readline())
        water = int(load.readline())
        bandage = int(load.readline())
        medkit = int(load.readline())
        sanity = int(load.readline())
        hunger = int(load.readline())
        thirst = int(load.readline())
        time = int(load.readline())
        beg_passive = int(load.readline())
        beg_agressive = int(load.readline())
        cockroach = int(load.readline())
        pants = load.readline()
        shirt = load.readline()
        cat = load.readline()
        dog = load.readline()
        rat = load.readline()
        cup_of_change = load.readline()
        god_bless_sign = load.readline()
        bike = load.readline()
        if pants[0] == "T":
          ripped_pants = True
        else:
          ripped_pants = False
        if shirt[0] == "T":
          ripped_shirt = True
        else:
          ripped_shirt = False
        name = save_name
        main_menu_bool = True
        load.close()
        if cat[0] == "T":
          cat = True
        else:
          cat = False
        if dog[0] == "T":
          dog = True
        else:
          dog = False
        if rat[0] == "T":
          rat = True
        else:
          rat = False
        if cup_of_change[0] == "T":
          cup_of_change = True
        else:
          cup_of_change = False
        if god_bless_sign[0] == "T":
          god_bless_sign = True
        else:
          god_bless_sign = False
        if bike[0] == "T":
          bike = True
        else:
          bike = False
        break
      except FileNotFoundError:
        print("-")
        print("Hobo does not exist!")
        break
      except:
        print("-")
        print("Unknown Load error")
        break
    elif main_menu_input == "3":
      main_menu_info()
    elif main_menu_input == "4":
      exit(0)
    else:
      main_menu()

  while hp > 0 and time < 24 and hunger > 0 and thirst > 0 and sanity > 0 and main_menu_bool and name != "":
    main()

  if hp <= 0 or hunger <= 0 or thirst <= 0:
    print("-")
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
  elif sanity <= 0:
    sanity = 0
    sanity += 3
    hunger -= 4
    thirst -+ 3
    time += 3
    print("-")
    print("You pass out on the streets causing you to have bad sleep")
    print("You gain 3 Sanity")
    print("You lose 4 Hunger")
    print("You lose 3 Thirst")
    print("The Time is now " + str(time))
  elif time >= 24:
    time -= 24

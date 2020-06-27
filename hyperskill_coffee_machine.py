water = 400
milk = 540
coffee = 120
cups = 9
cash = 550

def print_resource():
    print("The coffee machine has:\n", water, " of water\n", milk, " of milk\n", coffee, " of coffee beans\n", cups,
          " of disposable cups\n", "$", cash, " of money")

def buy():
    order = ""
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    try:
      order = int(input())
    except ValueError:
          pass
    global water, coffee, milk, cups, cash

    if cups < 1:
        print("Sorry, not enough cup!")

    if order == 1:
        if water // 250 < 1:
            print("Sorry, not enough water!")
        elif coffee // 16 < 1:
            print("Sorry, not enough coffee!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 250
            coffee -= 16
            cups -= 1
            cash += 4
    elif order == 2:
        if water // 350 < 1:
            print("Sorry, not enough water!")
        elif milk // 75 < 1:
            print("Sorry, not enough milk!")
        elif coffee // 20 < 1:
            print("Sorry, not enough coffee!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            coffee -= 20
            cups -= 1
            cash += 7
    elif order == 3:
        if water // 200 < 1:
            print("Sorry, not enough water!")
        if milk // 100 < 1:
            print("Sorry, not enough milk!")
        if coffee // 12 < 1:
            print("Sorry, not enough coffee!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            cups -= 1
            coffee -= 12
            cash += 6

def fill():
    global water, coffee, milk, cups, cash
    print("Write how many ml of water do you want to add:", )
    fill_water = int(input())
    print("Write how many ml of milk do you want to add:")
    fill_milk = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    fill_coffee = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    fill_cups = int(input())
    water += fill_water
    milk += fill_milk
    coffee += fill_coffee
    cups += fill_cups

def take():
    global water, coffee, milk, cups, cash
    print("I gave you $", cash)
    cash -= cash
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        print_resource()
    elif action == "exit":
        exit()
    elif action == "back":
        continue
  
      
      

      

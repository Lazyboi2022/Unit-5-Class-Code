'''
Name: Roddick Jensen
Date: 1/21/25
Description: This is a text adventure game called The Peoples dream about a day in the life of someone who lives under communism
and tries to find their way to safty.
'''

import random
points= 0
#important variables
HP = 10
IQ = 100
money = 10
hunger = 5
SC = 50 #social credit
neighbor = 0
safe = 0
snitch = 0
def Update_stats():
    #displays all your stats
    print(f"\nHP:{HP}\nIQ: {IQ}\nMoney: {money}\nHunger:{hunger}\nSocial Credit:{SC}\n")

def game_over(points):
    # used to give point total after multiplying and adding scoring elements
    points = SC + hunger* 5 + money *.5 + IQ*10 + safe*250
    print(f"GAME OVER\n{points} Points!")
    return points

def intro_art(): # art to start the game off
    print("""XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+:;XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx::+XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;:::::::xXXXXXXXXXX+:::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+::::::::::XXXXXXXXXXXX;:::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+::::::::::XXXXXXXXXXXXXXXX:::;XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX::::::::::XXXXXXXXXXXXXXXXXXX::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:::::::::::::xXXXXXXXXXXXXXXXXXX::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+:::::::x::::::XXXXXXXXXXXXXXXXXx::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+:::xXXXX::::::XXXXXXXXXXXXXXXX:::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxXXXXXXXx::::::XXXXXXXXXXXXXXX::::;XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+::::::XXXXXXXXXXXXX:::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;::::::XXXXXXXXXXX:::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX::::::;XXXXXXXXX:::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX::::::+XXXXXXX:::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX::::::xXXXX:::::xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx::::::xX::::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;::::+XXXXXXXXXXXXX+:::::::::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx::::::::::xXXXXXXXXXXXX:::::::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:::::XXX::::::::;+xxx;::::::::::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+::::;XXXXXXX;:::::::::::::::::::::::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+:::::XXXXXXXXXXXXx:::::::::::::xXX+:::::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;:::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;:::::;XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+:::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX::::XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX""")



def waking_up(): #the actions someone takes when they wake up
    global SC #collects global variable
    print("you wake up, the sounds of car horns and the smell of smog breaks into your appartment as the sun begins its red dawn")
    while True:
        Waking_opt = int(input(f" Do you want to: " "\n1.) Solute the supreme Leader" "\n2.) Refuse \n"))
        if Waking_opt == 1:
            print("\nYou solute the picture of the Supreme Leader. You could've sworn one of his eyes just moved\n")
            Update_stats() 
            break
        elif Waking_opt == 2: # causes massive SC loss
            print(f"\nThe eyes of our leader's portrait seems to lock onto you\n -100 Social Credit\n")
            SC -= 100
            Update_stats()
            break #ends loops
        else:  # the default action for invalid inputs
            print("out of habit you solute our Glorious Leader\n")
            Update_stats()
            break
    print(f"You get up, time to get ready for the day\n")
    return SC #returns stats to finction
   
   
def appartment_Z1():
    dressed = 0 #setting up dressed with a value, it only is needed for this function unlike the others
    global SC, hunger, IQ
    Luck = random.randint(1,10) #goes through different events each playthrough
    while True:
        Z1_opt = int(input(f" What to do? " "\n1.) eat breakfast" "\n2.) get dressed \n3.) watch TV\n4.)Head out\n"))
        if Z1_opt == 1:
            #if user choses 1
            if Luck <= 3: #if you are unlucky you lose hunger due to lack of food
                print("\nyou check the pantry, you have no food...")
                print("-1 Hunger\n")
                hunger -= 1
                Update_stats()
                
            else: #if you are lucky you get this
                print("\nyou have state provided cereal! Flavor: Communist Crunch\n")
                hunger += 5
                print(f"yummers. +5 hunger")
                Update_stats()
            continue    
       
        elif Z1_opt == 2: #user choses option 2
            print("\nyou change out of your red pajamas and into work clothes. the parties symbol sewn to your jacket\n")
            dressed = 1 #updates dressed to show you dressed
            Update_stats()
        
        elif Z1_opt == 3: #option 3
            if Luck > 5: # 50% chance to get this option
                print("\nYou watch the daily propaganda broadcast, Its your favorite\n")
                SC += 5
                IQ -= 10
                print("\n+5 Social credit\n-10 IQ\n")
                Update_stats()
                
            else: #50% chance to awtch this show
                 print("\nYou watch The hit show: Big Brother. You see our glorious leader save a poor old lady form being robed by capitalists. Our leader is such a great guy\n")
                 SC += 10
                 IQ -= 15
                 print("\n+5 Social credit\n-10 IQ\n")
                 Update_stats()
            continue
        
        elif Z1_opt == 4: #option to move on to the next level
            if dressed == 1:
                print("\nYou put on a coat and open the door\n")
                Update_stats()
                break
            else: #cant go if they arent dressed
                print("\nYou cant go out in those, get dressed!\n")
        else: 
            print("invalid input")
               
    return SC , hunger , IQ #returns all stats to global
    
    
def neighbor(SC, neighbor): #neighbor interaction
    Luck = random.randint(1,10) #goes through different events each playthrough
    if Luck == 1:
        print(" you see your neighbor\nthey dont greet you by blessing our country\n")
        neighbor = 1 #sets the value of your ability to snitch on your neighbor
        
    else: #if you have a good neighbor
        print("you see your neighbor")
        greet = int(input("\ndo you:\n1.) Greet them\n2.) Ignore them\n"))
        
        if greet == 1: #if you greet them
            print("Glory to Velandria.\n+10 Social Credit\n")
            SC += 10
            Update_stats()
        elif greet == 2: #if you ignore them
            print("'Glory to Velandria!' they say to you. you ignored them\n-10 Social Credit\n")
            SC -= 10
            Update_stats()
    return SC, neighbor #returns stats to global
    
    
def home_Z3(): #needs to be up here so the next function can call it
        # takes a players choice from finale to decide their choice, with going to bed ending the game
            global SC, hunger
            while True: #keeps it going until they go to bed
                finale = int(input("now that its night its time to:\n1.) Watch TV\n2.) eat dinner\n3.) Go to bed\n"))
                if finale == 1:
                   #1 to watch TV
                    print("We are winning the war for the motherland, our hand is strong and ste-\nyou dont have the attention span for that\n+10 Social Credit\n")
                    SC += 10
                    Update_stats()
                    continue
                
                elif finale == 2:
                   #2 to eat dinner
                    print("you eat some soup and bread. Its not good but its better than nothing\n+10 Hunger\n")
                    hunger += 10
                    Update_stats()
                    continue
                
                elif finale == 3:
                    #3 to go to bed
                    print("You get into bed, ready to have another amazing state provided day tommorow.\n")
                    game_over(points)
                    break
                
                else:  #lets player retry if they misinput an option
                    print("invalid input, Please try again\n")
                    continue
            
            
def outside_Z2(): #the big one
    print("The cold crisp air hits you. where will you go?\n")
    global SC, hunger, IQ, money, HP, safe, snitch
    Luck = random.randint(1,10)
    while True:
        where = int(input("1.) Work\n2.) The Market\n3.) Government truth booth\n4.) The Farm\n5.) The Border\n6.) Home\n"))
        
        if where == 1: #if you work
            print("you walk into the factory. Working for what feels like days\n")
            work = int(input("do you\n1.) Keep working\n2.) Go home\n")) #gives the user choice
            
            if work == 1:  #lets you work
                print("you work for a few more hours, you begin to feel sore so you step outside for a moment\n+25 social credit\n -1 HP\n-1 IQ")
                IQ -= 1
                SC += 25
                HP -= 1
                Update_stats()
                continue
                if HP == 0: #if you take to much damage, game over
                    print("you fall over in exhaustion\n")
                    game_over(points)
                    break 
                   
            elif work == 2: #calls the function to bring you home
                home_Z3() #home, zone 3
            else:
                print("its been a long day, you should probably head back\n") #defaults the user to going home
                home_Z3()
            
        elif where ==2: #takes you to the market
            Luck = random.randint(1,10)
            print('you look around the market. There’s a massive line wrapping around the bread shop\n')
            buy = int(input("What would you like to buy?\n1.) New clothes\n2.) Bread\n3.) Medicine\n4.) Go back\n"))
            
            if buy == 1: #choice
                print("you look through the selection.\nIts all the same. -5$\n")
                money -= 5
                Update_stats()
                
            elif buy == 2: #choice
                print("you wait in the line  for hours\n")
                
                if Luck > 4: #random event
                    print("you made it to the end of the line, you buy bread\n -5$\n+5 Hunger\n")
                    money -=5
                    hunger +=5
                    Update_stats()
                    
                    if money < 0: #if your broke
                        print("State officials pull up in a black car")
                        game_over(points)
                        break
                
                else: # other end of random event
                    print("you sit in the line for a few hours. the shop closes before you make it halfway there\non your way back you find a dollar \n+1$\n")
                    money += 1
                    Update_stats()
                    
            elif buy == 3: #option
            
                if Luck > 7: #chance
                    print("you walked into the pharmacy, they gave you the medicine you requested free of charge\n +5 HP\n")
                    HP += 5
                else: #chance
                    print("You buy some medicine. +5 HP\n -10 dollars\n")
                    HP += 5
                    money -= 10
                    if money < 0:
                        print("State officials pull up in a black car\n")
                        game_over(points)
                        break
            elif buy == 4: #option
                print("you walk back\n")
                
            else: #lets users invalid inputs try again
                print("Invalid input, try again")
                continue
            
        elif where ==3: #choice
            if neighbor == 0: #choice based off cirumstances
                print("you have nothing to talk about, so you head back\n")
                
            else: #choice based off circumstances
                print("you snitch on your neighbor, she didnt greet you with patriotism as legaly required. +75 Social Credit")
                SC += 75
                snitch = 1
                Update_stats()
        
        elif where ==4: #if you want to go to the farm
            print("you take a walk by the farm, overlooking the animals. It seems all animals are equal, but some animals are more equal than others.\n*you just had an original thought*\n+5 IQ\n")
            
            if Luck > 8: #if you are lucky
                print("you find a book in the dirt, you decide to read some: 'Did you know paper burns at 451 fahrenheit'\n you cant be seen with this, you discard it\n+10 IQ\n-5 social credit\n")
                IQ += 10
                SC -= 5
                Update_stats()
                
        elif where ==5: #if you chose to go to the border
            choice = int(input("you approach the border, what are you doing here?\n1.) Nothing\n2.) Bribe a guard\n3.) Run for it\n"))
            
            if choice == 1: #choice
                Update_stats()    
                pass #does nothing
            
            elif choice == 2: #choice
                if money == 10 and Luck > 3:
                    print("the gaurd let you into the other side, you run through the forest and make it to the nearby country, they let you seek refuge.\n")
                    safe = 1
                    game_over(points)
                    break
                else:
                    print("They didnt find it very amusing\n")
                    game_over(points)
                    break
            
            elif choice == 3: #choice
                
                if Luck > 7: #chance
                    print("you run as fast as you can twards the horizon. you just manage to make it. far away from your country you sit to take a break, watching the sun rise on a new chapter on your life.\n")
                    safe = 1
                    game_over(points)
                    break
                else: #chance
                    print("the gaurd caught you")
                    game_over(points)
                    break
            else: #misinput
                ("Dont just stand there, do somthing!")
    
        elif where ==6: #chose to go home
            
            if snitch == 1:
                print("you go to unlock your door. your neighbors door has caution tape all over it")
                home_Z3()
            
            else:
                print("you unlock your door and enter your state provided apartment")
                home_Z3()
        
    else: # if you missinput on where to go
        print("you should probably go to work")
        print("you walk into the factory you work at working for what feels like hours")
        work = int(input("do you\n1.) Keep working\n2.) Go home"))
        
        if work == 1:
            print("you work for a few mor hours, you begin to feel sore\n +25 social credit\n -1 HP\n-1 IQ")
            IQ -= 1
            SC += 25
            HP -= 1
            
            if HP == 0:
                print("you fall over in exhaustion")
                game_over(points)
                
            elif work == 2:
                home_Z3()
            
    return SC, HP, IQ, hunger, safe, snitch
        
        
def Main(): #function that accually plays the game
    name = str(input("what is your name? "))
    description = str(input("Describe yourself "))
    print(f"\nWow! what an incredible character.\nUnfortunately we dont chose who we are in this world, {name}")
    while True:
        SC = waking_up()
        SC, hunger, IQ = appartment_Z1()
        if SC <= 0:
                print(f"The men in black stand outside your door. 'Hello there, {name}'" )
                game_over(points)
                break
        else:
            print("You walk outside your appartment,",end = "")
        neighbor(SC, neighbor)
        SC, hunger, IQ, HP, safe, snitch = outside_Z2()
#play the game
print("Welcome Commrade, to The Peoples Dream")
print(intro_art())
Main()

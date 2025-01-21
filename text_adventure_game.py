import random
import time
points= 0

HP = 10
IQ = 100
money = 10
hunger = 5
SC = 50 #social credit
neigh = 0


def Update_stats():
    print(f"\nHP:{HP}\nIQ: {IQ}\nMoney: {money}\nHunger:{hunger}\nSocial Credit:{SC}\n")

def game_over():
    points = SC + hunger* 5 + money *.5 + IQ*10
    print(f"{points} Points!")
    return points

def waking_up():
    global SC
   # print()
    while True:
        Waking_opt = int(input(f" Do you want to: " "\n1.) Solute the supreme Leader" "\n2.) Refuse \n"))
        if Waking_opt == 1:
            print("\nYou solute the picture of the Supreme Leader. You could've sworn one of his eyes just moved\n")
            Update_stats()
            break
        elif Waking_opt == 2:
            print(f"\nThe eyes of our leader portrait seems to lock onto you\n -100 Social Credit")
            SC -= 100
            Update_stats()
            break
        else:
            print("out of habit you solute our Glorious Leader\n")
            Update_stats()
            break
    print(f"You get up, time to get ready for the day\n") ###################################################
    return SC
   
   
def appartment_Z1():
    #hunger = hunger
    
    dressed = 0
    global SC, hunger, IQ
    Luck = random.randint(1,10)
    #IQ = IQ
    #SC = SC
    while True:
        Z1_opt = int(input(f" What to do? " "\n1.) eat breakfast" "\n2.) get dressed \n3.) watch TV\n4.)Head out\n"))
        if Z1_opt == 1:
            
            if Luck <= 3:
                print("\nyou check the pantry, you have no food...")############################################
                #time.sleep(.5)
              
                print("-1 Hunger")
                hunger -= 1
                #return hunger
                Update_stats()
                
            else:
                print("\nyou have state provided cereal! Flavor: Communist Crunch")
                hunger += 5
                print(f"yummers. +5 hunger")
                #return hunger
                Update_stats()
                #return hunger
            continue    
        elif Z1_opt == 2:
            print("\nyou change out of your red pajamas and into work clothes. the parties symbol sewn to your jacket\n")
            dressed = 1
            #if IQ =< 30:
             #   print("uh, How do we do this again?")
            #continue
            Update_stats()
        elif Z1_opt == 3:
            if Luck > 5:
                print("\nYou watch the daily propaganda broadcast, Its your favorite")
                SC += 5
                IQ -= 10
                print("\n+5 Social credit\n-10 IQ")
                #return SC
                #return IQ
                Update_stats()
                
            else:
                 print("\nYou watch The hit show: Big Brother. You see our glorious leader save a poor old lady form being robed by capitalists. Our leader is such a great guy")
                 SC += 10
                 IQ -= 15
                 print("\n+5 Social credit\n-10 IQ")
                 #return SC
                 #return IQ
            continue
        
        elif Z1_opt == 4:
            if dressed == 1:
                print("\nYou put on a coat and open the door ")
                break
            else:
                print("\nYou cant go out in those, get dressed!")
        else: 
            print("invalid input")
               # continue
    return SC , hunger , IQ
    
def neighbor():
    Luck = random.randint(1,10)
    global SC
    global neigh
    if Luck == 1:
        print(" you see your neighbor\nthey dont greet you by blessing the Leader ")
        neig = 1
        return neigh
    else:
        print("you see your neighbor")
        greet = int(input("\ndo you:\n1.) Greet them\n2.) Ignore them"))
        if greet == 1:
            print("Glory to Velandria\n+10 Social Credit")
            SC += 10
            
        elif greet == 2:
            print("'Glory to Velandria!' they say to you. you ignored them\n-10 Social Credit")
            SC -= 10
            
    return SC
            
            
def outside_Z2():
    print("The cold crisp air hits you. where will you go?")
    global SC, hunger, IQ, money, HP
    
    where = int(input("1.) Work\n2.) The Market\n3.) Government truth booth\n4.) The Farm\n5.) The Boarder\n6.) Home"))
    if where == 1:
        print("you walk into the factory you work at working for what feels like hours")
        work = int(input("do you\n1.) Keep working\n2.) Go home"))
        if work == 1:
            print("you work for a few mor hours, you begin to feel sore\n +25 social credit\n -1 HP\n-1 IQ")
            IQ -= 1
            SC += 25
            HP -= 1
            if HP == 0:
                print("you fall over in exhaustion")
                game_over()
            break
        else:
            print("its been a long day, you should probably head back")
            break
            
    elif where ==2:
        Luck = random.randint(1,10)
        print('you look around the market. There’s a massive line wrapping around the bread shop')
        buy = int(input("What would you like to buy?\n1.) New clothes\n2.) Bread\n3.) Medicine\n4.) Go back"))
        if buy == 1:
            print("you look through the selection.\nIts all the same. -5$")
            money -= 5
        elif buy == 2:
            print("you wait in the line  for hours")
            if Luck > 4:
                print("you made it to the end of the line, you buy bread\n -5$\n+5 Hunger")
            else:
                print("you sit in the line for a few hours. the shop closes before you make it halfway there\non your way back you find a dollar")
            
            
            
            
    elif where ==3:
        
    elif where ==4:
        
    elif where ==5:
        
    elif where ==6:
        
    else:
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
                game_over()
            break
    return SC, HP, IQ, hunger
        
        
        
SC = waking_up()
Update_stats()
SC, hunger, IQ = appartment_Z1()
Update_stats()
if SC <= 0:
        print("The men in black stand outside your door a bag was thrown over your head. you seem to get very tired." )
        game_over()
else:
    print("You walk outside your appartment,",end = "")
neighbor()
Update_stats()

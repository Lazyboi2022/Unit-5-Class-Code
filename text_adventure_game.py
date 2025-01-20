import random
import time
points= 0

HP = 10
IQ = 100
money = 10
hunger = 5
SC = 50 #social credit



def Update_stats():
    print(f"HP:{HP}\nIQ: {IQ}\nMoney: {money}\nHunger:{hunger}\nSocial Credit:{SC}")

def game_over(points):
    points = SC + hunger* 5 + money *.5 + IQ*10
    print(f"{points} Points!")
    return points

def waking_up(SC):
   # print("The air is thick with smog, a grey oppressive blanket that filters out the sun and makes the sky look perpetually overcast. Your lungs sting as you take a shallow breath, but it’s a routine discomfort one that everyone endures. The hum of machinery fills the background, the noise of factories working overtime, engines revving, and loudspeakers blaring government approved slogans. The walls of your small apartment are bare, save for the occasional state issued propaganda poster extolling the virtues of collective labor and unity. You shuffle out of bed, your joints stiff, the result of long hours at the factory yesterday. your time, like everyone elses, is strictly regulated and measured.") #insperation from gtp
    while True:
        Waking_opt = int(input(f" Do you want to: " "\n1.) Solute the supreme Leader" "\n2.) Refuse \n"))
        if Waking_opt == 1:
            print("You solute the picture of the Supreme Leader. You could've sworn one of his eyes just moved\n")
            break
        elif Waking_opt == 2:
            print("Big Brother did not like that\n")
            SC -= 100
            
            break
        else:
            print("out of habit you solute our Glorious Leader\n")
            break
    print(f"You get up, time to get ready for the day\n {SC}") ###################################################
    return SC
   
   
def appartment_Z1(SC,hunger,IQ):
    #hunger = hunger
    dressed = 0
    Luck = random.randint(1,10)
    #IQ = IQ
    #SC = SC
    while True:
        Z1_opt = int(input(f" What to do? " "\n1.) eat breakfast" "\n2.) get dressed \n3.) watch TV\n4.)Head out\n"))
        if Z1_opt == 1:
            
            if Luck <= 3:
                print("you check the pantry, you have no food", end="")############################################
                #time.sleep(.5)
                for i in range(3):
                    
                    print(".",end ="")
                hunger -= 1
                #return hunger
                continue
            else:
                print("you have state provided cereal! Flavor: Communist Crunch")
                hunger += 5
                print(f"yummers. +5 hunger")
                #return hunger
                
        elif Z1_opt == 2:
            print("you change out of your red pajamas and into work clothes. the parties symbol sewn to your jacket\n")
            dressed = 1
            #if IQ =< 30:
             #   print("uh, How do we do this again?")
            #continue
        elif Z1_opt == 3:
            if Luck > 5:
                print("You watch the daily propaganda broadcast, Its your favorite")
                SC += 5
                IQ -= 10
                #return SC
                #return IQ
                continue
            else:
                 print("You watch The hit show: Big Brother. You see our glorious leader save a poor old lady form being robed by capitalists. Our leader is such a great guy")
                 SC += 10
                 IQ -= 15
                 #return SC
                 #return IQ
                 continue
        elif Z1_opt == 4:
            if dressed == 1:
                print("You put on a coat and open the door ")
                if SC <= 0:
                    print("You open the door, The men in black stand outside your door a bag was thrown over your head. you seem to get very tired." )
                    game_over(points)
                else:
                    print("*Outside Zone 2*")
                    break
            else:
                print("You cant go out in those, get dressed!")
        else: 
            print("invalid input")
               # continue
    return SC , hunger , IQ



waking_up(SC)
appartment_Z1(SC,hunger,IQ)
Update_stats()
if SC <= 0:
    print("You open the door, The men in black stand outside your door a bag was thrown over your head. you seem to get very tired." )
    game_over(points)
else:
    print("*Outside Zone 2*")

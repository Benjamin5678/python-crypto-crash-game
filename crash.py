from random import random
from time import sleep

#https://youtu.be/F1HA7e3acSI
def get_multiplier():
    multiplier = 0.01 + 0.99/random()
    return multiplier

def animation(fail, multiplier, bet_cashout):
    if(fail):
        print("Crash!!!")
        return
    
    animated_cashout = False
    animated_multiplier = 1
    
    while(animated_multiplier * 1.05 < multiplier):
        animated_multiplier = animated_multiplier * 1.05
        
        if((animated_multiplier > bet_cashout) & (animated_cashout == False)):
            print("---Cash out!---")
            animated_cashout = True

        print(animated_multiplier)
        sleep(0.1)
    
    print(multiplier)
    print("CRASH!!!")

cash = float(input("What do you want your starting cash to be? -> "))

while(cash > 0):
    print("\n--New Game--")
    print("Cash =", cash)
    bet_amount = float(input("How much do you want to bet? -> "))
    bet_cashout = float(input("What multiplier do you want to cash out on? -> "))

    cash = cash - bet_amount
    multiplier = get_multiplier()
    fail = random() < 0.03

    animation(fail, multiplier, bet_cashout)

    if(fail):
        print("Sorry, the rocket ship didnt make it off the launch pad. You lost your bet.")
        continue

    if(multiplier < bet_cashout):
        print("Sorry, the rocket ship only made it to", str(multiplier) + ". You lost your bet.")
        continue

    cash = cash + bet_amount*bet_cashout

    print("You won the bet!")
    print("The rocket ship made it to", str(multiplier) + ". You cashed out at", str(bet_cashout) + ".")
import random

def D10(): 
    return random.randrange(10)
def D25():
    return random.randrange(10,25)
def D50():
    return random.randrange(26,50)
def D100():
    return random.randrange(51,100)
def D200():
    return random.randrange(101,200)

def chooseDice():
    print("Please select the dice you'd like to roll")
    print("The options are 10, 25, 50, 100 and 200")
    dice = int(input(">"))
    if dice == 10:
        print("Rolling dice 10..")
        print("You got",D10())
    elif dice == 25:
        print("Rolling dice 25..")
        print("You got",D25())
    elif dice == 50:
        print("Rolling dice 50..")
        print("You got",D50())
    elif dice == 100:
        print("Rolling dice 100..")
        print("You got",D100())
    elif dice == 200:
        print("Rolling dice 200..")
        print("You got",D200())
    else:
        print("That's not a valid dice!") 
        
chooseDice()

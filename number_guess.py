import random
random.seed(a=None, version=2)

#This is where the upper and lower bounds are set and checked
lower = input("set lower bound: ")
try:
   num = int(lower)
   number = True
except ValueError:
    print("that doesn't only contain numbers")
    number = False

while number == False:
    lower = input("set lower bound: ")
    try:
       num = int(lower)
       number = True
    except ValueError:
        print("that doesn't only contain numbers")
        number = False
        
higher = input("set higher bound: ")
try:
   num = int(higher)
   number = True
except ValueError:
    print("that doesn't only contain numbers")
    number = False

while number == False:
    higher = input("set lower bound: ")
    try:
       num = int(higher)
       number = True
    except ValueError:
        print("that doesn't only contain numbers")
        number = False
        
#the guessing begins
secret = random.randint(int(lower), int(higher))
guess =  0
number = False
while number == False:
    try:
        num = int(guess)
        number = True
    except ValueError:
        print("that doesn't only contain numbers")
        number = False

    else:
        if number == True:
            while not secret == int(guess):
                guess = input("What is your guess? ")
                if not str(guess) == str(secret):
                    if int(guess) < int(secret):
                        print('too low!')
                    if int(secret) < int(guess):
                        print('too high!')
                else:
                    print ('you win! run code to play again')
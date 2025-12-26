import random
var= random.randint(1,20)
print("Welcome to the guessing game!")
while True:
    guess= int(input("Enter your number/guess"))
    if guess < var:
        print("Your guess is lower")
    elif guess > var:
        print("Your guess is bigger")
    else:
        print("Your guess is correct")
        break
    
    

 


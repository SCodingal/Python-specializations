import random
import time

number=random.randint(1,100)

def intro():
    print("May I ask you for your name?")

    global name 
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 100")
    
    if(number%2==0):
        x='even'
    else:
        x='odd'
        print("\nThis is an {} number".format(x))
        time.sleep(.5)
        print("Go ahead. Take a guess!")

    def pick():
        guessesTaken = 0

        while guessesTaken < 6:
            time.sleep(.25)
            enter=input("Guess:")
            try:
               guess = int(enter)

            if guess<=100 and guess>=1
               guessesTaken=guessesTaken+1
            if guessesTaken<6:
                
            if guess<number:
                print("The gues of the number that you have is too low")
            if guess>number:
                print("The gues of the number that you have is too high")
            if guess != number:
                time.sleep(.5)
                print('Try AGAIN!')
            if guess==number:
                break
        if guess>100 or guess<1:
            print("The number isnt in th range!")
            time.sleep(.25)
            print("Please enter a number between 1 and 100")

    except:
print("I don't think that "+enter+"is a proper number. Yh sorry...")

guess==number:
guessesTaken=str(guessesTaken)
print('Nice,{}! You got it, in{}guesses!'.format(name,guessesTaken))

guess !=number:
print('Nope. The numbe I was thinkign of was'+str(number))





            

            

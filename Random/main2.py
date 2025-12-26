import random
var2= ["Rock", "Paper","Scissors"]
print("Welcome to the rock, paper scissors game")
while True:
    cc=random.choice(var2)
    choice= str(input("Enter your choice: "))
    print("computer choice" , cc)
    if cc == "Rock":
        if choice == "Rock":
            print("Tie")
        elif choice == "Paper":
            print("You win")
        else:
            print("Computer wins")
    if cc == "Paper":
        if choice == "Rock":
            print("Computer wins")
        elif choice == "Paper":
            print("Tie")
        else:
            print("You win")
    if cc == "Scissors":
        if choice == "Rock":
            print("You win")
        elif choice == "Paper":
            print("Computer win")
        else:
            print("Tie")    
    replay= str(input("Do you want to play again?"))
    if replay == "no":
        print("Thank you for playing")
        break
    else:
        print("NEXT ROUND")







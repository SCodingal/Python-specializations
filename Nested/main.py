medical_cause= input("Did you have a medical cause Y or N:")

atten=int(input("Enter the attendence of the student:"))

if medical_cause == 'Y':
    print(" You are allowed")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("Not allowed")


print("Select your ride:")
print("1. Bike")
print("2. Car")
 
choice= int(input("Enter your choice:"))

if (choice == 1):
    print("What type of bike?")
    print("1.Scooty\n")
    print("2. Scooter\n")

    choice2 =int(input("Enter your choice2:"))
    if choice2==1:
        print("You have selected a scooty")
    else:
        print("You have selected a scooter")

elif (choice==2):
    print("Which type of car?")
    print("1.Sedan")
    print("2. XUV")

    choice3=int(input("Enter your choice3"))
    if choice3 ==1:
        print("You chose a Sedan")
    else:
        print("You chise a XUV")
    
else:
    print("Invalid option")    

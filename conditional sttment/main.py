#Program to check positive or negative number
number= int(input("Enter a number"))
if (number>0):
    print("Its a positive number'+'")
elif number==0:
    print("Its a neutral number")   
else:
    print("Its a negative number'-'")

# program to check odd or even number
number1= int(input("Enter a number"))
if (number1%2==0):
    print("Its an even number")
else:
    print(" Its an odd number")

# Program to check eligibility to vote
age= int(input("Enter your age:"))
if (age>=18):
    print("You are eligible to vote!")
else:
    print(" Your not eligilbe to vot! Go back home and study!")
# Program to say profit or loss
cp=int(input("Enter the cost of the item:"))
sp=int(input("Enter the selling price of the item:"))
if (cp>sp):
    print("Its a loss")
else:
    print("Its a profit! Great u havet lost much money!")
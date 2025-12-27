valid = False
while not valid:
    try:
        n=int(input("Enter your age: "))
        if n %2==0:
          print("Well your age is even")
          break
        else:
          print("nope sorry, age is odd")
          

    
    except ValueError:
        print("Invalid")


    
    

    
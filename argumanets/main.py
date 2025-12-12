def total_calc(bill_amount, tip_perc):
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")

total_calc(150,20)

def cube(number):
    return number*number*number
def by_three(number):
    if number %3 ==0:
     return cube(number)
    else:
       return False
print(by_three(9))
print(by_three(3))

def factorial(x):
   
   if x==0 or x==1:
    return 1
   
   else:
      return x*factorial(x-1)
   
print(factorial.__doc__)
print("the factorial of 0:" , factorial(0))




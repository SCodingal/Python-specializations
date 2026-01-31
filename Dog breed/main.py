
class Yorkshire:
   species="dog"
   def __init__(self,name,age): 
      self.name=name
      self.age=age

kim=Yorkshire("Kim",10)

print("kim is a {}".format(kim.species))


print("{} is {} years old".format(kim.name, kim.age))




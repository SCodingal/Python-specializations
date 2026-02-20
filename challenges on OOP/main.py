class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if(self.a<other.a):
            return "obi1 s less than obi2"
        else:
            return "obi2 is less than obi1"
    def __eq__(self,other):
        if(self.a == other.a):
           return "both are equal"
        else:
            return "Not equal"

    def __gt__(self,other):
        if(self.a<other.a):
           return "obi1 is greater than obi2"
        else:
            return "obi2 is greater than obi1"
        

obi1=A(2)
obi2=A(3)
print("Passes Values:", obi1.a, obi2.a)
print(obi1 < obi2)

obi3=A(4)
obi4=A(4)
print("Passes Values:", obi3.a, obi4.a)

obi5=A(10)
obi6=A(8)
print("Passes Values:", obi5.a, obi6.a)
print(obi5 > obi6)

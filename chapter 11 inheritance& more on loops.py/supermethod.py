class Employee:
    def __init__(self):
        print("constructor of Employee")
    a= 1

class Programmer(Employee):
    def __init__(self):
        print("constructor of Programmer")
    b= 2


class Manager(Programmer):
    def __init__(self):
        super().__init__()# run also parent constructor
        print("constructor of Manager")
    c= 3
    
# o=  Employee()
# print(o.a)

# o= Programmer()
# print(o.a,o.b)
   
object = Manager()# manager class has all three class value 
print(object.a,object.b,object.c)    

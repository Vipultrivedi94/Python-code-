class Employee:
    a= 1

class Programmer(Employee):
    b= 2


class Manager(Programmer):
    c= 3
    
    
object = Manager()# manager class has all three class value 
print(object.a)    
print(object.b)
print(object.c)

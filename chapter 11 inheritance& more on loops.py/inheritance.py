class Employee:# this is parent or base class
    company = "itc"
    def show(self):
        print(f"the name of the employee is {self.name}")
        
        
class Programmer(Employee):# inheritance class whichhas all employee class and all programmer class work

    company = "itc infotech"
    
    def showlanguage(self):
        print(f"the name of the employee is {self.name}")
        
        
a= Employee()    
b= Programmer()

print(a.company,b.company)    
        
            
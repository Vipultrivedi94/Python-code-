class Employee:# this is parent or base class
    company = "itc"
    def show(self):
        print(f"the name of the employee is {self.name}")
        
class Coder:
    language = "python"
    def printlanguages(self):
        print(f"out of all the languages here is your language {self.language}")
        
    
    
class Programmer(Employee,Coder):# inheritance class whichhas all employee class and all programmer class work

    company = "itc infotech"
    
    def showlanguage(self):
        print(f"the name of the company is {self.company}")
        
        
a= Employee()    
b= Programmer()


b.printlanguages()
b.showlanguage()

        
            
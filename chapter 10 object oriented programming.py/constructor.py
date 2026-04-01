# which function starts double underscore called dunder method 
   
class Employee: # variable of class is always capital 
    
    
    language = "python"
    
    salary = 120000
    
    def __init__ (self,language,salary,name): # dunder method function 
        
        self.name = name
        self.salary= salary
        self.language = language 
        
        
        print("i am creating an object")
    
    
    def greet(self):# make method then give self 
        print("good morning")
        print(f"the language is {self.language }") 
        
        
# create any object then automatically called init dunder method         
    
harry = Employee("python", 130000,"Vipul ")
harry.name = "Harry "# thia is a instant attribute 
print(harry.name ,harry.language,harry.salary)

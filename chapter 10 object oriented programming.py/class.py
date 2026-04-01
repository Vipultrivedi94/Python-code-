# class is a blue print for create a valid object 

class Employee: # variable of class is always capital 
    
    
    language = "python"
    
    salary = 120000
    
    
    def greet(self):# make method then give self 
        print("good morning")
        print(f"the language is {self.language }") 
    
harry = Employee()
harry.name = "Harry "# thia is a instant attribute 
print(harry.name ,harry.language,harry.salary)

harry.greet()    

# language and salary is  class attribute and name is a instants 


class Employee:
    a= 1
    
    # class method use cls instead os self
    
    @classmethod# by class method we use directly class method
    def show(cls):
        print(f"the value of a is {cls.a}")
        
        
        
       
    # def shownoclassmethod(self):
    #     print(f"the value of a is {self.a}")
        
        
e= Employee()
e.a= 45

e.show()
# e.shownoclassmethod()        
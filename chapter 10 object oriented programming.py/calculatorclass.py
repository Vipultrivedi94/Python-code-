class Calculator:
    def __init__(self,a):
        self.a= a
        
    def square(self):
        print(f"the square of a number{self.a} is {self.a* self.a}") 
        
    def cube(self):
        print(f" the cube of a number{self.a} is {self.a*self.a*self.a} ")
        
    def squareroot(self):
        print(f"the squareroot is {self.a**1/2}")
           
           

a= Calculator(4)
a.square()         
a.cube()
a.squareroot()
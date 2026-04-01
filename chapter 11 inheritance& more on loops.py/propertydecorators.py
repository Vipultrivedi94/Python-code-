
class Employee:
    def __init__(self):
        print("constructor of Employee")
    a= 1


@property
def name(self):
    
    return f"{self.fname} {self.lname}"

@name.setter

def name(self,value):
    self.fname= value.split( " ")[ 0]
    self.lname = value.split( " ")[ 1]
   
   
e= Employee()
e.a = 45

e.name = "harry khan " 
print(e.fname,e.lname)  

e.show()
 




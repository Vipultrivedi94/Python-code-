
from random import randint

class Train:
    
    def __init__(self,trainno):
        self.trainno = trainno
    
    def book(self,fro,to):
        print(f"ticket is booked in train no  {self.trainno} from{fro} to {to} ")
       
    
    def getstatus(self,trainno):
        print(f" train no{self.trainno} is running succesfully ")
    
   
    
    
t=Train(12344)
t.book( " rampur","delhi")
 
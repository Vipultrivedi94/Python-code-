class Programmer:
    company = "microsoft"
    
    def __init__(self,name,salary,pin):
        self.name = name 
        self.salary= salary
        self.pin= pin
    
p= Programmer("Vipul",120000, 242042)
print(p.name,p.salary,p.company)

r= Programmer("rohan",120000,242402)

print(r.name,r.salary,r.pin)
a= int(input("enter number"))
b= int(input("enter number"))
c= int(input("enter number"))

def greatest(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greatest number")
        
    elif(b>c):
        print(f" {b} is greatest number")
        
    else:
        print(f" {c} is greatest number")
        
greatest(a,b,c)                        
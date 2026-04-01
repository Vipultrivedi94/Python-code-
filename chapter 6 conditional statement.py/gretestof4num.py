a= int(input("enter number "))
b= int(input("enter number "))
c= int(input("enter number "))
d= int(input("enter number "))

if(a>b and a>c and a>d):
    print(f"the greatest num is {a}")
    
elif(b>c and b>d):
    print(f"the greatest num is {b}")
    
elif(c>d):
    print(f"the greatest num is {c}")        
    
else :
    print(f"the greatest num is {d}")    
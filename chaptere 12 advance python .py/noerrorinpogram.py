try:
    a= int(input("enter number"))
    b= int(input("enter number"))
    print(a/b)
    
except ZeroDivisionError as v:
    print("divide by zerp is not allowed in python ")
        
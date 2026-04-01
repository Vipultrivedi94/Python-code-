try:
    a= int(input("enter number"))
    print(a)
    
except ValueError as v:
    print("value error please enter integer value ")
    print(v)    
    
except Exception as e:
    print(e)    
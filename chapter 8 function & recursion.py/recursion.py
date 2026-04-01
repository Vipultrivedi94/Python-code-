# recursion calls itself 

# factorial n = n*factorial (n-1)

def factorial(n):
    if(n==0 or n==1):# base case is imp in recursion 
        return 1
    
    else :
        return n*factorial(n-1)

n= int(input("enter number for factorial :"))    
print(f"the factorial of the number{n} is {factorial(n)} ")






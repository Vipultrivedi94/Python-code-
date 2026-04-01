n= int(input("enter number for factorial"))

product = 1

for i in range ( 1,n+1):
    product = product*i
    
print(f" the factorial of {n} is {product}")    
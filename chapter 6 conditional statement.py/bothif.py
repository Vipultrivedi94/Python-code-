a= int(input("enter age"))

# when if statement is true then also check another if condition
if(a%2==0):
    print(f"the number is even {a}")
    
# but when if conidition condition become true then cannot check elif condition 
    
if (a>= 18):
    print("you are eligible to vote")
# give proper indentation(proper space after if,elif and else)
elif(a<0):
    print(f"you are entering invalid age {a}")

elif(a==0):
    print("you enter 0 which is invalid")

else :
    print("you are not eligible to vote")        
def f_to_c(f):
    return (f-32)*5/9

f= int(input("enter fahreinheit value"))

c = f_to_c(f)
print(round(c,2))# give value upto 2 decimal places 
marks1 = int(input("enter 1st marks"))
marks2 = int(input("enter 2nd marks"))
marks3 = int(input("enter 3rd marks"))

total_persentage= (100*(marks1+marks2+marks3))/300


if (total_persentage >= 40 and marks1>=33 and marks2 >= 33 and marks3 >=33):
    print("you are pass ",total_persentage)
    
else :
    print("Try next time ",total_persentage)    
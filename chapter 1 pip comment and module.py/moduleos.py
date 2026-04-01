import os



# Specify the directory you want to list
directory_path = 'whatsapp image'

# LIST ALL FILES AND DIRECTORYS IN THE SPECIFIED PATH

contents = os.listdir(directory_path)

# print each file and directory name 

for item in contents:
    print(item)

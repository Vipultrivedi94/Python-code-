with open("old.txt") as f:
    content = f.read()
    
with open("rename.txt","w") as f:
    f.write(content)    # create file rename.txt same as old.txt
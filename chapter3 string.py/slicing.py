name = "harry"

nameshort = name[0:4] # idx 4 is not include 

print(nameshort)

print(name[ :5])
# same as name[0: 5]

print(name[0: ])

# same as name[0: len(name)]

b = "abcdefghijklmnopqrstuvwxyz"

print(b[0:len(b):4])

print(name.endswith("ry"))

print(name.startswith("Ha"))

print(name.capitalize())

print(name.find("r"))

print(name.replace("r","t"))# replace all accurence of r 

print(len(name))
 


s = { 2,3,4,5,2,3,6,7,8,11}

s.remove(2)# remove all occurence of 2 

print(s)

s.pop()# remove random element of set 
print(s)

# s.clear()# empty the set 
# print(s)

s2= { 2,3,4,5,8,10}
s1= { 2,3,4,7,8,10}

print(s1.union(s2))# give all value but no repetation 

print(s1.intersection(s2))# give common value 

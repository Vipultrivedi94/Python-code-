
# dictionary is a key value pairs in python

d= {} # this is an empty dictionary 

marks = {
    "harry" : 100,
    "Shubham": 90,
    "Rohan": 80
}

print(marks)

# dict is unordered
# it is mutable
# it is indexed
# cannot contain duplicate keys

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"harry": 99})

print(marks)

print(marks.get("Rohan"))# give value of key

print(marks["Rohan"])

print(marks.get("Rohan2"))# give none value
# print(marks["Rohan2"]) give error 

print(len(marks))

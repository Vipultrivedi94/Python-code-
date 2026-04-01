marks = {
    "harry" : 100,
    "Shubham": 90,
    "Rohan": 80
}

print(marks)


print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"harry": 99})

print(marks)

print(marks.get("Rohan"))# give value of key

print(marks["Rohan"])

print(marks.get("Rohan2"))# give none value
# print(marks["Rohan2"]) give error 


dict = {
    "name" : "sampath",
    "age"  : 19,
    "city" : "hyderabad",
    "marks": {
        "science": 85,
        "maths": 90,
        "english": 88
    }
}

print(list(dict["marks"]))
print(list(dict.get("name")))
print(list(dict.keys()))
print(list(dict.values()))
# used to store a collection of key-value pairs where each key is unique with corresponding value 
# for example, to store a collection of people name and age ( key and value seprates by colon :)
#example
person = { "name":"rojay", "age": 25, "city": "btm"}
print(person["name"])
print(person.get("name"))
person["name"] = "rameshor"
print(person["name"]) 
person["mood"] = "harami" # adding new key and value in person dictionary 
print(person)
print(person.keys())
print(person.values())
print(person.items())
person.pop("mood") # Pop is used to remove key and value in dictionary 
print(person)
print("name" in person)
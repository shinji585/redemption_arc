from collections import ChainMap

student = {"name": "Emma", "age": 21}
course = {"subject": "Python", "duration": "3 Months"}
data = ChainMap(student, course) # type: ignore[misc]


print(f"Data without using any method to filter the object: \n{data}\n")


# we have methods like: new_child that add a new child if the key math with the new dict
# we have methods like: maps, parents, keys, values, items, get(key, default), update(...), copy()


print(f"Data by just showing them as a list of dictionaries: \n{data.maps}\n") # this return a list of element that were passed as mappings


# we new child we create a new chainmap with an additional mapping at the begining, this is the form of how we emulate an append or insert method 

new_data = data.new_child({"subject": "react"})


print(f"New data by showing them as a list of dictionaries: \n{new_data.maps}\n")


# if we want to see all unique keys available across the dictionaries in the ChainMap we could do 
print(list(new_data.keys()))

# for see the values 
print(list(new_data.values()))

# we could accessing data by index them 
print(new_data["subject"])
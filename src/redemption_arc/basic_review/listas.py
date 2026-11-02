# python list are used to store multiple items in a single variable. Duplicate values are allowed in a list, and elements can be of different types: for example, you can have both numeric and string data in a python list


a = ["food", "bus", "apple", "queen"]
print(a)

mylist = ["bus", "apple", {"Samuel", 21, "Colombian"}, 10]

print(mylist)


# we can also loop list

for element in mylist:
    print(element)


# and also we can access to elements by their positions
print(mylist[-1])


# could also access to the elements and their positions
for postion, value in enumerate(mylist):
    print(f"""
      Value position: {postion}
      Value: {value}
    """)


# we could also ignore the values that enumerates returns passing _


# we could also add values by +=


mylist += ["samuel"]

print(mylist)  # and it will add the value at the last position

# we have two types of list: ordered the elements are ordered in a sequence in which they are specified in the list at the time of defining them, and we have Dynamic: the list is dynamic. it can grow or shrink as needed by adding or removing list items


print(
    mylist.remove("samuel")
)  # remove retunrs None when the value was already eliminated

# sequence data types are used to store multiple values in a single variables in an organzied and efficient way
# There are four basic sequence types: string, range, list, and tuples, and ¿sets?
# what is a sequence?: A sequence organizes elements in a order. This allows you to access elements by their position, or index.
# Why isn't a set considered as a sequence?: A set isn't considered a sequence because it store values that are differents and also its behavior follow a mathematical fundamental structure that has its same name


# A string is an immutable sequence of characters represented in single, double, or triple quotes.


# immutable means that once a data type has been assigned some value, it can't be changed. (I think this refer from memory)


# In python a variable can be reassigned to reference another object without modifying the original object


name = "Toji"
print(f"{name}\n")
# we aren't change the inmmutable value store in memory "Toji" we are changing a reference so name isn't any more refering to "Toji" instead now it is refering to "cr7"

name = "CR7"

print(name)


# the 3 forms of use strings


str1 = "Hwllo how are you"
str2 = "Hello how are you"
str3 = """Multiple 
       Strings"""

print(str1)
print(str2)
print(str3)

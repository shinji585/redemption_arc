student_id = "samuel_21"
print(hash(student_id))


example_set = {"and", "python", "data", "structure"}
print(example_set)


example_set_two = {"and", "python", "data", "structure"}
print(example_set_two)

# comparing two sets

print("python" in example_set)
print(f"Lenght set: {len(student_id)}")


# common use sets

x1 = {"data", "structure"}
x2 = {"python", "data", "c", "c++"}


# union
print(x1.union(x2))


# inserction
print(x1.intersection(x2))

# difference between sets
print(x1.difference(x2))


# symetric difference
print(x1 ^ x2)


# subset
print(x1 <= x2)


# another type of set we have is frozenset the only difference between it and sets is that frozenset are inmmutable we can't change them after their creation


x = frozenset(["data", "structure", "python", "java"])

print(x)


# frozenset are useful when we want to have multiple sets in one structure because using normal sets it isn't possible

a11 = frozenset("data")
a12 = frozenset("structure")
a31 = frozenset("python")
x1 = {a11, a12, a31}


print(x1)

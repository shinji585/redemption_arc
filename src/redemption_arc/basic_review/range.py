# the range data type represents an inmmutable sequence of numbers. IT is mainly used in for and while loops
# it returns a senquence of numbers starting from a give number up to a number specific bny the function argument.
# It is used as in the following command:


# range(start, stop, step)

# how it work
print(
    list(range(0, 9, 1))
)  # this print a list of number that start from 0 to 9 with an step of 1
print(range(10))  # this print ten numbers
print(list(range(0, 9, 2)))  # the same as the first print but with a step of 2


# it doesn't count the last number because it is n to n-1
# so if we want that it finish at 9 or create a list of number from 0 to 9 we need to pass an structure like 1, 10
print(list(range(0, 10, 1)))



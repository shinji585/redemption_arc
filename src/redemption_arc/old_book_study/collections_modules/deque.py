import itertools
from collections import deque

dq = deque("ABCD")


print(f"The visual representation of deque is: {dq}")


# deque operations
# deque is a data structure that combine or merge two types of data structure those who follow the principle FIFO and LIFO
# so here every thing could be putted at the start or end of the "list"
# we have methods like, append, appendleft, extend, extendleft, pop, popleft, and one method that is interesting is rotate that moves the last element to the right and others are moved 1 step after their natural position

dq.append("WERT")  # this is adding WERT to the end

print(dq)


dq.appendleft("samuel")  # this is adding samuel at the begining


print(dq)


# we could access elements or iotems by indexing them, but we can't make slicing

print(
    f"Element in the first position and element in the last position: {dq[0]}, {dq[-1]}"
)


# continue with the operations we have things like:


dq.extend(["santiago", "sebastian", "francisco", "martha"])


print(f"deque with extend values: {dq}")


# we also could make the same but by left

dq.extendleft(["ferrari", "real madrid", "bayer munich", "machine learning"])


print(dq)


# we could remove the first ocurrence of a specified value

dq.remove("ferrari")

print(dq)


print(dq.pop())  # remove the last element in the right part
print(dq.popleft())  # remove and return the first element in the left


# with the clear method we are available to remove all the elements
dq.clear()

print(dq)


# we could also count how many time is value inside the deque

dq = deque([x for x in range(1, 10)])

print(dq.count(2))  # it is returning 1 because 2 is just 1 time inside the deque

# rotate is another method that is interesting because it allow to us move elements that are at the end to the right
# it's standart idea is circular move


print(dq)

dq.rotate(1)

print(dq)


# the last method that we have is reverse that reverses the order of elements in the deque


dq.rotate(-1)
dq.reverse()

print(dq)


# the only or simple way to return a slice of a deque in python is by the next form


print(list(itertools.islice(dq, 0, 5)))

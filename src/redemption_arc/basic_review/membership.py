nombres = ["samuel", "santiago", "sebastian"]

# membership allow to us validate if a value is on a sequence by using two operations "in" and "not in"


# exaple of use


if "francisco" not in nombres:
    print("Good Morning MR.Francisco")


if "samuel" in nombres:
    print("Good Morning MR.Samuel")


# here we need to have a clear disctintion that is not confuse "in or not in" with "is and is not"


# in checks membership, while is checks identity


# when we talk about identity, we are talking about to variables refer to the same values at memory


a = [1, 2]
b = [1, 2]

print(
    a is b
)  # this is going to be false because those valeus doesn't have the same reference
print(
    a is not b
)  # this is going to be true because they don't have the same reference in memory


# if we want to express that we could do


a = b

print(
    a is b
)  # this is going to be true because now both are pointing to the same reference


firslist = []
secondlist = []

print(len(firslist))
print(len(secondlist))
print(firslist == secondlist)


# also we have logical operators like and, or , and not


a = 30
b = 20


if a > b > 0 or a > b or b < 0:
    print(f"Hello World {a} is higher than {b}")


if not b > a and a > 0:
    print(f"Hello Wolrd {b} is not higher than {a}")
else:
    print("This isn't a Hello World any more")

import itertools

programming_language_that_love = ("python", "rust", "golang", "typescript")


# we could loop a tuple

for v in programming_language_that_love:
    print(v)


for i, v in enumerate(programming_language_that_love):
    print(f"""
         index {i}: 
            value: {v}
    """)


# we could check if a value is inside it
print("rust" in programming_language_that_love)


# but there are some operations that we can't perform inside a tuple those operations are:
# 1. modify a value inside a tuple (directly), we can remove a value, and we can't add values inside a tuple


# but we have some strategies to do that for example we could concant tuples by adding them or eliminate a value from a tuples by filtring, or reasigning them into a list, the best way for me is to index the tuple


# adding two tuples


# let's say that we have another tuple that contains programming language that I hate
programming_language_that_hate = ("java", "javascript", "php")

# one day I tried all those programming language that I hate and one point of it I started to like them


# how I combine those programming language that I love with the ones that I hate


new_programming_language_that_love = tuple(
    itertools.chain(programming_language_that_love, programming_language_that_hate)
)

print(f"New programming languages that I love: {new_programming_language_that_love}")

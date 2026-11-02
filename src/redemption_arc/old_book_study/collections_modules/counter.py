from collections import Counter

items = ['apple', 'banana', 'apple', 'banana', 'orange', 'apple']

count = Counter(items) # type: ignore[var-annotated]



print(count)

# here we have methods like counter.update that allow to us update a key with a new number of value that is fixed
count.update({'apple': 10}) # this doesn't remove the old 3 it add 10 to that old 3 

print(count)


# we have methods like elements, most_common, and subtract that remove an amount from the total 
{count.subtract({'apple': 5})}
print(f"""
      elements: {list(set(count.elements()))} 
      most_common: {count.most_common()}
      subtract: {count}
      """) 
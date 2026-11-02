import json
from pathlib import Path
from typing import Any, cast

# dictionaries are something special, I know this because most of the time I'm working with them at the backend part so let's go to practice


data: dict[str, Any] = {
    "names": ["samuel", "sebastian", "santiago"],
    "ages": [21, 16, 16],
    "nationalities": ["Canadian", "Colombian", "German"],
    "description": "These people are brother even they were born in differents countries, that is crazy",
}


# we could perfom actions with dictionaries such as:

print("names" in data)  # to check if the key names is inside data
print(data.values())  # returns all the values that data contains
print(data.keys())  # returns all the keys that data contains

result = cast(
    str, data.setdefault("goals", ["Machine Learning Engineer", "Business", "Unknown"])
)  # type: ignore
print(result)


print(len(data))
print(data.get("ages"))
print(data.items())

# we have to method pop one for eliminate a key and its value we are going only use popitem
# print(
#    data.popitem()
# )  # it remove the last key-value pair added in the dictionary and returns it as a tuple

# for merge one dictionary with another. firsttly, it checks whether a key of the second dictionary is present in the first dictionary; the correspoding value is then updated
# if the key is not present in the first dictionary, then the key-value pair is added

print(
    data.update(
        {
            "description": "They are brother that live in Colombian",
            "montly payment": [2000000.25, 125000, 300000],
        }
    )
)


# we could also transform those dictionaries into json and work with them
file_path = Path("output.json")


characters_written = file_path.write_text(json.dumps(data, indent=4))
print(f"Successfully wrote {characters_written} into the file {file_path}")




# let's say we have this 

d2 = {'one':'uno' , 'two':'deux', 'three':'trois', 'four': 'quatre', 'five':
'cinq', 'six':'six'}
d = [k for k, _ in d2.items()]

print(sorted(d2)) # this is ordered alpahbetically


def wordcount(fname):
    try:
        fhname = open(fname)  # noqa: SIM115
    except Exception as e:  # noqa: BLE001
        print(f"File cannot be opened: {e}")
        
    count = {}
    for line in fhname:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else: 
                count[word] += 1
    return count 


def counter(string: str) -> str:
    return (string[len(string) - 1])

print(sorted(d2, key=counter))


print(wordcount(".txt"))
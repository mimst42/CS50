people = [
    {"name": "Harry", "House": "Gryffindor" },
    {"name": "Cho", "House": "Ravenclaw" },
    {"name": "Draco", "House": "Slytherin" }
]

def f(person):
    return person["House"]

# people.sort(key=f)
people.sort(key = lambda person: person["name"])

print(people)
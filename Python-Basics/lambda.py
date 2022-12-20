people = [
    {"name": "Bizimana", "house": "Bonny"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Denise", "house": "Nyarutarama"}
]
#Lambda will rid of the below function:
# def f(person):
#   return person["house"]

people.sort(key=lambda person: person["house"])

print(people)
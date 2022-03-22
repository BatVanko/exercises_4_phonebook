line = input()
phonebook = {}

while not line.isnumeric():
    name, number = line.split("-")
    phonebook [name] = number
    line = input()
searched_people = int(line)

for i in range (searched_people):
    people = input()
    if people not in phonebook:
        print(f"Contact {people} does not exist.")
    else:
        print(f"{people} -> {phonebook[people]}")









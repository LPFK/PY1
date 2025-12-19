for i in [0, 1, 2]:
    print("meow")

for i in range(3):
    print("meow")

for i in range(3):
    print("meow", end=" ")

students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(student)

students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1, students[i])

students = {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor"}
for student in students:
    print(student, students[student], sep=" ")

student = [{"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
{"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
{"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
{"name": "Draco", "house": "Slytherin", "patronus": None}]
for student in student:
    print(student["name"], student["house"], student["patronus"] if student["patronus"] else "No patronus", sep=" | ")

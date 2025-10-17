# 기본 딕셔너리
students = {
    "Hermione" : "Gryffindor",
    "Harry": "Gryffindor",
    "Ron" : "Gryffindor", 
    "Draco" : "slytherin",
}

for student in students :
    print(student, students[student], sep=", ")

# 더 복잡한 구조

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus":"otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus":"Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus":"Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=",")
    
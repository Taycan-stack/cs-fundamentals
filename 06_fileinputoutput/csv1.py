# Comma-Seprated Value (CSV)

# CSV 파일을 일반 텍스트 파일처럼 읽는 방법
# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")



# 변수 두 개로 나누기 (더 깔끔하게 하는 법)    
# split은 리스트를 반환하지만, 리스트로 반환하지 않고 두 변수로 바로 받는 법
# 튜플 인패킹이라는 개념

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")


# 리스트에 저장하고 정렬하기 학생 데이터를 한 번에 정렬해서 보고 싶을 때
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)

# 딕셔너리로 표현하기 (더 구조적으로)
# 리스트는 보기엔 편하지만, 이름과 소속의 관계를 명확히 표현하기엔 딕셔너리가 좋음.

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name" : name, "house" : house} # 이게 딕셔너리
#         students.append(student)

# for student in students:
#     print(f"{student['name']} is in {student['house']}")

# 딕셔너리 리스트 정렬하기
# 딕셔너리 안의 특정 키(name)을 기준으로 정렬하려면
# sorted()에 key 함수를 전달해야 함

# def get_name(student):
#     return student["name"]

# for s in sorted(students, key=get_name):
#     print(f"{s['name']} is in {s['house']}")


# CSV 안에 쉼표(,)가 들어갈 경우?
# CSV는 기본적으로 ","를 기반으로 문자열을 분리하는데, , 가 들어가서 split(",")가 3개 이상으로 나뉘어버림
# 해결책 : 파이썬 내장 CSV 모듈 사용

# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append({"name" : row[0], "home" : row[1]})

# for s in sorted(students, key=lambda s: s["name"]):
#     print(f"{s['name']} is from {s['home']}")


# DictReader - 헤더가 있는 CSV 파일 (DictReader)
# 파일의 첫 줄에 열 이름(헤더)를 추가해서 더 깔끔해지는 경우

# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for s in sorted(students, key=lambda s: s["name"]):
#     print(f"{s['name']} is from {s['home']}")


# CSV 파일에 쓰기 (Dict Writer)
import csv

name = input("What's your name?")
home = input("Where's your home?")

with open("students.csv", "a", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
    

# 코드 예시 1- 절차적 방식

name = input("Name : ")
house = input("House: ")
print(f"{name} from {house}")


# 함수로 정리하기 (조금 개선된 버전)
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name : ")    

def get_house():
    return input("House:")

if __name__=="__main__":
    main()


# 튜플로 묶기
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")    

def get_student():
    name = input("Name : ")    
    house = input("House:")
    return (name, house)

if __name__ == "__main__":
    main()

# 리스트로 바꾸기
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")    
    house = input("House: ")
    return [name, house]

if __name__ == "__main__":
    main()

# 딕셔너리 사용하기
def main():
    student = get_student()
    print(f"{student['name'] from {student['house']}}")    

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name" : name, "house": house}

if __name__=="__main__":
    main()



# 객체로 표현하기
class Student:

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")        

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__"    :
    main()

# 객체 지향 프로그래밍은 ‘데이터(정보)’와 ‘행동(함수)’을 하나의 객체로 묶는 방식이에요.
# Classes

class Student: # 학생이 태어나는 순간 이름과 집을 설정해주는 코드
    def __init__(self, name, house): # 객체가 생성될 때 자동으로 실행되는 함수
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__"    : # 더블 언더스코어 __ 파이썬 내장 특별 함수?
    main()

# 속성 검증하기
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "slytherin"]:
            raise ValueError("Invalid house")

        self.name = name
        self.house = house

# raise 예외 처리
# raise : 일부러 에러를 일으키는 명령어
def divide(a, b):
    if b == 0:
        raise ValueError("0으로는 나눌 수 없습니다!") 

print(divide(10, 2))        
print(divide(10, 0))


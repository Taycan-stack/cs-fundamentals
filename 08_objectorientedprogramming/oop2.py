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
# raise는 데이터를 깨끗하게 유지해주는 안전장치 역할을 함
def divide(a, b):
    if b == 0:
        raise ValueError("0으로는 나눌 수 없습니다!") 

print(divide(10, 2))        
print(divide(10, 0))


# try/except 에러 잡아서 처리하기
try:
    x = int(input("숫자를 입력하세요: "))
    print(10/x)
except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다")
except ValueError:
    print("숫자만 입력해주세요")    



"""
🧠 정리
키워드	설명
try	“이 코드를 실행해봐”
except	“에러가 나면 이렇게 처리해”
raise	“에러를 일부러 발생시켜”
ValueError, ZeroDivisionError 등	에러 종류 (상황별로 다름)
"""    
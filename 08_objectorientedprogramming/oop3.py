#  Decorators : 함수 위에 @로 시작하는 특별한 "기능"을 붙이는 문법

# 예제 1.
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property #getter
    def house(self):
        return self._house


    @house.setter   #setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravelclaw", "Slytherin"]:
            raise ValueError("Invalid house")

        self._house = house

"""
@property: getter 역할 (값을 읽을 때 자동 호출)
@house.setter : setter 역할 (값을 쓸 때 자동 호출)
_house : 실제 저장되는 변수 이름
밑줄은 직접 건드리지 말라는 신호 > 이 값은 항상 setter를 통해서만 변경해야함

"""
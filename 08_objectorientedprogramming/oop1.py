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

    
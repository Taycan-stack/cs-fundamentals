# open 함수 연습 문제
# 1️⃣ 사용자에게 이름을 계속 입력받아서 names.txt에 저장하는 프로그램을 작성해보세요.
# 단, 빈 문자열("")을 입력하면 종료되도록 만들어보세요.


while True :
    name = input("What's your name?")
    if name == "":
        break
    else:
        file = open("names.txt", "a")
        file.write(f"{name} \n")
        file.close()


# 더 좋은 답 (with 이용)
while True:
    name = input("What's your name?")
    if not name: # name == ""와 같음
        break
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")
        
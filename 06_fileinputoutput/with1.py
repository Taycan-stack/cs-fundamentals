# With 구문 (자동으로 파일 닫기)

name = input("What's your name?")

with open("names.txt", "a") as file: # with를 쓸 경우 close()를 자동으로 호출해줌
    file.write(f"{name}\n")


# 파일 읽기
with open("name.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip()) # rstrip() : 문자열 끝의 줄바꿈 문자 제거
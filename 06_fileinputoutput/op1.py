# open 함수 : 파일을 열어서 내가 읽거나 쓸 수 있게 해주는 열쇠

# open 기본 형태
# file = open("파일이름", "모드")
# 모드에는 "r", "w", "a", "x" 등의 선택지 존재
# 각각 read, write, append, create 등임.

# name = input("What's your name?")

# file = open("names.txt", "w") # names.txt 파일을 쓰기 모드로 엶. 없으면 파일 생성
# file.write(name) # 입력받은 이름을 파일에 씀
# file.close() # 파일을 닫기. 완전한 저장의 개념


# 쓰기 모드는 새로 쓰기 (덮어쓰기) 개념이라서, a 모드로 보완해야함.
# name = input("What's your name?")

# file = open("names.txt", "a") # names.txt 파일을 추가 모드로 엶. 없으면 파일 생성
# file.write(name) # 입력받은 이름을 파일에 씀
# file.close() # 파일을 닫기. 완전한 저장의 개념

# print(name)

# 문제는, 이렇게 하면 문자열들이 붙여져서 출력됨.
# 줄바꿈 추가하기

name = input("What's your name?")

file = open("names.txt", "a")
file.write(f"{name}\n") # 줄바꿈 추가
file.close()
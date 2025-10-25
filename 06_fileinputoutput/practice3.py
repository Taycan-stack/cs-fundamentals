# 연습문제

# names.txt에 여러 줄로 이미 저장된 이름이 있을 때, 위 코드로 읽어와 대문자(Uppercase) 로 바꿔 출력하는 프로그램을 만들어 보세요. (line.rstrip().upper() 사용)
# with open("names.txt", "r", encoding="utf-8") as file :
#     for line in file:
#         print(line.rstrip().upper())



# 사용자에게 이름과 집(house)을 입력받아 students.txt에 이름:집 형식으로 한 줄씩 저장하는 프로그램을 작성해 보세요. (예: Harry:Gryffindor)


# while True:
#     name = input("What's your name?")
#     house = input("Where is your home?")
    
#     if not name or not house:
#         break

#     with open("students.txt", "a", encoding="utf-8") as file:
#         file.write(f"{name}:{house}\n")




# (도전) names.txt에서 중복된 이름을 제거하고 정렬해서 출력하는 코드를 작성해 보세요.
unique = set()
with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines = line.strip() # 한 줄씩 줄바꿈 제거 후 리스트 생성 ()
        if not lines: # 공백 줄이면 건너뛰기
            continue
        unique.add(lines)

for name in sorted(unique): # name으로 변수 지정하면서 한 개씩 출력
    print(name)




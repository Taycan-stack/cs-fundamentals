# 여러 명의 이름을 입력받을 때

names = []

# for _ in range(3):
#     names.append(input("Whats your name?"))

# print(names)

# 정렬해서 출력하기
for _ in range(3):
    names.append(input("What's your name?"))

for name in sorted(names):
    print(f"hello, {name}")
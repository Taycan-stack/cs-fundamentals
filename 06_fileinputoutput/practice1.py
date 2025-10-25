# 이름을 5개 입력받아서 정렬된 순서로 모두 출력하는 프로그램을 작성

names = []

for _ in range (5):
    names.append(input("What's your name?"))


for name in sorted(names):
    print(f"hello, {name}")


# 좀 더 파이써닉하게 적어보기
names = sorted([input("What's your name?") for _ in range(5)])
for name in names:
    print(f"hello, {name}")
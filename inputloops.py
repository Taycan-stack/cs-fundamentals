# n이 0보다 작을 때에는 계속 물어봄

while True:
    n = int(input("What's n?"))
    if n > 0:
        break

for _ in range(n):
    print("meow")


# 함수를 사용한 개선 버전
def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")



main()
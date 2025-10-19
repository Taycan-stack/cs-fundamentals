# mario 예제
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")
    
main()

# 가로줄 출력
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

# 정사각형(square) 출력
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

main()


# 더 깔끔한 버전
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
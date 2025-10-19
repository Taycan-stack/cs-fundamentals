# Pass로 조용히 넘기기
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except :
            pass

main()
"""

# Prompt(입력 메시지)를 함수로 전달하기
def main():
    x = get_int("What's x?")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
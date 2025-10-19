# 좋은 코드는 이렇게 작성함. try 안에 정말 필요한 부분만 삽입

# 오류 생김. x is not defined (try 안에서만 정의되어있음.)
"""
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
"""

# 오류 안 생기려면?
try: # 시도해보고
    x = int(input("What's x?"))
except ValueError: # 오류 나면 여기로
    print("x is not an integer")
else: # 오류가 없을 때만 실행!
    print(f"x is {x}")
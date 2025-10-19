"""
# 리스트 기반 루프
for i in [0, 1, 2]:
    print("meow")

    
# range()로 간결하게
for i in range(3):
    print("meow")

# 변수를 사용하지 않을 때 _ 활용
for _ in range(3):
    print("meow")
"""

# 문자열 곱셈으로 더 간단하게
print("meow\n" * 3, end="")
# Command-Line Arguments -- "명령줄에서 입력받기"

import sys

print("hello, my name is", sys.argv[1])


# 입력이 없을 때 에러 처리

if len(sys.argv) < 2 :
    sys.exit("Too few arguments")
elif len(sys.argv > 2) :
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
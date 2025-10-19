# 프로그램이 오류로 멈추지 않도록 하는 법
try :
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
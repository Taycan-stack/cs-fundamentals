from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 30

if __name__ == "__main__": # 이 파일이 메인 요리일 때만 아래 코드를 돌려라
    test_square()
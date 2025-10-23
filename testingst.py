def hello(to="world"):
    print(f"hello, {to}")

def test_hello():
    assert hello("David") == "hello, David"    

hello("David")


"""
테스트 파일 정리하기
project/
│
├── hello.py
│
└── test/
    ├── __init__.py
    └── test_hello.py


"""
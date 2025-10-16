# 궁금한 것

1. if를 각각 쓰는 게 elif와 혼용해서 사용하는 것과 차이가 뭐야? 
🔹 1️⃣ if를 각각 쓰는 것 vs if + elif (그리고 else)를 함께 쓰는 것

두 코드를 비교해볼게요.

🧩 예시 1 — if를 각각 사용하는 경우
x = 2
y = 2

if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal to y")


➡️ 결과:
x == y이기 때문에 마지막 조건만 True.
결과는 "x is equal to y"이 출력됩니다.

하지만 중요한 건,
파이썬은 세 개의 if문을 모두 검사했다는 점이에요.
즉, 첫 번째 if가 False여도 나머지 두 if를 전부 확인해요.

✅ 장점: 각각의 조건이 독립적으로 작동함

⚠️ 단점: 불필요한 검사가 많음 → 효율이 떨어짐

⚠️ 논리적으로 “하나만 참일 수 있는” 상황에는 비효율적


2. match-case와 if/elif의 차이는 뭐야?
🔹 2️⃣ match-case vs if / elif / else

이건 Python 3.10부터 생긴 새로운 문법이에요.
기본적인 목적은 같아요 — “조건에 따라 다른 코드를 실행하기”.
하지만 사용 목적과 내부 작동 방식이 조금 달라요.

🧩 예시 1 — if/elif 버전
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")


각 조건에 대해 **비교 연산(==)**을 수행

여러 조건이 있으면 or, and로 연결해야 함

코드가 길어지면 조금 지저분해질 수 있음

🧩 예시 2 — match-case 버전
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


match 문은 값을 여러 패턴에 “매칭”시켜서 실행함

| 기호로 여러 값을 한 번에 묶을 수 있음

_는 “기타 모든 경우”를 의미 (즉, else 역할)

코드가 훨씬 깔끔하고 읽기 쉬움

⚙️ 내부적으로의 차이
항목	if / elif / else	match / case
작동 방식	논리식 평가 (True/False 검사)	값 또는 패턴 매칭
비교 방법	비교 연산자 사용 (==, <, > 등)	case의 패턴과 값 일치 여부 검사
코드 가독성	복잡해질 수 있음	단순하고 구조적
Python 버전	모든 버전에서 가능	3.10 이상부터 가능
추가 기능	없음	구조적 패턴 매칭 (복잡한 데이터도 매칭 가능)
💡 예시로 느껴보자

예를 들어, if문으로 이런 건 조금 복잡하지만…

if command == "move":
    print("Moving...")
elif command == "attack":
    print("Attacking...")
elif command == "defend":
    print("Defending...")
else:
    print("Unknown command")


match로 쓰면 딱 보기 좋게 이렇게 됩니다 👇

match command:
    case "move":
        print("Moving...")
    case "attack":
        print("Attacking...")
    case "defend":
        print("Defending...")
    case _:
        print("Unknown command")

✅ 요약
비교 항목	if / elif / else	match / case
용도	논리적 조건 판단	값이나 패턴 매칭
가독성	길어질 수 있음	깔끔하고 직관적
Python 버전	모든 버전	3.10 이상
_의 의미	없음	“else” 역할
추천 상황	복잡한 조건식 (>, <, != 등)	값 비교나 여러 케이스 처리
🧠 간단한 비유로 정리
상황	문법
“온도가 30도 이상이면 덥다” → 비교 논리 필요	→ if
“이 이름이 누구냐?” → 값 비교 중심	→ match
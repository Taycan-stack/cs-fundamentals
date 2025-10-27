# 0_Functions & Variables

좋아요 😄
그럼 이번엔 **CS50 파이썬 0강 전체**를 한 번에,
핵심만 쏙쏙 정리해서 빠르게 복습해볼게요 💨

---

# 🧩 CS50 Python Lecture 0 — Functions & Variables 요약 복습

---

## 🐍 1. Python 프로그램의 시작

* **프로그래밍**은 컴퓨터에게 “이거 해!”라고 명령하는 일이에요.
* 파이썬은 그 명령을 사람이 읽기 쉬운 문장으로 표현한 언어예요.
* 첫 번째 프로그램은 항상 이것! 👇

  ```python
  print("hello, world")
  ```

  👉 `print()` 함수는 **화면에 보여줘!** 라는 뜻이에요.

---

## ⚙️ 2. Functions (함수)

* **함수(function)** 는 “명령어를 묶어둔 상자”예요.
  비슷한 일을 반복할 때 효율적으로 사용할 수 있어요.

```python
def hello():
    print("hello, world")
```

* `def` : “이제 함수를 정의할게”
* `hello()` : 함수 이름
* `:` : “이 밑은 함수의 내용이야”
* `print("hello, world")` : 함수가 실제로 하는 일
* 실행하려면 `hello()` 라고 써요.

---

## 🐞 3. Bugs (버그)

* **버그**는 프로그램에서 생기는 **오류나 오작동**이에요.
* 파이썬은 문법이 틀리면 **에러 메시지**를 보여줘요.
  에러 메시지를 읽는 습관을 들이면 훨씬 빨리 성장해요 💪
* “버그를 찾는 과정”을 **디버깅(debugging)** 이라고 해요.

---

## 📦 4. Variables (변수)

* **변수(variable)** 는 **값을 저장하는 상자**예요 🎁

  ```python
  name = "Alice"
  print(name)
  ```

  → `name`이라는 상자에 `"Alice"`를 넣고, 나중에 꺼내서 써요.

---

## 💬 5. Comments (주석)

* **주석(comment)** 은 사람이 보기 위한 메모예요.
* 컴퓨터는 무시하고 지나가요.

  ```python
  # 이건 주석이야
  print("hi")  # 이 부분은 코드 오른쪽 주석
  ```

---

## 🧠 6. Pseudocode (슈도코드)

* **슈도코드**는 **코드처럼 보이지만 실제로는 코드가 아닌 설명문**이에요.
* 프로그램을 설계할 때 “무엇을 할지”를 미리 정리할 때 써요.

  ```
  1. 사용자에게 이름을 묻는다
  2. 인사말을 출력한다
  ```

---

## 🧵 7. Strings (문자열)

* 문자열(string)은 **글자들의 모음**이에요.

  ```python
  name = "Alice"
  print("Hello, " + name)
  ```

  → `"+"`로 문자열을 이어붙일 수 있어요.

---

## 🎯 8. Parameters (매개변수)

* 함수에 **입력값**을 주고 싶을 때 사용하는 게 **매개변수(parameter)**

  ```python
  def hello(to):
      print("hello,", to)

  hello("David")
  ```

  → 결과: `hello, David`

---

## ✨ 9. Formatted Strings (f-string)

* 문자열에 변수를 더 깔끔하게 넣는 방법 👇

  ```python
  name = "David"
  print(f"hello, {name}")
  ```

  → 중괄호 `{}` 안에 변수를 바로 넣어요.

---

## 🔢 10. Integers & Floats (정수와 실수)

* **int** (정수): 1, 2, 100
* **float** (소수): 3.14, 2.0

  ```python
  x = 2
  y = 3.5
  print(x + y)  # 5.5
  ```

---

## 🧱 11. Principles of Readability (가독성)

* 좋은 코드는 **“사람이 읽기 쉬운 코드”**
* 가독성을 높이려면:

  * 변수명은 의미 있게 (`score`, `name`)
  * 들여쓰기 잘 지키기
  * 주석 적당히 활용하기

---

## 🧮 12. Creating Your Own Functions & Return Values

* 함수가 **계산 결과를 돌려주고 싶을 때** `return`을 써요.

  ```python
  def square(n):
      return n * n

  result = square(3)
  print(result)  # 9
  ```
* `print()`는 보여주는 것,
  `return`은 값을 “돌려주는 것”이에요.

---

## ✅ 핵심 정리

| 개념        | 한 줄 요약       |
| :-------- | :----------- |
| `print()` | 화면에 보여줘      |
| 함수(`def`) | 명령어 묶음       |
| 변수        | 값을 담는 상자     |
| 주석(`#`)   | 코드 설명        |
| 문자열       | 따옴표로 감싼 글자   |
| 매개변수      | 함수에 전달하는 값   |
| `return`  | 함수가 결과를 돌려줌  |
| 가독성       | 사람이 읽기 쉬운 코드 |

---

🧩 CS50 Python Lecture 1 — Conditionals
🎯 1. 배경 설명

이전 0강에서는 “컴퓨터에게 일을 시키는 방법”을 배웠어요.
하지만… 세상 모든 일은 조건에 따라 달라지죠!

예를 들어 👇

비가 오면 → 우산을 챙기고 ☔

아니면 → 그냥 나간다 🚶‍♀️

이런 “상황에 따라 다른 행동을 하는” 코드를 만들고 싶을 때
조건문(Conditional) 을 써요.

⚙️ 2. 기본 구조: if, elif, else
x = int(input("x: "))
y = int(input("y: "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


🪄 한 줄씩 설명

if: “만약 ~라면”

elif: “그렇지 않고 만약 ~라면”

else: “그 외의 경우엔”

들여쓰기(Indentation)가 매우 중요해요!
→ “이 줄은 if문 안에 포함돼 있어요”라는 뜻이에요.

💬 3. 비교 연산자
연산자	의미
==	같다
!=	다르다
<	작다
>	크다
<=	작거나 같다
>=	크거나 같다

예시 👇

if score >= 90:
    print("A학점!")

🔀 4. 논리 연산자: and, or, not

조건을 합칠 때 사용해요.

if x > 0 and y > 0:
    print("둘 다 양수!")

연산자	의미	예시
and	둘 다 참이어야 함	“x도, y도”
or	하나라도 참이면 됨	“x거나 y거나”
not	반대로	“참이면 거짓, 거짓이면 참”
💡 5. Modulo (%)

숫자를 나눈 나머지를 구해요.

if n % 2 == 0:
    print("짝수")
else:
    print("홀수")


👉 % 2로 나머지를 확인하면
짝수인지 홀수인지 바로 알 수 있죠!

🧠 6. Pythonic Coding

파이썬답게! ✨
불필요한 조건문을 줄이고, 간결하게 표현할 수 있어요.

예시 👇

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


를 이렇게 줄일 수도 있어요 👇

print("Even" if n % 2 == 0 else "Odd")

🧩 7. match 문 (파이썬 3.10+)

파이썬 최신 문법으로 switch-case 역할을 해요.

name = input("Name: ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


case _:는 “그 외 모든 경우”

여러 가지 경우를 깔끔하게 나눌 때 아주 유용해요.

✅ 핵심 정리
개념	설명
if, elif, else	조건에 따라 다른 행동
비교 연산자	크다, 같다, 다르다 등
and, or, not	조건 결합
%	나머지 (짝/홀 판단에 유용)
Pythonic Style	코드 짧고 읽기 좋게
match	여러 조건을 깔끔하게 구분

---
🌀 CS50 Python Lecture 2 — Loops (반복문)
🎯 1. 배경 설명

이전 강의에서는 “조건에 따라 한 번 행동” 하는 법을 배웠죠.
하지만 컴퓨터는 사람보다 잘하는 게 하나 있어요 — “반복” 🔁

예를 들어,

“별을 5번 찍어라”

“리스트 안의 모든 이름을 출력해라”

“파일 안의 줄들을 하나씩 읽어라”

이런 건 반복문(loop) 으로 처리해요.
반복문은 컴퓨터에게 “이걸 여러 번 해!”라고 시키는 명령이에요.

🔁 2. while 문
i = 0
while i < 3:
    print("meow")
    i += 1


🪄 설명

while은 “~하는 동안 계속해라”

i < 3이 참(True) 인 동안 반복

i += 1로 i를 1씩 증가시켜, 언젠가 조건이 거짓(False)이 되어 멈춤

💡 만약 i += 1을 빼먹으면?
→ 조건이 영원히 참이어서 무한 루프(무한 반복) 발생 😱

🔂 3. for 문
for i in range(3):
    print("meow")


🪄 설명

range(3) → 0, 1, 2 (세 번 반복)

i는 각 순서의 번호(인덱스)를 받음

for은 “정해진 횟수만큼 반복”할 때 사용

💬 결과:

meow
meow
meow

📏 4. range() 함수

range(n) → 0부터 n-1까지

range(1, 4) → 1, 2, 3

range(0, 10, 2) → 0, 2, 4, 6, 8 (2씩 증가)

📋 5. list (리스트)

리스트(list) 는 여러 값을 한꺼번에 담는 상자 모음이에요 📦📦📦

students = ["Harry", "Hermione", "Ron"]
for student in students:
    print(student)


💡 여기서 student는 리스트 안의 요소를 하나씩 꺼내주는 반복 변수예요.

🧱 6. len() 함수

리스트나 문자열의 길이(개수) 를 알려줘요.

students = ["Harry", "Hermione", "Ron"]
print(len(students))  # 3


💡 len은 “length(길이)”의 줄임말이에요.

🧭 7. dict (딕셔너리)

딕셔너리(dictionary) 는 “이름표가 붙은 상자들”이에요.
즉, 키(key) 와 값(value) 의 쌍으로 데이터를 저장하죠.

students = {
    "Harry": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student])


출력 결과 👇

Harry Gryffindor
Draco Slytherin


💡 for student in students:
→ 딕셔너리의 key 들을 하나씩 꺼냄

🧠 8. break, continue (반복 제어)

break : 반복문을 즉시 멈춤

continue : 이번 회차만 건너뛰고 다음으로 진행

예시 👇

for i in range(5):
    if i == 2:
        continue
    print(i)


결과:

0
1
3
4

✅ 핵심 정리
개념	설명
while	조건이 참인 동안 반복
for	정해진 횟수나 리스트 순회
range()	숫자 범위 생성
len()	리스트나 문자열 길이
list	여러 값을 순서대로 저장
dict	키와 값의 쌍으로 저장
break / continue	반복 제어

⚠️ CS50 Python Lecture 3 — Exceptions (오류 처리)
🎯 1. 배경 설명

지금까지 프로그램을 잘 짜왔다고 해도,
사용자가 엉뚱한 입력을 하면 프로그램이 멈출 수 있어요!

예를 들어 👇

x = int(input("x: "))
y = int(input("y: "))
print(x / y)


만약 사용자가 y에 0을 넣으면?

ZeroDivisionError: division by zero


😱 프로그램이 멈춰버려요!

이런 문제를 막기 위해 필요한 게 바로 예외 처리(Exceptions) 입니다.

⚙️ 2. try / except 구조
try:
    x = int(input("x: "))
    y = int(input("y: "))
    result = x / y
    print(result)
except ValueError:
    print("숫자를 입력해야 해요!")
except ZeroDivisionError:
    print("0으로 나눌 수 없어요!")


🪄 설명

try: “이 코드를 시도해봐”

except: “만약 에러가 나면 이렇게 처리해”

프로그램이 멈추지 않고, 예쁘게 대처할 수 있음

💡 3. 여러 종류의 에러
에러 이름	언제 발생하나요?
ValueError	형 변환이 잘못됐을 때 (예: int("hi"))
ZeroDivisionError	0으로 나눌 때
RuntimeError	실행 중 논리 오류 발생 시
TypeError	자료형이 맞지 않을 때 (예: "hi" + 5)
🧠 4. else, finally, pass
else

try가 성공했을 때만 실행되는 부분이에요.

try:
    x = int(input("x: "))
except ValueError:
    print("숫자가 아니에요!")
else:
    print("잘했어요 👍")

finally

에러가 나든 안 나든 무조건 실행되는 코드
(예: 파일 닫기, 연결 끊기 등)

try:
    f = open("data.txt")
    # 파일 읽기
finally:
    f.close()

pass

“여기 에러 나도 그냥 넘어가”라는 뜻이에요.
보통 임시로 써요.

try:
    risky_code()
except:
    pass


⚠️ 하지만 너무 자주 쓰면 문제 숨기기가 되니까 조심!

🔍 5. 예외 처리의 목적

프로그램이 강제 종료되지 않게 하기

사용자 친화적인 메시지 보여주기

예상치 못한 상황에도 안정적으로 작동시키기

✅ 핵심 정리
키워드	의미
try	시도해봐
except	에러가 나면 이거 실행
else	에러가 없을 때 실행
finally	무조건 실행
pass	그냥 넘어가기
ValueError, ZeroDivisionError	대표적인 예외 타입
🧩 실생활 비유

예외 처리는 안전벨트에요! 🚗

사고(에러)가 나도, 프로그램(운전자)은 다치지 않고 계속 진행할 수 있게 보호해 줍니다.

이제 프로그램이 “문제가 생겨도 멈추지 않고 대처할 수 있는” 단계로 진화했어요 👏

📚 CS50 Python Lecture 4 — Libraries (라이브러리)
🎯 1. 라이브러리란?

“다른 사람이 미리 만들어 놓은 유용한 코드 모음집”
파이썬에는 이런 코드 꾸러미가 아주 많아요.

예를 들어,
“주사위 굴리기” 기능을 직접 코딩하지 않아도,
random 라이브러리가 이미 있어요 🎲

⚙️ 2. 라이브러리 가져오기 — import
import random
print(random.randint(1, 6))


📦 import는 “이 도구 상자를 꺼내와”라는 뜻이에요.
random.randint(a, b)는 a~b 사이의 랜덤 정수를 리턴합니다.

🧮 3. 주요 표준 라이브러리들
라이브러리	역할	예시
random	난수 생성	random.choice(list)
statistics	평균, 중앙값 등 통계	statistics.mean(nums)
sys	명령줄 인자, 시스템 관련	sys.argv, sys.exit()
os	파일/디렉토리 작업	os.listdir()
datetime	날짜와 시간	datetime.now()
🧰 4. from ... import ... 구문
from random import choice
print(choice(["가위", "바위", "보"]))


👉 이렇게 하면 random.choice() 대신 그냥 choice()로 바로 호출할 수 있어요.

🖥️ 5. Command-Line Arguments (명령줄 인자)

프로그램 실행 시 명령줄에서 입력을 받을 수도 있어요.

import sys

print("Hello, my name is", sys.argv[1])


터미널에서 이렇게 실행 👇

python hello.py David


결과 →

Hello, my name is David


⚠️ sys.argv는 리스트 형태로,
argv[0]은 파일 이름, argv[1]부터 인자!

✂️ 6. Slice (슬라이싱)

문자열이나 리스트의 일부만 잘라내기

name = "David"
print(name[0:3])   # "Dav"
print(name[:2])    # "Da"
print(name[1:])    # "avid"


🧠 파이썬에서 [시작:끝]은 “시작은 포함, 끝은 제외”

🧩 7. Packages (패키지)

여러 라이브러리를 폴더 단위로 묶어둔 것

예를 들어,

requests → HTTP 통신용 패키지

PIL (Pillow) → 이미지 처리용 패키지

설치는 이렇게 👇

pip install requests

🌐 8. APIs (Application Programming Interfaces)

서버끼리 대화할 수 있는 약속된 방법

예: “날씨 알려줘 API”

import requests

response = requests.get("https://api.weatherapi.com/v1/current.json?key=KEY&q=Seoul")
data = response.json()
print(data["current"]["temp_c"])

🏗️ 9. 내 라이브러리 만들기

mymath.py 파일을 만들어서 👇

def square(n):
    return n * n


그리고 다른 파일에서

import mymath
print(mymath.square(5))


✅ 직접 만든 모듈도 import해서 쓸 수 있어요.

✅ 핵심 정리표
키워드	설명
import	라이브러리 불러오기
from ... import ...	특정 함수만 가져오기
sys.argv	명령줄 인자 받기
slice	문자열/리스트 일부 자르기
pip	외부 패키지 설치
API	서버 간 통신 인터페이스
requests, PIL	외부 패키지 예시

📌 요약:
이제 파이썬을 “혼자” 쓰지 않고,
다른 사람의 코드, 도구, API를 활용해서
더 강력한 프로그램을 만들 수 있게 되었어요 💪


🧪 CS50 Python Lecture 5 — Unit Tests (단위 테스트)
🎯 1. 왜 테스트가 필요할까?

예를 들어, 이런 코드가 있다고 해요 👇

def square(n):
    return n * n


겉보기에 멀쩡해 보여요.
하지만 누군가 이렇게 바꿔버렸다면?

def square(n):
    return n + n


겉으론 잘 몰라도, 프로그램 전체가 틀릴 수 있죠 😨
그래서 **“자동으로 코드의 결과를 검사하는 방법”**이 필요해요.
그게 바로 **unit test (단위 테스트)**예요!

🧩 2. assert 문 — “이게 맞지 않으면 멈춰!”
def test_square():
    assert square(2) == 4
    assert square(3) == 9


assert는 **“이 조건이 참이어야 한다”**는 뜻이에요

만약 틀리면 프로그램이 멈추고 오류를 내요 ❌

즉,

“square(2)는 4가 되어야 한다!”
“square(3)는 9가 되어야 한다!”
를 자동으로 확인하는 거예요 ✅

🧰 3. pytest — 자동으로 테스트 돌려주는 도구

1️⃣ 먼저 설치

pip install pytest


2️⃣ 파일 이름을 이렇게 만들어요

test_square.py


3️⃣ 안에 이렇게 작성 👇

from mymath import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(0) == 0


4️⃣ 그리고 터미널에서 실행 👇

pytest


✅ 결과:

================= test session starts =================
collected 1 item
test_square.py .                                [100%]
================= 1 passed in 0.01s ==================


모든 테스트가 통과되면 “. (점)”이 표시돼요!

🧠 4. 테스트의 핵심 원리
용어	뜻
Unit Test	프로그램의 작은 단위(함수 등)를 검사
Integration Test	여러 단위를 함께 테스트
Regression Test	버그가 고쳐진 후 다시 생기지 않는지 검사

파이썬에서는 주로 unit test로 함수 동작을 점검해요.

💡 5. 테스트의 좋은 습관

작은 기능 단위로 자주 테스트하기

엣지 케이스(극단 입력) 확인하기

예: 0, 음수, 아주 큰 수

테스트 코드도 깔끔하게 관리하기

테스트를 자동화해서 매번 수동 실행 안 하게 하기

🧩 6. 테스트 실패 예시
def square(n):
    return n + n   # 실수!

def test_square():
    assert square(2) == 4


결과:

E       assert 4 == 4
E       AssertionError: assert 4 == 4  # ✅ 통과


하지만 만약 square(2)가 5였다면,

E       assert 5 == 4
E       AssertionError


라고 뜨면서 테스트가 실패해요 🚨

✅ 요약 정리
키워드	설명
assert	“이 조건이 참이어야 한다”를 검사
pytest	테스트 자동 실행 도구
unit test	함수 단위로 코드 검증
test_*.py	pytest가 인식하는 테스트 파일 이름
AssertionError	테스트 실패 시 발생하는 오류

📌 핵심 요약:

테스트는 “코드가 제대로 동작하는지 자동으로 증명하는 방법”이에요.
직접 눈으로 확인하지 않아도, pytest가 대신 확인해줘요! 👀✅

💾 CS50 Python Lecture 6 — File I/O (Input/Output)
🎯 1. 왜 파일 I/O를 배울까?

지금까지 만든 프로그램은
사용자가 입력한 데이터를 “메모리” 안에서만 썼어요.
그런데 프로그램을 끄면?
👉 데이터가 다 사라져요 😢

그래서 우리는
파일에 데이터를 저장하고 다시 읽는 방법을 배워야 해요!

📂 2. 파일 열기 — open()
file = open("names.txt", "r")
for line in file:
    print(line.strip())
file.close()


"r" : 읽기 모드 (read)

"w" : 쓰기 모드 (write — 덮어쓰기)

"a" : 추가 모드 (append — 이어쓰기)

strip()은 줄바꿈 \n을 없애줘요 ✂️

🔐 3. with 문 — 자동으로 닫아주는 안전한 방법
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())


✅ with는 파일을 자동으로 닫아줘서,
close()를 따로 쓸 필요가 없어요!

💡 “파일을 잠깐 열었다가, 다 쓰면 바로 닫는 안전한 문법”이에요.

✍️ 4. 파일에 쓰기 — "w" 모드
with open("names.txt", "w") as file:
    file.write("Harry\n")
    file.write("Ron\n")
    file.write("Hermione\n")


📌 주의! "w"는 기존 내용이 사라지고 덮어쓰기예요.

➕ 5. 이어쓰기 — "a" 모드
with open("names.txt", "a") as file:
    file.write("Draco\n")


이건 기존 파일 뒤에 추가됩니다 ✨

📊 6. CSV 파일 다루기

CSV는 Comma-Separated Values (콤마로 구분된 값)
엑셀 같은 표 데이터를 저장할 때 많이 써요.

✅ 읽기 예시
import csv

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]} is from {row[1]}")

✅ 쓰기 예시
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "house"])
    writer.writerow(["Harry", "Gryffindor"])
    writer.writerow(["Draco", "Slytherin"])


💡 newline=""은 줄바꿈이 두 번 생기지 않게 막아줘요.

🖼️ 7. Binary Files & PIL (이미지 파일 다루기)

텍스트 파일이 아니라 사진, 음악, 동영상 같은 파일은
0과 1로 된 이진(binary) 파일이에요.

예를 들어 이미지를 열어 수정하려면,
PIL (Pillow) 라이브러리를 써요 📷

from PIL import Image

image = Image.open("cat.jpg")
image.show()
image.save("newcat.png")


.open() : 이미지 열기

.show() : 보여주기

.save() : 다른 이름으로 저장

🧠 8. 정리
개념	설명
open("파일", "r")	읽기
open("파일", "w")	덮어쓰기
open("파일", "a")	이어쓰기
with open(...)	파일 자동 닫기
csv.reader	CSV 읽기
csv.writer	CSV 쓰기
PIL	이미지 파일 다루기
✅ 요약 문장

지금까지 배운 파이썬은 “기억력이 없는 아이”였다면,
이제는 파일에 기록을 남길 줄 아는 똑똑한 아이가 되었어요 ✨
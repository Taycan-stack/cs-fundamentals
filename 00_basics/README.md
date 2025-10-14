# cs-fundamentals
Computer Science 공부

---

## 🎓 Lecture 0 — Python 기초: "Creating Code with Python"

### 🧩 1. 파이썬 코드 실행하기 (hello.py)

**목표:** “Hello, world” 프로그램을 만들어보자.

---

#### 📁 1단계: 파일 만들기

Codespaces 터미널에서 다음을 입력해 새 파일을 만듭니다:

```bash
code hello.py
```

이 명령은 VS Code 에디터 창에 `hello.py` 파일을 열어줍니다.

---

#### ✍️ 2단계: 코드 작성하기

파일에 다음을 입력하세요:

```python
print("hello, world")
```

이건 모든 프로그래머가 배우는 “전통의 첫 코드”입니다.

---

#### ▶️ 3단계: 코드 실행하기

터미널로 이동해서 다음을 입력합니다:

```bash
python hello.py
```

결과:

```
hello, world
```

✅ 축하합니다! 여러분은 첫 번째 파이썬 프로그램을 만들었습니다.

---

### ⚙️ 2. 함수 (Functions)

`print()`는 **함수(function)**입니다.
함수란 **컴퓨터가 미리 알고 있는 행동(명령어)**이에요.

예:

```python
print("hello, world")
```

* `print`는 "출력하라"는 뜻의 함수
* `"hello, world"`는 **인자(argument)** — 함수에게 주는 정보입니다.

---

### 🐞 3. 버그 (Bugs)

버그는 **코드의 오류**입니다.
예를 들어:

```python
print("hello, world"
```

괄호를 닫지 않으면 에러가 발생합니다.

```
SyntaxError: unexpected EOF while parsing
```

➡️ 에러 메시지를 **읽는 연습**이 중요합니다. 에러가 여러분의 친구예요.
“어디서 틀렸는지” 힌트를 줍니다.

---

### 👩‍💻 4. 프로그램 개선하기

사용자에게 **이름을 입력받아서** 인사하도록 해볼까요?

```python
input("What's your name? ")
print("hello, world")
```

하지만 이렇게 하면 입력값을 **저장하지 않아요.**

---

### 📦 5. 변수 (Variables)

변수를 사용하면 입력값을 저장할 수 있습니다.

```python
name = input("What's your name? ")
print("hello, world")
```

이제 `name`이라는 상자(변수)에 사용자의 입력값이 저장됩니다.

그런데 이렇게 해볼까요?

```python
name = input("What's your name? ")
print("hello, name")
```

결과는?

```
hello, name
```

❌ 틀렸죠.
파이썬은 `"hello, name"`을 **문자 그대로 출력**했어요.
우리가 원한 건 변수 `name`의 값이죠.

---

### ✅ 해결방법

방법 1:

```python
print("hello, " + name)
```

방법 2:

```python
print("hello,", name)
```

결과:

```
What's your name? David
hello, David
```

---

### 💬 6. 주석 (Comments)

주석은 컴퓨터가 무시하는 설명문입니다.

```python
# Ask the user for their name
name = input("What's your name? ")

# Print hello and the inputted name
print("hello,", name)
```

`#` 뒤의 내용은 코드 실행에 영향을 주지 않아요.
나중에 코드를 읽을 때 큰 도움이 됩니다.

---

### 🧠 7. 의사 코드 (Pseudocode)

의사 코드는 **논리적인 계획서**입니다.

```python
# Ask the user for their name
# Print hello
# Print the name inputted
```

아직 어떻게 코딩할지 몰라도, **무엇을 해야 할지** 단계별로 적는 것이죠.

---

### 🧹 8. 코드 더 깔끔하게 만들기

다음처럼 더 효율적인 코드로 바꿔봅시다:

```python
# Ask the user for their name
name = input("What's your name? ").strip().title()

# Print the output
print(f"hello, {name}")
```

📌 `.strip()` → 양쪽 공백 제거
📌 `.title()` → 이름을 “David”처럼 첫 글자 대문자로 바꿈
📌 `f"..."` → **f-string** (문자열 포매팅)

예시 입력/출력:

```
What's your name?   david  
hello, David
```

---

### 🧮 9. 정수 (int)와 덧셈

새 파일을 만들어볼게요.

```bash
code calculator.py
```

간단한 계산기:

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
```

이제 입력받은 문자열을 **정수(int)**로 변환했습니다.
이걸 **형변환(casting)**이라고 부릅니다.

---

### 💡 10. 실수 (float)

소수점이 있는 숫자도 처리해볼까요?

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)
print(f"{z:,}")
```

`round()` → 반올림
`f"{z:,}"` → 천 단위 구분 쉼표 추가 (예: `1,000`)

---

### 🔁 11. 함수 정의하기 (def)

이제 **직접 함수를 만들어볼 차례입니다.**

```python
def hello(to="world"):
    print("hello,", to)

name = input("What's your name? ")
hello(name)
hello()
```

결과:

```
What's your name? David
hello, David
hello, world
```

`to="world"` → **기본값(default value)** 설정

---

### 🧱 12. main 함수로 구조화하기

```python
def main():
    name = input("What's your name? ")
    hello(name)
    hello()

def hello(to="world"):
    print("hello,", to)

main()
```

이제 프로그램이 더 **구조적이고 읽기 쉬워졌죠.**

---

### 🔙 13. 값 반환하기 (return)

```python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()
```

`square()` 함수는 값을 계산하고,
그 결과를 `main()`으로 **되돌려(return)** 줍니다.

---

## 🧾 Lecture 0 요약

| 개념                        | 핵심 내용              |
| ------------------------- | ------------------ |
| `print()`                 | 터미널에 출력            |
| `input()`                 | 사용자 입력 받기          |
| 변수                        | 값을 저장하는 상자         |
| 주석 `#`                    | 코드 설명              |
| 문자열                       | `"텍스트"`            |
| f-string                  | `f"hello, {name}"` |
| int / float               | 정수, 실수             |
| round(), title(), strip() | 내장 함수들             |
| 함수 정의                     | `def hello():`     |
| return                    | 함수 결과 되돌리기         |
| main()                    | 프로그램의 시작점          |

---


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

이제 ✅ 0강에서 배운 걸 다 정리했어요!
다음은 **1강 Conditionals (조건문)** 으로 넘어갈 차례예요.

넘어갈까요?

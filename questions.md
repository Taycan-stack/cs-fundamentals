# 질문 모음

완전 괜찮아요 — 모르는 게 많다는 건 배우고 있다는 증거입니다. 😊
질문 하나하나 차근차근, 예시랑 함께 기초부터 설명해줄게요.

# 1) `f"x is {x}"` — 그냥 외워야 하나? 규칙성은?

* 이건 **f-string**(포맷 문자열)이라고 불러요. `f"..."` 앞에 `f`를 붙이면 문자열 내부의 `{}` 안에 있는 **파이썬 표현식**(변수, 연산, 함수 호출 등)을 계산해서 문자열로 넣어줍니다.
* 규칙:

  * 반드시 `f` 또는 `F`를 문자열 앞에 붙여야 동작해요.
  * 중괄호 `{}` 안에는 변수 이름이나 표현식이 들어갑니다. 예: `f"{x}"`, `f"{x+1}"`, `f"{name.upper()}"`.
  * 대괄호 `[x]`는 **리스트 인덱싱** 등 다른 의미이므로 f-string에서 값을 넣고 싶으면 `{}`를 써야 합니다.
* 예시:

```python
name = "Ava"
x = 3
print(f"{name} has {x} apples.")  # Ava has 3 apples.
print(f"{x+2} apples")            # 5 apples
# 만약 print("x is {x}") 이렇게 하면 {x}가 문자 그대로 출력됨
```

요약: 규칙성은 `{}` 안에 파이썬 표현식을 넣는 것 — 외우기보다 규칙(앞에 `f`, 중괄호 사용)을 이해하면 금방 익숙해져요.

---

# 2) Google Sheets의 `IFERROR`와 Python `try/except`는 비슷한가?

* **비슷한 목적**(오류가 났을 때 우아하게 처리) 은 맞아요.
* 차이점:

  * `IFERROR(value, fallback)`는 *수식 수준*에서 “value가 오류면 fallback을 반환”하는 함수입니다. 한 줄로 끝나요.
  * `try/except`는 **파이썬의 제어 흐름**으로, 여러 줄의 코드 블록에서 어떤 종류의 예외를 잡아 처리할 수 있어요. 예외의 종류도 선택적으로 처리 가능하고, 복잡한 로직(입력 반복, 여러 함수 호출 등)에 사용할 수 있어요.
* 비유하면: `IFERROR`는 간단한 `if`-스타일의 오류 치환, `try/except`는 더 유연한 오류 처리 도구입니다.

---

# 3) `try` 안에 `print`를 넣었을 때 vs 밖에 뒀을 때 — 정확한 차이

핵심: **어떤 코드가 `try` 블록에서 실패하면 그 라인 이후의 `try` 내부 코드는 실행되지 않고 except로 넘어간다**.
그래서 `x`를 `try` 안에서만 정의하려 했는데 실패하면, `try` 밖에서 `x`를 사용하면 `NameError`(정의되지 않음)가 난다는 거예요.

예시 1 (print 안에 같이 있음):

```python
try:
    x = int(input("What's x? "))   # 이 줄에서 실패하면 아래 print도 실행 안 됨
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```

* 입력이 `50`이면: `print(f"x is {x}")` 실행.
* 입력이 `cat`이면: `int(...)`에서 `ValueError` → `print(f"x is {x}")` **실행 안 됨** → except 실행.

예시 2 (print를 밖에 둠):

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")   # 문제가 생길 수 있음
```

* 입력이 `cat`이면: except 실행되어 "x is not an integer" 출력. 그 다음 `print(f"x is {x}")` 실행하려 하는데, `x`가 **정의되지 않았기 때문에** `NameError` 발생.
* 즉 차이는 **변수 `x`의 정의 유무(스코프/타이밍)** 때문에 생깁니다.

---

# 4) `def foo()` 에서 괄호 안에 변수를 넣을지 말지 — 언제 어떤 걸 쓰나?

* `def 함수이름(매개변수들):` 는 **함수를 정의할 때 외부로부터 어떤 값을 받을지** 정하는 자리예요(매개변수 = parameter).
* 함수를 사용할 때(호출할 때) 전달하는 값은 **인수(arguments)** 라고 불러요.

예:

```python
def greet():                 # 매개변수 없음
    print("Hello!")

def greet_name(name):        # name은 매개변수
    print("Hello,", name)

greet()                     # 호출, 인수 없음
greet_name("Ava")           # 호출, "Ava"는 인수
```

언제 넣을까?

* 함수가 외부 값(문자열, 숫자 등)을 필요로 할 때 괄호 안에 매개변수를 선언해요.
* 필요 없으면 빈 괄호로 정의(예: `def main():`).

`get_int()` 예:

* `get_int()`로 정의하면 내부에서 고정된 질문만 쓴다는 의미.
* `get_int(prompt)`로 정의하면 **프롬프트를 바꿀 수 있어서 재사용성↑**.

---

# 5) `else: break` 대신 `return x` 하는 이유

비교:

```python
# A: else + break, 그리고 함수 끝에서 return x
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x
```

```python
# B: else에서 바로 return
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
```

* `break`는 **루프만 종료**시켜요. 루프 밖에 `return x`가 있어야 함수가 값을 반환합니다.
* `return`은 **즉시 함수 전체를 종료하면서 값을 반환**해요. 그래서 `else: return x`가 더 간결합니다.
* 둘 다 동작은 같지만 `return`을 쓰면 코드가 한 줄 줄고 의도가 더 직접적이에요(값을 반환한다는 목적이 명확).

---

# 6) `try`에서 바로 `return` 하는 것 vs `else`에서 `return` — 차이?

두 코드:

```python
# 1: try에서 바로 return
def g1():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
```

```python
# 2: else에서 return
def g2():
    while True:
        try:
            val = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return val
```

* **기능상 결과는 동일**: 올바른 정수를 입력하면 바로 반환, 아니면 계속 반복.
* 하지만 스타일/안전성 차이가 있어요:

  * `try` 블록에 **최소한의 위험한 코드만** 넣는 것이 권장돼요. 이유: `try` 내부에 불필요한 다른 코드(예: 파일 쓰기, 복잡한 계산 등)가 있으면 의도치 않은 예외까지 잡힐 수 있어요(디버깅 어려움).
  * `else`는 “예외가 절대 발생하면 안 되는 코드”를 두는 곳으로 읽기 쉽고 안전해요.
* 성능 차이는 미미(사실상 무시 가능). 가독성과 안정성 때문에 **작은 범위의 try + else** 패턴을 권장하곤 합니다.

요약: 짧게 쓰는 건 괜찮지만, 유지보수/디버깅 관점에서 `else`를 쓰는 게 더 명확한 경우가 많아요.

---

# 7) `except ValueError` 에서 `"ValueError"`는 에러 이름인가? 꼭 알아야 하나?

* 맞아요. `ValueError`는 **예외(오류)의 클래스 이름**이에요. 파이썬에는 여러 예외 클래스가 있어요(예: `TypeError`, `NameError`, `ZeroDivisionError`, `IndexError` 등).
* `except ValueError:` 라고 하면 **오직 `ValueError`만 처리**합니다.
* `except:`(아무것도 안 적음)은 모든 예외를 잡아버리므로 디버깅을 어렵게 만들 수 있어요 — 보통 권장하지 않습니다.
* 왜 특정 예외를 쓰냐? 같은 블록에서 발생할 수 있는 **다른 문제는 다른 방식으로 처리**하고 싶을 때가 많거든요.

예:

```python
try:
    # A: 사용자 입력 -> ValueError 가능
    # B: 파일 읽기 -> FileNotFoundError 가능
    pass
except ValueError:
    print("입력 오류")
except FileNotFoundError:
    print("파일이 없어요")
```

결론: 어떤 에러가 날지 예상할 수 있으면 **그 에러만 정확히 잡는 것이 좋음** → 안전하고 디버깅 쉬움.

---

# 8) `get_int("What's x? ")` 처럼 프롬프트를 넘기는 게 왜 편한지 (예시로 설명)

* 함수에 매개변수를 만들면 **같은 기능을 다른 메시지로 재사용**할 수 있어요.

예시:

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not an integer, try again.")

age = get_int("How old are you? ")
apples = get_int("How many apples? ")
```

* `get_int("How old are you? ")` 호출 시 `prompt`에 `"How old are you? "`가 들어가고, `input(prompt)`이 그 메시지를 보여줍니다.
* 그러면 하나의 함수(`get_int`)로 여러 질문을 할 수 있어 코드가 재사용 가능하고 깔끔해져요.

---

## 마무리 — 연습 제안

원하면 바로 연습문제 3개 만들어줄게요:

1. f-string 변형 문제
2. try/except로 안전하게 입력받기 (여러 예외 핸들링 포함)
3. 함수를 매개변수 사용/미사용 두 버전으로 바꿔보기

어떤 걸 먼저 풀어볼래? 혹은 지금까지 설명 중에 다시 보고 싶은 부분 있어? 내가 바로 코드 예시랑 설명 더 추가해줄게 🙂

---

🔄 상태 변화 요약
표시	상태	설명
U (Untracked)	새 파일	Git이 아직 관리하지 않음 (git add 전)
A (Added)	추가됨	git add 했지만 커밋은 아직 안 됨
M (Modified)	수정됨	기존 파일을 수정했지만 커밋은 아직 안 됨
D (Deleted)	삭제됨	파일이 삭제되었지만 커밋은 아직 안 됨
✓ (없음)	커밋 완료	변경 사항이 커밋되어 Git 상태와 워킹 디렉토리가 일치
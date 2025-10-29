# re.match 사용
# 문자열 맨 앞에서만 패턴 찾음 ("world hello"에서는 "Hello를 못 찾음")

import re

s = "hello world"

if re.match(r"^hello", s):
    print("Match found!")
else:
    print("No match!")    
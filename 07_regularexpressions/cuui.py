# Cleaning Up User Input (입력값 정리하기)

import re

email = input("What's your email?".strip().lower())

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")    
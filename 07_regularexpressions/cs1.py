# Case Sensitivity (대소문자 구분)

import re

email = input("What's your email?").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")

else:
    print("Invalid")
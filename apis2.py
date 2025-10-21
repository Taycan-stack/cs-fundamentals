# Making your own libraries - "직접 만든 도구 상자"

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

import sys
from sayings import goodbye
dd .
if len(sys.argv) == 2:
    goodbye(sys.argv[1])


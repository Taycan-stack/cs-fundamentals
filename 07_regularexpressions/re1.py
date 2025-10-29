import re

email = input("What's your email? ").strip() # 문자열의 시작과 끝에서 특정 문자 제거

# re.search : 문자열 안에서 패턴을 찾는 함수
# r"..." : raw string (특수문자를 있는 그대로 인식하게 함)
if re.search(r"^[^@]+@[^@]+\.(com|edu|net|org)$", email):
    print("Valid")
else:
    print("Invalid")    


    

# with : 파일을 열고 사용한 뒤 자동으로 닫아주는 안전벨트. open 후 close를 깜빡하면 파일이 제대로 저장되지 않거나 프로그램이 에러날 때 파일이 닫히지 않을 수 있음.

# 쓰기 예시 (with 사용)
name = input("What's your name?")

with open("names.txt", "a") as file: # close 안해도 자동으로 닫히는 안전성
    file.write(f"{name}\n")


# 읽기 예시 : readlines() 사용
# readlines() : 파일의 모든 줄을 리스트로 읽어옴
with open("names.txt", "r") as file:
    lines = file.readlines()


for line in lines:
    print("hello, ", line)    


# 줄바꿈 문제 해결 - rstrip() 사용
# rstrip() : 문자열의 오른쪽(끝부분)에 있는 공백 문자들 (공백, 탭, \n 등)을 제거함
# lstrip, strip 등으로 응용 가능
with open("name.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello, ", line.rstrip())    


# readlines는 전체를 한꺼번에 메모리에 올리기 때문에 file을 한 줄씩 순회하여 메모리를 아끼는 방식
# 
with open("name.txt", "r") as file:
    for line in file:
        print("hello, ", line.rstrip())

# 정렬해서 출력하기 (메모리에 담아 처리)
# 파일이 매우 클 경우(수백만 줄) append로 메모리에 올리기보다 외부 정렬 기법이나 DB 사용을 고려해야함
name = []

with open("names.txt", "r", encoding="utf=8") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


# with 의 장점 (정리)    
# 자동으로 파일을 닫아줌 : 에러가 나거나 return/break가 있어도 안전하게 닫힘. -> 덕분에 파일 저장이 안전함
# 코드가 더 깔끔해짐 (close() 호출 불필요)
# 파일 읽기 시 한 줄씩 반복 가능한 객체이므로 메모리 효율적

# file.write()는 문자열만 쓸 수 있음. 숫자는 str()로 바꿔서 써야 함. ex. file.write(str(100) + "\n")
# file.writelines(list_of_strings)를 쓰면 리스트에 있는 문자열들을 한 번에 쓸 수 있음. (단, 줄바꿈을 각 문자열에 직접 넣어줘야 함.)
# 파일 열기 모드를 생략하면 기본은 read임. open("names.txt")는 읽기 모드
# 인코딩 문제 : 특히 한국어가 포함되면 encoding="utf-8" 명시를 권장
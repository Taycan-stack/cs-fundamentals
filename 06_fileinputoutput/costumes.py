# Binary files and PIL

# "Binary File" 이란?
# 모두 txt or csv 파일만 다뤄보았는데, 컴퓨터가 저장하는 방식인 binary file에 대해 배움

# PIL (Python Imaging Library)
# 이미지(그림)파일을 다루려면 파이썬 기본만으로는 어렵기에 PIL이라는 외부 라이브러리를 다룸.

# 이미지 열기 (Image.open)
# 이미지 저장 (.save)
# 여러 이미지를 하나로 묶기 (GIF 만들기)
# 이미지 크기 조정, 필터, 회전 등

import sys # 시스템 관련 모듈 제공
from PIL import Image # 

images = []

for arg in sys.argv[1:]: # 터미널에서 입력한 인자(arguments)를 리스트로 저장, [1:]은 슬라이싱. costumes.py를 제외하고 뒤의 파일 이름들만 가져옴
    image = Image.open(arg) # 내부적으로 이진 데이터(binary data)를 읽음
    images.append(image) # 이미지 객체를 리스트에 추가.

# GIF(Graphics Iterchange Format) 만들기
images[0].save(
    "costumes.gif",              # 새로 저장할 파일 이름
    save_all=True,               # 여러 이미지를 다 저장
    append_images=[images[1]],   # 이어붙일 이미지 목록
    duration=200,                # 프레임 간 시간(ms)
    loop=0                       # 0 → 무한 반복
)


# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# 절대주소를 이용하여 파일위치 열기
# 맥 vs 윈도우
# 맥에서는 / 인반면 윈도우에서는 \로 표시되어있음.

# with open("/Users/jungb/Documents/new_file.txt") as file:
#     contents = file.read()
#     print(contents)

# C:\Users\jungb\PycharmProjects\DAY24 <- main.py 위치
# 상대주소를 이용하여 new_file.txt 파일 열기
# 상대주소: 현재 작업하고 있는 디렉토리와 관련
with open("../../Documents/new_file.txt") as file:
    contents = file.read()
    print(contents)





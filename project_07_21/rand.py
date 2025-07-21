from random import * # random 라이브러리 전체 import

# import random # random 라이브러리 import
# print(random.random()) # 0.0 ~ 1.0 미만 까지의 실수

# print(random()) # 0.0 ~ 1.0 미만 까지의 실수
# print(random() * 10) # 0.0 ~ 10.0 미만 까지의 실수
# print(random()* 10 + 3) # 3.0 ~ 13.0 미만 까지의 실수
# print(int(random() * 10 + 3)) # 3 ~ 13 미만 까지의 정수
# print(randrange(1, 15)) # 1 ~ 15 미만 까지의 정수
# print(randint(1, 15)) # 1~ 15 이하 까지의 정수

# random을 이용해서 컴퓨터와 가위바위보 게임

select = int(input("가위 = 0, 바위 = 1, 보 = 2 : "))

rand = randint(0,2)

if (select == 0 & rand == 2) | (select == 1 & rand == 0) | (select == 2 & rand == 1):
    print(f"당신 : {select}, COM = {rand}, 이겼습니다.")
elif (select == 0 & rand == 1) | (select == 1 & rand == 2) | (select == 2 & rand == 0):
    print(f"당신 : {select}, COM = {rand}, 졌습니다.")
elif select == rand:
    print(f"당신 : {select}, COM = {rand}, 비겼습니다.")
else:
    print("정수형의 0, 1, 2만 입력해주세요.")
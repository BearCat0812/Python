# 조건문
# if, else, elif
# if 조건식 :
#   실행할 코드

# age = 20
# if age > 19:
#     print("성인입니다.")
# else:
#     print("미성년입니다.")

# 삼항 연산
# 참 if 조건 else 거짓

# print("성인" if age>=19 else "미성년")

# 1. 짝수 / 홀수 판별
# input으로 입력받은 수가 짝수면 짝수입니다 출력, 홀수면 홀수입니다. 출력

num = int(input("숫자를 입력해주세요. : "))

if num % 2 == 1:
    print("홀수입니다.")
elif num % 2 == 0:
    print("짝수입니다.")
elif num == 0:
    print("0입니다.")
else:
    print("수가 아닙니다.")

    
# 2. 양수 / 음수 / 0 판별
# input으로 입력받은 수가 양수, 음수, 0에 따라 양수, 음수, 0입니다. 출력

num = int(input("숫자를 입력해주세요. : "))

if num > 0:
    print("양수입니다.")
elif num < 0:
    print("음수입니다.")
elif num == 0:
    print("0입니다.")
else:
    print("수가 아닙니다.")

# 3. 비밀번호 확인
# input으로 입력받은 비밀번호가 "1234"와 같으면 성공 아니면 실패 출력

password = 1234

num = int(input("비밀번호를 입력해주세요. : "))

if password == num:
    print("성공")
else:
    print("실패")
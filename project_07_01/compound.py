# 복리 계산 수식
# A = P * (1 + r / n) ^ t
# A : 최종 금액 (원금 + 이자)
# P : 초기 원금
# r : 연이율
# n : 연간 복리 계산 횟수
# t : 시간 (연 단위)
#  원금과 이자율과 예금 기간은 사용자로부터 입력받기
# pow(x, y) : x의 y제곱

try:
    P = float(input("초기 원금을 입력하세요 : "))
    r = float(input("연 이율을 입력해주세요 : "))
    n = float(100)
    t = float(input("시간을 입력해주세요. (연 단위) : "))

    A = P * pow((1 + r / n), t)
    print(A)
except:
    print("숫자만 입력해주세요.")
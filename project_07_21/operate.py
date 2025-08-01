# 산술 연산
print("5 + 2 = ", 5 + 2) # 더하기
print("5 - 2 = ", 5 - 2) # 빼기
print("5 * 2 = ", 5 * 2) # 곱하기
print("5 / 2 = ", 5 / 2) # 나누기 몫 (실수형)
print("5 // 2 = ", 5 // 2) # 나누기 몫 (정수형)
print("5 % 2 = ", 5 % 2) # 나누기 나머지
print("5 ** 2 = ", 5 ** 2) # 거듭제곱

# 비교 연산 => 결과 값이 bool 타입이다. => bool 타입을 반환한다.
print("5 > 3 = ", 5 > 3) # 크다
print("5 < 3 = ", 5 < 3) # 작다
print("5 >= 3 = ", 5 >= 3) # 크거나 같다
print("5 <= 3 = ", 5 <= 3) # 작거나 같다
print("5 == 3", 5 == 3) # 같다
print("5 != 3", 5 != 3) # 다르다

# 논리 연산
# 소문자로만 and, or 작성. 대문자 X
print(5 > 3 and 5 < 3) # and 연산 : 앞 조건과 뒷 조건 둘 다 True일 경우 True
print(5 > 3 or 5 < 3) # or 연산 : 앞 조건과 뒷 조건 둘 중 하나라도 True일 경우 True

# 대입 연산
# 산술 연산 = 형태 (누적)
a = 1
a += 1 # a = a + 1
print("a = ", a)
a *= 2 + 3 # 우선순위 따라서 처리
print(a)

# 비트 연산
# &, |
# 숫자 => 2진수
print(5 & 3) # and 비트 연산 101 & 011 => 001
print(5 | 3) # or 비트 연산 101 | 011 => 111

# 쉬프트 연산
# >>, <<
# 숫자 => 2진수 => n만큼 좌, 우로 이동
print(5 >> 3) # 5 => 101 => 오른쪽으로 3칸 이동 : 2^n제곱 만큼 나누기
print(5 << 3) # 5 => 101 => 왼쪽으로 3칸 이동  : 2^n제곱 만큼 곱하기
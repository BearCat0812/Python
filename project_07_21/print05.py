# f-string을 이용한 고급 포매팅

# 1. 천 단위 구분 쉼표 넣기
# 1000000 => 1,000,000
money = 1000000
print(f"{money:,}")

# 2. 소수점 자릿수 지정
pi = 3.1415926535
print(f"{pi : .2f}")

# 3. 정렬 및 폭 지정
n = 42
print(f"{n:>05}") # 오른쪽 정렬
print(f"{n:<05}") # 왼쪽 정렬
print(f"{n:^5}") # 가운데 정렬

# 4. 빈 자리 채우기
print(f"{n:*>5}") # *로 빈칸을 채우고 폭 5칸 오른쪽 정렬

# 5. 백분율(비율)
rate = 0.033
print(f"{rate:.1%}")

# 6. 진수 변환
n = 255
print(f"10진수 {n}")
print(f"2진수 {n:b}")
print(f"8진수 {n:o}")
print(f"16진수 {n:x}")
print(f"16진수 {n:X}")
# for 변수 in 범위
# 범위 = range()
for i in range(3): # range(값): 0 ~ 값 미만까지 정수를 반복
    print(i)

for i in range(1, 5): # range(시작, 끝): 시작부터 끝 미만까지 정수를 반복
    print(i)

for i in range(0,6,2): # range(시작, 끝, 스텝): 시작부터 끝 미만까지 스텝만큼 정수를 반복
    print(i)

# if 조건문에서 in은 요소에 포함이 되어있는지 확인

a = [1, 2, 3, 4, 5]
if 1 in a:
    print("a 안에 1이 있습니다")
else:
    print("a 안에 1이 없습니다")

s = "ABC"
if "A" in s:
    print("A가 s안에 있습니다.")
else:
    print("A가 s안에 없습니다.")

for i in range(1, 10):
    if i == 3:
        # break # 현재 반복문을 종료한다.
        # continue # 해당 반복을 건너뜀.
         pass # 아무것도 하지않음.
    print(i)

# 2중 반복문 => for문 2개
# 바깥 반복횟수 * 안쪽 반복횟수 만큼 반복 ex) 3 * 3 = 9번
for i in range(3):
    for j in range(3):
        print(j)

# 2중 반복문을 이용해서 구구단 출력 코드 작성

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} X {j} = {(i * j) : >2}", end = "   ")
    print()
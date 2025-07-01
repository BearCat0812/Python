a = "HelloPython"

print(a[:5])  # print(a[0:5])
print(a[5:])  # print(a[5:11])
print(a[-1])
print(a[-5:-1])

# 문자열 포맷팅
# 1. + 연산자를 이용해서 문자열을 연결
name = "이동준"
age = "27"
print("1. "+ name + "은 " + age + "살 입니다.")

# 2. % 키워드 사용 : %s = 문자열, %d = 정수
print("2. %s은 %s살 입니다." % (name, age))

# 3. format
print("3. {0}은 {1}살 입니다." .format(name, age))

# 4. f 키워드 사용
print(f"4. {name}은 {age}살 입니다.")

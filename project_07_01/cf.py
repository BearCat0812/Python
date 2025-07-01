# 섭씨 -> 화씨 : (섭씨*9/5)+32 = 화씨
# 1. 입력 문자를 받는다. (c or f)
# 2. 입력 문자가 c 또는 f가 아니면 둘 중 하나만 입력하라고 출력
    # if corf != "c" and corf != "f"
# 3. 온도를 입력 받는다
# 4. 입력 받은 문자가 c 면 화씨로 변환하고 f 면 섭씨로 변환
# 5. 변환된 온도를 출력

corf = input("c or f? : ")
if corf == "c":
    c = float(input("온도를 입력해주세요. : "))
    f = (c * 9 / 5) + 32
    print(f"{f}F")
elif corf == "f":
    f = float(input("온도를 입력해주세요. : "))
    c = (f - 32) * 5 / 9
    print(f"{c}C")
else:
    print("c 또는 f만 입력해주세요.")
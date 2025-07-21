# dictionary : 키와 값으로 이루어진 자료형, 자바스크립트의 객체(object), JSON과 비슷하다
# key-value로 구성된다
# 순서가 존재하지 않지만 key를 이용해서 value 접근 가능
# {} 감싸진 형태지만 : 이용해서 key와 value를 구분지어서 저장

# a = {
#     "name" : "Bear Cat",
#     "age" : 27,
#     "address" : "Sema"
# }

# print(a)
# print(type(a)) # dictionary의 타입은 dict

# 요소의 접근은 key를 이용한다. => 딕셔너리이름[키] 로 요소 접근
# print(a["name"])

# 요소의 변경
# a["name"] = "kim"
# print(a["name"])

# update() : 요소 변경
# a.update({"name":"BC"})
# print(a["name"])

# key 출력
# for key in a.keys():
#     print(key)

# value 출력
# for val in a.values():
#     print(val)

# items() : key, value를 튜플로 묶어서 출력
# for key, val in a.items():
#     print(key, val)

# 문제 1. 리스트로 학생 성적 평균 구하기 80, 95, 70, 100, 85

# score = [80, 95, 70, 100, 85]
# print(sum(score)/len(score))

# 문제 2. 딕셔너리로 전화번호부 만들기 사람의 이름을 = key, 전화번호 = value => input으로 이름을 검색하면
# 검색한 이름에 해당하는 전화번호 출력

num = {
    "Bear Cat" : "010-8003-0881",
    "곰냥" : "010-1234-5678"
}

a = input("이름을 입력해주세요. : ")

if a in num.keys():
    print(f"{a}의 전화번호는 {num[a]} 입니다.")
else:
    print("존재하지 않는 이름입니다.")
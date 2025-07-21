# 자료구조 : List, Tuple, Set, Dictionary
# 1. List : 순서 O, 중복 O, 가변
# 2. Tuble : 순서 O, 중복 O, 불변
# 3. Set : 순서 X, 중복 X, 가변
# 4. Dictionary : 키-값 쌍으로 이루어짐, 키는 중복 X, 값은 중복 O, 가변

# 1. List
# 형태 []로 감싸진 형태
a = ["사과", "배", "딸기", "포도", "수박"]
b = list(range(1, 10))
c = list(["사과", "딸기", "포도"])

# 리스트의 요소에 접근 => 인덱스를 이용, 요소는 0번부터 시작
print(a[0]) # 사과

# 리스트 슬라이싱
print(a[:3]) # ["사과", "배", "딸기"]
print(type(a[:3]))
 
b[:3] = ["복숭아", "체리"]
print(b)

# 리스트 요소 추가
# 리스트.append() : 리스트 끝에 요소 추가
a.append("망고")
print(a)

# insert()
# 리스트의 특정 위치에 요소 추가
a.insert(2, "오렌지")
print(a)

# pop() : 리스트의 마지막 요소 삭제 => 삭제된 요소를 반환
d = a.pop()
print(d)

# del : 리스트의 인덱스를 이용해서 삭제 => 삭제된 요소를 반환 X
del a[0]
print(a)

# clear() : 리스트 전체를 지움 - 단, 객체는 남아있다.
a.clear()
print(a)

# 리스트 컴프리핸션
su = [x for x in "ABCD"]
print(su)

# 집계 함수
# 합계 sum
d = list(range(1, 11))
print(sum(d))
# 최댓값 max
print(max(d))
# 최솟값 min
print(min(d))

# 단순 합치기
print(d + b)

# extend() : 리스트 합치기
b.extend(d)
print(b)

# count() : 해당 요소가 리스트 안에서 몇 개 있는지 갯수를 반환
print(b.count(4))
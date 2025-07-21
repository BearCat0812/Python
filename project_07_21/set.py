# set 중복되지 않은 요소들로 이루어진 집합 자료형
# 순서가 없기에 인덱스를 이용해서 접근 불가능
# set 내부 요소를 수정할 수 없다
# 중복 요소가 있을 경우 하나의 요소만 표현한다.
# {}로 감싸진 형태

a = {"apple", "banana", 0, True, False}
print(a) # False가 없어짐 : 0하고 중복되기 때문

# set 요소 추가
a.add("orange")
print(a)

# update() : 여러 개의 요소를 한꺼번에 추가
b = {"kiwi", "melon", "grape"}
a.update(b)
print(a)

# remove() : 없는 요소를 삭제할 경우 에러 발생
# 반드시 존재하는 값만 제거하고자 할 때 => 예외 처리 하고 싶을 때
# a.remove("kiwi")
print(a)

# discard() : 없는 요소를 삭제할 경우 에러 발생 X
a.discard("orange")
a.discard("strawberry")
print(a)

# pop() : 마지막 요소가 삭제되나, 순서가 없기 때문에 랜덤한 요소가 삭제된다고 봐야한다.
a.pop()
print(a)

b = {"사과", "바나나"}
c = {"사과", "체리", "바나나"}

# union(), | : 합집합
print(b.union(c))
print(b | c)

# intersection(), & : 교집합
print(b & c)
print(b.intersection(c))

# difference(), - : 차집합
print(c.difference(b))
print(c - b)
# list, tuple, set, dict

# 1. list
# 가변, 중복 O, 순서 O

fruits_list = [1, 2, "apple", 3, "banana", 4]
print(fruits_list)
print(fruits_list[2])

# list 요소 추가
# list 이름.append(값)

fruits_list.append(5)
print(fruits_list)

# list 요소 제거
# list 이름.remove(값)

fruits_list.remove(1)
print(fruits_list)

# list에 원하는 위치에 값을 추가
# list 이름.insert(위치, 값)

fruits_list.insert(0, 1)
print(fruits_list)

# list 마지막 요소 제거
# list 이름.pop()

fruits_list.pop()
print(fruits_list)

# 2. tuple
# 불변, 중복 O, 순서 O

fruits_tuple = (1, 3, 5, "apple", "banana", 1, 3, 5)
print(fruits_tuple)
print(fruits_tuple[3])
# fruits_tuple[3] = 7 # error

# 3. set
# 가변, 중복 X, 순서 X

fruits_set = {"apple", "banana"}
print(fruits_set)

# set 요소 추가
# set 이름.add(값)

fruits_set.add(0)
print(fruits_set)

# set 요소 제거
# set 이름.remove(값)

fruits_set.remove(0)
print(fruits_set)

# 불변성을 지닌 set => frozenset

fruits_frozenset = {"apple", "banana"}
print(fruits_frozenset)

# 4. dict
# 가변, 키-값 쌍으로 이루어짐, 키는 중복 X, 값은 중복 O, 순서 X

fruits_dict = {"1": "apple", "2": "banana"}
print(fruits_dict["1"])
print(fruits_dict)

# dict 요소 추가

fruits_dict["3"] = "grape"
print(fruits_dict)

# dict 마지막 요소 제거
# dict 이름.popitem()

# dict 전체 삭제
# dict 이름.clear()
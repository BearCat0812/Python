# 함수 : 자주 사용하는 코드를 하나의 이름으로 묶어놓은 형태
# def 키워드 사용
# def 함수명(매개변수): 코드
def my_func():
    print("Hello Python")

my_func()

def my_func2(a,b):
    print(a,b)
my_func2("Hello",5)

# 매개변수가 몇개가 올지 모를 때
# * 사용 => 매개변수의 타입이 튜플
def my_func3(a,*b,c):
    print(f"a={a}, b={b}, c={c}")
my_func3(1,2,3,4,5,c=6)

# ** => 매개변수의 타입이 딕셔너리(dict)
def my_func4(**a):
    print(a)
my_func4(age=21, name="kim")

def my_func5(a,b=5):
    print(a+b)
# def my_func5(a,b):
#   b = 5
#   print(a+b)
my_func5(1,3)
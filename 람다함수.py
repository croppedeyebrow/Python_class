# 람다 (함수)란 : 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현 한 것 입니다.
# 파이썬에서 람다 함수를 통해 이름이 없는 함수를 만들 수 있음.
# 람다 함수의 장점은 코드의 간결함, 메모리의 절약이라고 생각할 수 있습니다.
# 컴파일러나 인터프리터가 해석가능하면 생략.

def add(a, b) :
    return  a + b
print(add(1,2))

print((lambda a,b : a+b)(1,2))


#함수의 매개변수로 함수 전달 하기.
def call_times(func) :
    for i in range(10) :
        func()

def print_hello() :
    print(f"Hello^^")


call_times(print_hello)


# filter() 함수와 map()함수
# filter(함수, 리스트) : 리스트의 요소를 함수에 넣고 리턴값이 True인 것으로 새로운 리스트 구성.
# map(함수, 리스트) : 리스트의 요소를 함수에 넣고 새로운 리스트를 구성해주는 함수


def power(n) :   #함수를 선언하는 방법
    return n * n

in_ = [1,2,3,4,5]

out_ = list(map(power,in_))
print(out_)

##위에꺼를 람다식으로 바꾸어 변수에 대입하는 방법.
power_l =lambda n: n*n

in_ = [1,2,3,4,5]

out_ = list(map(lambda n: n*n,in_)) # 함수 자리에 람다식으로 익명의 함수를 만들어 넣는 방법.
print(out_)



#리스트에 람다 함수를 넣는 방법도 가능.
my_list = [lambda  a, b : a*b, lambda a,b : a+b]
print(my_list[0](1,2))
print(my_list[0](2,3))




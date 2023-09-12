# 오버라이딩 : 부모 클래스를 상속 받아 동일한 메소드에 대해 재정의해 사용하는 것을 오버라이딩


# 함수로 오버로딩과 동일한 효과를 낼 수 있기에, 오버로딩이 딱히 필요하지 않음.
def sum(num1, num2) :
    return  num1 + num2

print(sum(100, 200))
print(sum("korea", "seoul"))


def sum(num1, num2, num3=100) :
    return  num1 + num2 + num3

print(sum(100, 200 ))
print(sum(100, 200, 300))
#print(sum("korea", "seoul"))
#  관계 연산자  :  AND(&&) => and,   OR(||) => or,   NOT(!) => not

x = 10
y = 20
z = 30

rst1 = x > 0 and x > y  #False
# print(rst1)
rst2 = x > 0 or x > y  #True
rst3 = not(x > 0 or x > y)  #False

print(rst1, rst2, rst3, sep="\t")


######


#  다항(3항)연산자
num = int(input("정수 입력 : "))
rst = (num % 2 ==0) and "짝수" or "홀수"
print(f"{num}은 {rst}입니다.")


# 2진수 입력 받기 (0b)
number = 0b101010101   #뒤에는 1과 0만 올 수 있음.
# 8진수 입력 받기 (0o)
number = 0o1234567
# 16진수 입력 받기 ( 01234556789abcdef ) (0x)
number = 0xffffff
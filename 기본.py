print("Hello, world")
print('Hello, world')
print(100)
print(33.33)
print(100+23)

#파이썬은 스네이크 표기법,  변수 선언할 때 $ 사용 불가.
# 변수를 선언하고 값을 대입.
num = 100   # 데이터형은 값이 대입되는 순간에 결정 난다.
print(num)
num = "100"
# 여기는 주석 입니다.- 단일 주석 표기
""" 
여기는 범위 주석 구간 입니다. 
"""

# 변수 활용
name = "곰돌이사육사"
email = ("jks2024@gmail.com")
age = 25
addr = "서울시 강남구 역삼동 KH정보교육원"

print(f"""
이름 : { name }
이메일 : { email }
나이 : { age }
주소 : { addr }
""")

# 파이썬은 불린 값(참/거짓)이 대문자로 시작된다.
is_adult = True

#파이썬은 들여쓰기로 줄를 안지키면 오류 발생. 줄이 정확하게 맞아야 함.
if is_adult :
    print("나는 성인 입니다.")
else :
    print("나는 성인이 아닙니다.")

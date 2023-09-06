#파이썬의 다양한 출력 방법
name = "곰돌이사육사"
age = 20
gender = "남성"
jobs = "소프트웨어 개발자"
addr = "서울시 강남구 역삼동 포스코타워"


# 파이선 스타일 : 3.6 이전 방법.
print("="*5, "파이썬 3.6 이전 스타일", "="*5)
print("이름 : {}". format(name))
print("이름과 주소 : {}". format(name, addr))
print("나이 : {}".format(age))

# 파이썬 현재 스타일 : 3.6 이후 방식. f와 {} 사용해서 출력하는 방식.
print("="*5, "파이썬 3.6 이후 스타일", "="*5)
print(f"이름 : {name}")
print(f"나이 : {age}, 성별 :{gender}, 직업 {jobs}")




print(38)   # 정수형
print("문자열")  #문자열
print([1,2,3])  #리스트형
print(1+3)
#  print(1+"3")  #문자와 숫자를 이어붙이는 것은 불가
print("파"+"이"+"썬")  #문자열 이어 붙이기
print("파""이""썬")
print("파","이","썬")  #콤마를 구분자(seperate) 취급한다. 기본적으로 한칸의 공백을 가지고 있음
print("파\n\n\n이\t\t썬")  #\n 줄바꿈, \t 탭



# 작은 따옴표 3개를 사용해도 동일 함, 여러줄 연속 사용, \사용으로도 동일 효과 낼 수 있음
print("""동해물과 백두산이 마르고 닳도록 하느님이
보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전 하세
""")

# 큰 따옴표, 작은 따옴표 화면에 표시 하기
print("안녕하세요라고 \"곰돌이사육사\"가 말했습니다.")

# 이스케이프 문자 사용 하기
print("서울시\t강남구\t역삼동\n")

print("-----------------------------------")

# end와 sep 옵션.
# end : 출력문에서 끝에 자동으로 삽입되는 문자를 지정하는 옵션 : 기본은 \n
# sep : 출력문의 중간에 삽입되는 문자를 지정하는 옵션 : 기본은 space

print("Hello", end="$")
print("Hello", end="*")
print("Hello")

print("life", "is", "too", "short", sep="\\")
print("010","1234","5678", sep="-")

year = 2023
month = 9
day = 6
print(year,month,day, sep="/")



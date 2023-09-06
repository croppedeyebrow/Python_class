# 1. 정해진 형식으로 시간을 입력 받아서 출력하기
# 입력 형식 : 22:5:5 => 오후 10시 05분 05초

# hour, Min, sec = map(int, input("시간입력 : ").split(":"))
# if hour > 12:
#     hour -= 12
#     print(f"오후{hour:02}시{Min:02}분{sec:02}초")
# else:
#     print(f"오전{hour:02}시{Min:02}분{sec:02}초")

# 2번. 3개의 정수를 입력 받아서 최대값과 최소값 구하기.

#number_list = []
numbers = input("3개의 정수를 입력하세요. : ")
number_list = list(map(int, numbers.split(" ")))
print("입력한 정수 : " + str(number_list))

if len(number_list) == 3:
     max_num = max(number_list)
     min_num = min(number_list)
     print("최댓값은:", max_num)
     print("최솟값은:", min_num)
else:
    print("정확히 3개의 정수를 입력하세요.")




# 3번. 주민등록번호를 입력 받아서 생년월일, 성별, 나이 출력하기
# current_year = datetime.today().year


# jumin = input("-와 공백을 포함 16자리의 주민번호를 입력하세요 : ")
# print("입력한 주민번호 : ", jumin)
#
# gender = jumin[7]   # 성별
# year = jumin[:2]  # 출생년도
# mon = jumin[2:4]  # 월, 2번인덱스 4번인덱스 미만
# day = jumin[4:6]  # 일
#
# print("생년월일 : " + jumin[:6])
#
# print("태어난년도 : " + jumin[:2] + "년")
#
# from datetime import datetime
# current_year = datetime.today().year
#
# birth_year = int(jumin[:2])
# age = current_year - (1900+birth_year)
# print("올해의 나이는 : " + str(age) + "세" )
#
# if gender == "1" :
#     print("입영 대상자 입니다.")
# else :
#     print("병역 대상자가 아닙니다.")



# 4번. 갯수가 정해지지 않은 여러개의 정수를 입력 받아, 합계와 평균 구하기
#list를 사용
score = list(map(int,input("정수 : ").split()))
print(f"총점 : {sum(score)}")
print(f"평균 : {sum(score)/len(score)}")

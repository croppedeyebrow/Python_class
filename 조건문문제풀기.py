#1번 문제 : 세자리 정수를 입력 받은 후 가장 큰 수 찾기 (123 => 3)
# num = int(input("세자리 정수를 입력하세요 :  "))
# x = num // 100
# y = (num % 100) //10
# z = num % 10
# if x > y and x > z :
#         print(f"최댓값은 {x} 입니다.")
# if y > x and y >z :
#         print(f"최댓값은 {y} 입니다.")
# else:
#     print(f"최댓값은 {z} 입니다.")

##############################

#2번 문제 : 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
# 주간 근무 : 9620원
# 야간 근무 : 주간 시금 * 1.5
# 주간 근무 [1], 야간 근무[2]를 입력 하세요 :
# 근무 시간을 입력해 주세요 :
# 입력한 시간 동안 근무한 주간 또는 야간 급여는 ___원 입니다.


#1번방법.
daytime_pay = 9620
nighttime_pay = daytime_pay * 1.5

workpart = int(input("[1] 주간근무, [2] 야간근무 를 입력 하세요 :  "))
workhour = float(input("근무 시간을 입력해 주세요 :  "))

if workpart == 1 :
   day_total_pay = daytime_pay * workhour
   total_pay = day_total_pay
elif workpart == 2 :
    night_total_pay = nighttime_pay * workhour
    total_pay =night_total_pay



workpart_str = workpart ==1 and "주간" or "야간"

print(f"총 급여는{workhour}동안 근무한 {total_pay:.2f} 입니다.")


#2번방법.
# 근무타입 = int(input("주간근무[1], 야간근무[2]를 입력 하세요 :"))
# 근무시간 = int(input("근무 시간을 입력해 주세요 : "))
# if 근무타입 ==1 :
#     급여 = 근무시간 * 9620
# else :
#     급여 = 근무시간 *9620 * 1.5
#
# 근무타입문자열 = 근무타입 ==1 and "주간" or "야간"
# print(f"{근무시간}시간 동안 근무한 {근무타입문자열} 급여는 {급여}원 입니다.")


###############################

#3번 문제 : 문자열 추가하기
#2개의 문자열을 포인터 변수 s와k에,
#양의 정수를 정수형 변수 n에 각각 전달
# s 문자열의 뒷 부분의 n개 문자를 k문자열 앞에 끼워 넣는 코드 작성
# s: seoul
# k : korea
# n : 2
# 결과 : ulkorea


# s = input("s 문자열 :")
# k = input("k 문자열 :")
# n = int(input("정수 입력 : "))
# print(s[-n:] +k)
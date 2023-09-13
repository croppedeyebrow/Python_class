#입력.
# 첫째 줄에는 테스트 케이스의 개수 C
# 둘째 줄부터, 학생의수 N(1<=N<=1000)이 첫수, 이어서 N명의 점수(0이상,100이하) 나열.

# 5  ==> 총 테스트 횟수
# 5 50 50 70 80 100   ==> 각 케이스마다 평균이 넘는 % 구하기
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91

#출력.
# 각 테스트 케이스 중 평균을 넘는 학생들의 비율을 반올림하여, 소수점 셋째 자리까지 출력.


def over_rate()  :  # 각 케이스에서 평균이 넘는 비율 구하기.
    ls = list(map(int,input().split()))  # 공백 기준으로 입력 받아서 정수형 리스트로 담음.
    average = sum(ls[1:])/len(ls[1:]) # 리스트에서 맨 앞의 요소는 인원수 이므로 제외, 총합/인원수 = 평균
    cnt = 0 #평균이 넘는 %를 구하기 위해서는, 인원에 대한 카운트가 필요.
    for i in range(1,len(ls)) : #맨 앞의 요소는 인원수 이므로 제외 함.
        if ls[i] > average : cnt += 1
    return cnt/ (len(ls)-1) *100  #백분율 표기로 변경

n = int(input())  # 총 테스트 횟수
rst = [] #각 케이스에 대한 결과값을 받기 위한 리스트.
for i in range(n) : # 총 테스트 횟수 만큼 반복 수행.
    rst.append(over_rate())

for e in rst :
    print(f"{e:.3f}%")



# total_case = int(input("테이트 케이스 총 횟수를 입력하세요 :  "))
# results = []
#
# for _ in range(total_case) :
#     student = list(map(int,input("테스트에 참여한 학생 수를 입력하세요 : ").split()))
#     N = student[0]
#     scores =student[1:]
#     total = sum(scores)
#     score_average = total/ N
#
#     count = 0
#     for score in scores :
#         if score > score_average:
#             count +=1
#
#     good_ratio =(count/N) * 100
#     results.append(good_ratio)
#
# for i, result in enumerate(results) :
#  print(f"평균을 넘은 학생들의 비율은 {result:.3f}% 입니다.")


############################

#함수형.

# def calculate_above_average_percentage(total_case):
#     results = []
#
#     for _ in range(total_case):
#         student = list(map(int, input("테스트에 참여한 학생 수를 입력하세요 : ").split()))
#         N = student[0]
#         scores = student[1:]
#         total = sum(scores)
#         score_average = total / N
#
#         count = 0
#         for score in scores:
#             if score > score_average:
#                 count += 1
#
#         good_ratio = (count / N) * 100
#         results.append(good_ratio)
#
#     return results
#
# def main():
#     total_case = int(input("테이트 케이스 총 횟수를 입력하세요 : "))
#     results = calculate_above_average_percentage(total_case)
#
#     for i, result in enumerate(results):
#         print(f"평균을 넘은 학생들의 비율은 {result:.3f}% 입니다.")
#
# if __name__ == "__main__":
#     main()




#입력.
# 첫째 줄에는 테스트 케이스의 개수 C
# 둘째 줄부터, 학생의수 N(1<=N<=1000)이 첫수, 이어서 N명의 점수(0이상,100이하) 나열.

#출력.
# 각 테스트 케이스 중 평균을 넘는 학생들의 비율을 반올림하여, 소수점 셋째 자리까지 출력.


total_case = int(input("테이트 케이스 총 횟수를 입력하세요 :  "))
results = []

for _ in range(total_case) :
    student = list(map(int,input("테스트에 참여한 학생 수를 입력하세요 : ").split()))
    N = student[0]
    scores =student[1:]
    total = sum(scores)
    score_average = total/ N

    count = 0
    for score in scores :
        if score > score_average:
            count +=1

    good_ratio =(count/N) * 100
    results.append(good_ratio)

for i, result in enumerate(results) :
 print(f"평균을 넘은 학생들의 비율은 {result:.3f}% 입니다.")


############################

# C = int(input())  # 테스트 케이스 개수 입력
#
# for _ in range(C):
#     scores = list(map(int, input().split()))  # 각 테스트 케이스의 점수 입력
#     N = scores[0]  # 학생 수
#     total = sum(scores[1:])  # 점수 총합
#     average = total / N  # 평균
#
#     count = 0
#     for score in scores[1:]:
#         if score > average:
#             count += 1
#
#     ratio = (count / N) * 100
#     print(f'{ratio:.3f}%')





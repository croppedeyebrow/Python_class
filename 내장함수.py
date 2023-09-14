# 내장 함수 : 파이썬이 기본적으로 제공, import가 필요 없음


# 큰값 작은 값 찾기

# print(max(1,2,3,4,56,67,777,88,99,100))
# print(min(1,2,3,4,56,67,777,88,99,100))
#
#
#
# #총 합 구하기.
# print(sum([1,2,3,4,56,67,777,88,99,100])) # 리스트의 총 합
# print(sum((1,2,3,4,56,67,777,88,99,100))) # 튜플에 대한 총 합
# num = list(map(int,input("정수값 입력 : ").split()))
# print(f"입력 받은 수의 총 합 : {sum(num)}")
# print(f"입력 받은 수의 평균 : {sum(num)/len(num)}")
#
#
# # 몫과 나머지 구하기
print(f"몫과 나머지 : {divmod(10,4)}")   #튜플의 동작 원리

# 여러개의 값을 한번에 입력 받아 리스트로 만들기.
# 최대값,최소값,합계,평균, 몫과 나머지

#오름 차순 정렬
my_list = [1,2,3,4,56,67,777,88,99,100]
print(sorted(my_list))

#내림 차순 정렬
my_list = [1,2,3,4,56,67,777,88,99,100]
print(sorted(my_list,reverse=True))

number = list(map(int, input("여러개의 정수를 입력하세요 : ").split()))
print(f"입력 받은 수들의 총 합 : {sum(number)}")
print(f"입력 받은 수들의 평균 : {sum(number)/len(number)}")
print(f"입력 받은 수들의 최댓값 : {max(number)}")
print(f"입력 받은 수들의 최솟값 : {min(number)}")
print(f"입력 받은 수들의 합을 5로 나누었을때에 대한 몫과 나머지 : {divmod(sum(number),5)}")


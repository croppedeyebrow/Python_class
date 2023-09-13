#집합이란, 주로 중복 제거를 목적으로 자주 사용
#순서가 보장 되지 않음
#중복 불가
#mutable 특성을 가짐
#
# s1 = set([1,2,3,4,5])
# s2 = set([4,5,6,7,8])
#
# #요소의 중복 제거.
# s3 = set([1,2,3,4,5,1,2,3,4,5,1,2,3])
# print(s3)
#
#
# # 합집합  :집합에서 한군데만 존재하면 포함됨, 중복제거
# print(s1.union(s2))
# print(s1 | s2)
#
#
# #교집합 : 집합에서 양쪽 모두에 존재하는 요소만 선택
# print(s1.intersection(s2))
# print(s1 & s2)
#
#
# # 차집합 : 집합에서 앞에서 뒤를 빼서 남은 앞의 요소만 선택.
# print(s1.difference(s2))
# print(s1-s2)


# frozenset 생성
# frozen_set1 = frozenset([1, 2, 3, 4, 5])
# frozen_set2 = frozenset([4, 5, 6, 7, 8])
#
# # 결과 출력
# print("frozen_set1:", frozen_set1)
# print("frozen_set2:", frozen_set2)
# print("Union:", frozen_set1 | frozen_set2)
# print("Intersection:", frozen_set1 & frozen_set2)
# print("Difference:", frozen_set1-frozen_set2)



import random

input_count = int(input("로또 몇 장을 발급 하시겠습니까?"))
for _ in range(input_count) :
    nums = set()
    while True :
        num = random.randrange(1,46)
        nums.add(num)
        if len(nums) == 6 : break
    print(nums)



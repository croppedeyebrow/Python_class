# 응용 예제(2)
# 무작위 수를 공백으로 기준하여 입력받아, 홀수와 짝수로 리스트에 나누어 담아 출력 하는 문제.

# num = list(map(int,input("무작위 수를 입력하세요 :  ").split()))
#
# even_list = []
# odd_list =[]
#
# for i in num :
#     if i % 2 ==0 :
#         even_list.append(i)
#
#     else:
#         odd_list.append(i)
#
#
# print(f"짝수 리스트: {even_list}")
# print(f"홀수 리스트: {odd_list}")


# map : 전달 받은 갯수를 함수내부에서 가공해서 반환 ( 입력 개수와 반환 개수가 동일 )
# filter : 전달 받은 값을 함수내부에서 조건에 일치하는 것만 골라서 반환.




# filter 내장 함수와 lambda를 이용한 방법

num = list(map(int,input("입력 :  ").split()))
odd = list(filter(lambda e:e % 2 == 1, num))
even = list(filter(lambda e:e % 2 == 0, num))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")
#  for 요소 in 시퀀스 : 시퀀스의 각 요소를 순회하는데 사용 (자바의 향상된 for문과 동일)
# fruits = ["apple", "banana", "cherry", ["seoul", "korea"] ]
# print(fruits[3][1][0])
# for e in fruits :
#     print(e[0])
#
#
# str1 = "서울시 강남구 역삼동 kh정보교육원"
# for e in str1 :
#     print(e, end=" / ")

#for 변수 in range(시작값, 종료값, 증감값) :    #증감값을 안 넣으면 기본적으로 1
# n = int(input("정수를 입력 하세요 : "))
# sum = 0
# for i in range (1, n+1) :   #1 부터 n+1 미만
#     sum += i
# print(sum)

#for 문을 역순으로 반복하기
#
# for i in range(10, -1, -2) :   #10~0 까지 출력.
#     print(i)


#  이중 for문
# n = int(input("정수를 입력 하세요 : "))
# for i in range(0,n) :
#     for j in range(0,n) :
#         print("*", end=' ')
#         print()


# 구구단 찍기
# for i in range(2,10) :  #2단~9단
#     for j in range(1,10) :
#         print(f"{i} X {j} = {i*j}")
#         print()


#홀수/짝수 나누어 찍기
# n = int(input("정수 입력 : "))
# for i in range(0,n) :
#     for j in range(0,n) :
#         if j % 2 ==0 : print("$", end=' ')
#         else : print("*", end=' ')
#         print()


# 사각형 찍기
# 정수값을 n을 입력 받아 n*n 크기의 행렬의 출력하는 프로그램 작성
# 값은 1부터 시작.

# n = int(input("정수 입력 : "))
# for i in range(1,n*n+1) :
#     print(f"{i:5>3}", end= ' ')   #정렬사용.
#     if i % n == 0 : print()     # 줄바꿈 조건 설정.



#증가하는 별 찍기

# *
# **
# ***
# ****
# *****

# n = int(input("별 갯수 입력 :  "))
# for i in range(n) :
#     for j in range(i+1) :
#         print("*", end='  ')
#     print()


###################################


#감소하는 별 찍기
# * * * * *
# * * * *
# * * *
# * *
# *

# n = int(input("별 갯수 입력 : "))
# for i in range(n, 0, -1) :
#     for j in range(i) :
#       print("*", end=' ')
#     print()

# n = int(input("뒤집어진 역삼각형 : "))
# for i in range(n) :
#     for j in  range(n-i) :
#         print("*", end=' ')
#     print()



#반대방향 감소하는 별 찍기
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# n = int(input("뒤집어진 역삼각형(반대) : "))
# for i in range(n) :
#     for s in  range(i) :
#         print(" ", end=" ")
#     for j in range(n-i) :
#         print("*", end= " ")
#     print()


##########################


# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n = int(input("별 갯수 입력 : "))
# for i in range(n) :
#     for j in range(i):
#         print(" ", end= '')
#     for k in range(n-i) :
#         print("*", end=' ')
#     print()

# n = int(input("행 수를 입력하세요: "))
#
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end='')
#     for k in range(i):
#         print("*", end=' ')
#     print()

# n = int(input("역삼각형 : "))
# for i in range(n,0,-1) :
#     for s in range(n-i) :
#         print(" ", end="")
#     for j in range(i) :
#         print("*", end=" ")
#     print()


#################


# 문자와 ascii 코드
# chr : 유니코드 값을 입력 받아 그 코드에 해당하는 문자를 출력
# ord : 문자를 유니코드 값으로 변환
for i in range(ord("A"), ord("Z")+1) :
    print(chr(i), end=" ")
print()

for i in range(65, 91) :
    print(chr(i), end=" ")
print()


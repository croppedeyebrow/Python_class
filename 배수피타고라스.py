# 배수 찾기(초급)

# 첫째 줄에 n이 주어짐, 다음 줄 부터 값이 주어 짐
# 목록에 있는 수가 n의 배수인지 아닌지 판별
# 0을 입력하면 목록이 끝남.

#입력
# 3
# 1
# 7
# 99
# 321
# 777
# 0

#출력
# 1 is NOT a multiple of 3.
# 7 is NOT a multiple of 3.
# 99 is a multiple of 3.
# 321 is a multiple of 3.
# 777 is a multiple of 3.

# N = int(input("N값을 입력하세요. :  "))
# list = []
#
# while True :
#     arr_number = int(input("임의의 값들을 입력하세요 :  "))
#     if arr_number == 0:
#         break
#     list.append(arr_number)
#
# for arr_number in list :
#     if arr_number % N == 0 :
#         print(f"{arr_number} is a mutiple of {N}")
#     else:
#         print(f"{arr_number} is Not a multiple of {N}")
#
# ############
#
# n = int(input())
# ls = []
# while True :
#     x = (int(input()))
#     if x == 0: break
#     ls.append(x)
#
# for e in ls :
#     if e % n == 0 : print(f"{e} is a multiple of {n}.")
#     else:
#         print(f"{e} is NOT a multiple of {n}")



# 2. 피타고라스 정리(중급)
# 피타고라스의 정리 : 직각삼각형에서 빗변을 제외한 나머지 두변의 길이를
# 각각 제곱해 더하면 빗변의 제곱과 같다.
# 과거 이집트인들은 각 변들의 길이가 3,4,5인 삼각형이 직각 삼각형인것을 알아냈다
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
# 마지막 줄에는 0 0 0이 입력

#입력
# 6 8 10
# 10 8 6
# 25 52 60
# 5 12 13
# 0 0 0

#출력
# right
# right
# wrong
# right


# def is_right_triangle(a,b,c) :
#     a_squard = a**2
#     b_squard = b**2
#     c_squard = c**2
#
#     if (a_squard +b_squard == c_squard) or (b_squard+c_squard == a_squard) or (a_squard+c_squard == b_squard) :
#         return  True
#     else:
#         return False
# triangel_list =[]
#
# while True :
#     triangle_slides = list(map(int,input("세 변의 길이를 입력하세요 :  ").split()))
#
#     if triangle_slides == [0, 0, 0]:
#         break
#     triangel_list.append(triangle_slides)
#
#
#
# for triangle_slides in triangel_list :
#     triangle_slides.sort()
#     if is_right_triangle(triangle_slides[0], triangle_slides[1], triangle_slides[2]) :
#             print("right")
#     else:
#              print("wrong")

##########################

rst =[]
while True :
    li = list(map(int,input().split()))
    li.sort()
    if li[0] == 0 and li[1] ==0 and li[2] == 0 :break
    elif li[2] **2 == li[1] **2 ==li[0]**2 :
        rst.append("right")
    else:
        rst.append("wrong")

for e in rst : print(e)
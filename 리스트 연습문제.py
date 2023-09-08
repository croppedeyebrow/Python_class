#1번 문제 : 상근날드.
# 햄버거는 총 3종류 상덕버거, 중덕버거, 하덕버거가 있고, 음료는 콜라와 사이다 두 종류.
# 첫째 줄에는 상덕버거, 둘째 줄에는 중덕버거, 셋째 줄에는 하덕버거, 넷째 줄에는 콜라의 가격, 다섯째 줄에는 사이다의 가격
# 모든 가격 100원 이상, 2000원 이하.
# 가장 싼 세트 메뉴의 가격을 출력.

#1번풀이
# menuprice = []
#
# for i in range(5) :
#      price = int(input())
#      menuprice.append(price)
#
#
# min_burger = min(menuprice[:3])
# min_drink =  min(menuprice[3:5])
#
#
# print(f"가장 저렴한 세트메뉴 가격 : {min_drink+min_burger-50}")




#2번풀이.
# ls = list(map(int,input().split()))
#
# min_b = min(ls[:3])
# min_d = min(ls[3:5])
# print(f"{min_b+min_d-50}")






##########

#2번. 첫째 줄에 첫 번째 색, 둘째 줄에 두 번째 색, 셋째 줄에 세 번째 색이 주어진다. 위의 표에 있는 색만 입력으로 주어진다.
# 입력으로 주어진 저항의 저항값을 계산하여 첫째 줄에 출력한다.

# color = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")
# A_name=color.index(input())
# B_name=color.index(input())  # input()으로 입력 받은 문자열이 color 튜플내의 인덱스로 반환
# C_name=color.index(input())
# print(int(str(A_name)+str(B_name)) * (10**C_name))



##################################



#3번.
#1~100번 까지의 컴퓨터가 있음
#손님은 자신이 앉고 싶어하는 자리르 선택하고자 합니다. 이미 예약된 자리는 선택할 수 없으므로 거절.
# 거절횟수는?


#1번방법.
# seat_num = list(map(int,input().split()))
# pc = [0] * 100
# cnt = 0
# for e in seat_num : #향상된 for문이므로 e값을 고객이 앉고 싶어하는 좌석 번호
#     if pc[e-1] != 0: cnt += 1
#     else:pc[e-1] =1
# print(cnt)


#2번방법.

# user = int(input())
# c_seat = [0]*100
#
# use_seat = list(map(int,input().split()))
#
# rejected = 0
#
# for seat in use_seat :
#      if c_seat[seat] == 0:
#         c_seat[seat] =1
#      else:
#           rejected +=1
# print(f"거절 당한 손님의 수는 : {rejected} 입니다. ")





#####################################


#4번.
# : Knuth-Morris-Pratt => KMP, Mirko-Slavko => MS

upper_str = ""
for e in input() :  #입력 받는 개수만큼 자동 순회
    if e.isupper() : upper_str += e

print(upper_str)


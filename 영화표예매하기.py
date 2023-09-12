# 메뉴는 [1]예매하기, [2]종료하기
# 좌석은 10개
# 예매가 완료된 좌석은 값을 1로 변경.
# 한 좌석 당 예매 가격은 12000원

# customer = int(input())
# M_seat = [0]*10
# total_sales = 0
#
# while True :
#    print("메뉴를 선택하세요 : [1]예매하기 [2]종료하기")
#    choice = int(input())
#
#    if choice == 1 :
#        print("예매할 좌석 번호를 입력하세요 1번~10번")
#        check_seat = list(map(int,input().split()))
#
#        for seat in check_seat :
#             if 1 <=seat <= 10 :
#                 if M_seat[seat-1] == 0:
#                      M_seat[seat-1] =1
#                      total_sales += 1
#                      print(f"{seat}번 좌석 예약 완료")
#                 else:
#                      print(f"{seat}번 좌석은 이미 예약되었습니다.")
#             else:
#                  print("잘못된 좌석 번호입니다. 1~10번까지 다시 선택해주세요. ")
#    elif choice == 2 :
#        break
#
# total_payment =total_sales * 12000
#
# print(f"총 매출액은 : {total_payment} 입니다. ")



####################

#함수형 풀이.

TICKET_PRICE = 12000
seat = [0] * 10

#좌석 상태를 표시하는 메뉴 만들기
def print_seat() :
    for e in seat :  #향상된 for문으로 좌석의 갯수 만큼 순회
        if e == 0 : print("[ ]", end=" ") #판매 안된 좌석
        else : print("[v] ", end=" ")  #판매된 좌석
    print()

# 총 매출액 구하기
def amount() :
    cnt = 0
    for e in seat :
        if e ==1 : cnt+=1  #팔린 좌석의 총 갯수 구하기
    return  cnt * TICKET_PRICE

# 좌석 예약 하기.
def select_seat() :
    print_seat() # 현재 예약 가능한 좌석 보여주기
    num = int(input("좌석 번호를 선택 하세요 : ")) -1  # 선택된 좌석번호는 1부터 시작하고, 인덱스는 0부터 시작.
    if seat[num] == 0 :
        seat[num] =1
        print_seat()
    else:
       print("이미 예약된 좌석 입니다.")


while True :
   sel = int(input("[1]예매하기 [2] 종료하기 : "))
   if sel == 1 : select_seat()
   else:
        print(f"총 매출액 : {amount()}")
        break



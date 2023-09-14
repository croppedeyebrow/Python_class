#계좌 개설.

#변수는 이뮤터블 특성, 변경해주려면 전역변수(global)이 필요하다
#전역변수 추가 공부 필요.!
#리스트는 뮤터블 특성


def open_account(name) :
    print(f"{name}님의 계좌가 개설 되었습니다.")
    return name  #반환 값으로, 이름을 전달.

#입금 함수.
# def deposit(balance, input) : #잔고와 입금액을 매개변수로 전달 받음.
#     #global balance
#     #balance += input
#     print(f"{input}이 입금 되었습니다. 잔액은 {balance+input}입니다.")
#     return balance + input


def deposit(input) : #잔고와 입금액을 매개변수로 전달 받음.
      global balance
      balance[0] += input
      print(f"{input}이 입금 되었습니다. 잔액은 {balance[0]}입니다.")



#출금 함수.
# def withdraw(balance, output) :
#     #global  balance
#     if balance >= output :
#         #balance -= output
#         print(f"{output}이 출금 되었습니다. 잔액은 {balance-output}입니다.")
#         return balance - output
#
#     else:
#         print(f"출금이 실패 했습니다. 잔액은 {balance} 입니다.")
#         return  balance


def withdraw(output) :
    #global  balance
    if balance[0] >= output :
        #balance[0] -= output
        print(f"{output}이 출금 되었습니다. 잔액은 {balance[0]}입니다.")

    else:
        print(f"출금이 실패 했습니다. 잔액은 {balance[0]} 입니다.")

#


# balance = 0 #외부에서 선언했지만 매개변수로 전달하여 결과를 리턴 받음.
# name = open_account("눈썹")
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# print(f"{name}의 잔액은 {balance} 입니다.")


balance = [0] #외부에서 선언했지만 매개변수로 전달하여 결과를 리턴 받음.
name = open_account("눈썹")
deposit( 1000)
withdraw( 500)
print(f"{name}의 잔액은 {balance[0]} 입니다.")
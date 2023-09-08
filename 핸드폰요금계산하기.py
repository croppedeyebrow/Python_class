# 영식 요금제 : 30초에 10원
# 민식 요금제 : 60초에 15원


n = int(input()) #통화 횟수
call = list(map(int,input().split()))  #통화 횟수에 대한 통화 시간
#input으로 입력 받은 문자열을 split()을 이용해 공백기준으로 쪼개서, int형 자료로 변환시킨 후 map으로 정렬 후 list로 나열.

y_pay = m_pay = 0
for i in range(n) :
    y_pay += (call[i] // 30) *10 + 10
    m_pay += (call[i] // 60) *15 + 15

if y_pay > m_pay :
    print("민식", m_pay)

elif y_pay < m_pay :
    print("영식", y_pay)
else:
    print("민식,영식", y_pay)

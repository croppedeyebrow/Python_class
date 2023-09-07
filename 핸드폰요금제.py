# 영식 요금제 : 30초당 10원(1~29초에 10원, 30초가 되면 2통이 됨)
# 민식 요금제 : 60초당 15원(1~59초에 15원, 60초가 되면 2통이 됨)
# 첫번째 줄에 통화의 횟수(20 미만), 두번째 줄에 통화당 통화 시간(초단위)
# 출력은 싼 요금제를 출력 영식 요금제는 Y, 민식 요금제는 M
# 총 통화 요금이 같은 경우는 YM 총 통화요금 표시

n = int(input())
call = list(map(int,input().split()))

y_pay = m_pay =0

for i in range(n) :
    y_pay += (call[i] //30) *10 + 10
    m_pay += (call[i] //60) *15 + 15

if y_pay > m_pay :
    print("민식", m_pay)

elif y_pay < m_pay :
    print("영식", y_pay)
else:
    print("민식,영식", y_pay)


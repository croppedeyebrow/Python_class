# A = int(input("첫번쨰 자연수를 입력하세요. : "))
# B = int(input("두번쨰 자연수를 입력하세요. : "))
# C = int(input("세번쨰 자연수를 입력하세요. : "))

while True :
    NUMA = input("첫번쨰 자연수를 입력하세요. : ")
    if NUMA.isdigit() :
        NUMA = int(NUMA)
        if 99 < NUMA < 1000 : break
    print("입력 범위를 넘어섰습니다. 다시 입력하세요.")


while True :
    NUMB = input("두번쨰 자연수를 입력하세요. : ")
    if NUMB.isdigit() :
        NUMB = int(NUMB)
        if 99 < NUMB < 1000 : break
    print("입력 범위를 넘어섰습니다. 다시 입력하세요.")


while True :
    NUMC = input("세번쨰 자연수를 입력하세요. : ")
    if NUMC.isdigit():
        NUMC = int(NUMC)
        if 99 < NUMC < 1000: break
    print("입력 범위를 넘어섰습니다. 다시 입력하세요.")

result = NUMA * NUMB * NUMC

result_str = str(result)

for i in range(10) :
    print(result_str.count(str(i)))







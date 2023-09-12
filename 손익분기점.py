
# fixed_costs = float(input("고정비용을 입력하세요: "))
# variable_costs = float(input("가변비용을 입력하세요: "))
# selling_price = float(input("판매가를 입력하세요: "))
#
# print(fixed_costs, variable_costs,selling_price)
#
# # 손익분기점 계산
# if variable_costs >= selling_price:
#     print("손익분기점을 넘기 위한 판매량이 존재하지 않습니다.")
# else:
#     break_even_point = fixed_costs // (selling_price-variable_costs)+1
#     print(f"손익분기점은 {break_even_point:} 입니다.")


######################

fix,var,sell = map(int, input().split())
cnt = 0
while True :
    #if fix +(var*cnt) < sell * cnt : break
    if cnt > fix // (sell-var) : break
    cnt +=1

print(cnt)
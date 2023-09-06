# 출력 시 정렬
# < 좌측 정렬
# > 우측 정렬, 생략 가능
# ^ 중앙 정렬


print("|{:5}|".format(10))
print("|{:<5}|".format(10))
print("|{:^5}|".format(10))

num = 10
print(f"|{num:>5}|")
print(f"|{num:<5}|")
print(f"|{num:^6}|")

PI = 3.14159265
print(f"{PI:.4f}")   # 소수점 이하 자릿수 표기 (숫자f)
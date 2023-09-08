word = input()
max_length = 1000000
limited_string = word
for i in input():
    if i <= len(word) <= max_length:
        limited_string = word
    else:
        print("입력 문자열의 길이가 범위를 벗어납니다.")
        limited_string = word[:max_length]
print(limited_string)
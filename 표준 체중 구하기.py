def std_weight(height, gender) :
    if gender == "남성" :
        return height * height*22
    else :
        return height * height*21

height = 175
gender = "남성";
weight = round(std_weight(height/100,gender),2)
    #반올림 함수, 사사오입과는 다르게 동작.
    # 파이썬에서는 오사오입을 적용.
print(f"키{height}cm {gender}의 표준 체중은 {weight}kg 입니다.")

    
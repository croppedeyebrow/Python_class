name = input("이름을 입력하세요 : ")
while True :
    age = input("나이를 입력하세요 : ")
    if age.isdigit() :
        age = int(age)
        if 0 < age < 200 : break
    print("나이를 잘 못 입력하셨습니다. 다시 입력하세요.")

while True :
    gender = input("성별을 입력하세요 : ")
    if gender == "M" or gender == "m" : break
    elif gender == "W" or gender =="w" : break
    else:
        print("성별을 잘 못 입력하셨습니다. 다시 입력하세요.")

while True :
     job = input("직업을 입력하세요 : [1]학생, [2]회사원, [3]주부, [4]무직")
     if job.isdigit() :
         job = int(job)
         if 0 < job < 5 : break
     print("직업을 잘 못 선택하셨습니다. 다시 입력하세요.")

if gender == "M" or gender == "m" :
    gender_name = "남성"
elif gender == "W" or gender == "w" :
    gender_name = "여성"

job_name = (" ", "학생", "회사원", "주부", "무직")

print(f"이름은 {name} 입니다. ")
print(f"나이는 {age} 입니다. ")
print(f"성별은 {gender_name} 입니다. ")
print(f"직업은 {job_name[job]} 입니다. ")

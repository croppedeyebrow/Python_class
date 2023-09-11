knife = 10  #칼을 10자루 준비
def game(player) :
    global knife # 전역 변수
    knife -= player
    print(f"남아 있는 칼은 {knife}자루 입니다.")
    #return knife

player = int(input("경기에 참여하는 학생이 몇명 입니까? : "))
game(player)
print(f"경기에 사용하고 남은 칼은 {knife}입니다.")


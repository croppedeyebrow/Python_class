# 순차 검색
def search_list(a,x) :
    for i in range(len(a)) :
        if x == a[i] : return i
    return -1

v = [17,92,18,33,58,7,33,42]
print(search_list(v,33))
print(search_list(v,18))
print(search_list(v,100))
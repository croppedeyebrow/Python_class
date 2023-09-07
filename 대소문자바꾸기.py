
w = ""
for i in input():
    if i.islower() :
       w += i.upper()
    else:
       w += i.lower()

print(w)
class Vector2D :
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):    #+연산에 대응 됩니다.
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self,other) :
        return Vector2D((self.x * other.x) +100, (self.y * other.y)+100)

v1 = Vector2D(1,3)
v2 = Vector2D(4,4)

# print(100*200)
# print(100.1*200.1)

v3 = v1 * v2

print(v3.x, v3.y)




# self.x * other.x calculates the product of the x components of v1 and v2, which is 1 * 3 = 3.
# self.y * other.y calculates the product of the y components of v1 and v2, which is 2 * 4 = 8.
# Then, you add 100 to both the x and y components, resulting in 3 + 100 = 103 for the x component and 8 + 100 = 108 for the y component.
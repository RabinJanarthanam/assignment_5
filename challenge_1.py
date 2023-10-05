class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2

x=int(input("enter the x number:"))
y=int(input("enter the y number:"))
z=int(input("enter the z number:"))


p = Point(x,y,z)
result = p.sqSum()
print(result)  # Output should be 35

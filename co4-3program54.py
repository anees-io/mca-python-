class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def __lt__(self, other):
        area1 = self.__length * self.__width
        area2 = other.__length * other.__width
        return area1 < area2


l1 = int(input("Enter length of Rectangle 1: "))
w1 = int(input("Enter width of Rectangle 1: "))

l2 = int(input("Enter length of Rectangle 2: "))
w2 = int(input("Enter width of Rectangle 2: "))

r1 = Rectangle(l1, w1)
r2 = Rectangle(l2, w2)

if r1 < r2:
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 1 does not have smaller area")

class Shape:
    def what_am_i(self):
        print("ya figu")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width + self.len) * 2


class Square(Shape):
    def __init__(self, a):
        self.side = a

    def calculate_perimeter(self):
        return self.side * 4


a_rec=Rectangle(7, 5)
a_squ=Square(6)

a_rec.what_am_i()
a_squ.what_am_i()



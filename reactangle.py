class Shape():
    def __init__(self):
        pass
    def what_am_i(self):
        print("Я - фигура")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        print("Периметр прямоугольника:")
        return (self.width + self.len) * 2

class Square(Shape):
    def __init__(self, s1, s2, s3, s4):
        self.storona = s1
        self.storonb = s2
        self.storonc = s3
        self.storond = s4

    def perim(self):
        print("Периметр квадрата:")
        return self.storona + self.storonb + self.storonc + self.storond

    def change_size(self, n):
        self.num = n       
        self.storona = self.storona + n
        self.storonb = self.storonb + n
        self.storonc = self.storonc + n
        self.storond = self.storond + n



class Horse():
    def __init__(self, name):
        self.name = name

class Rider():
    def __init__(self, name, at):
        self.name = name
        self.at = at
        

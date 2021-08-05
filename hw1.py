class Windows:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def square(self):
        return self.x * self.y


class Rul:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def square(self):
        return self.x * self.y


class Room:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.windows = []
        self.rul = []

    @property
    def square(self):
        p = (self.x + self.z) * 2
        area = p * self.y
        for window in self.windows:
            area -= window.square
            self.area = area
        return area

    def add_window(self, x, y):
        self.windows.append(Windows(x, y))

    def add_rul(self, x, y):
        self.rul.append(Rul(x, y))

    @property
    def sum(self):
        for sq in self.rul:
            qwe = self.area // sq.square
        return qwe


r = Room(10, 5, 15)
print(r.square)
r.add_window(10, 5)
r.add_window(10, 5)
print(r.square)
r.add_rul(2, 5)
print(r.sum)

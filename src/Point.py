def main():
    test_point()

def test_point():
    p1 = Point(20, 30)
    p2 = Point(200, 150)
    p3 = Point(100, 30)
    p1.move_to(10, 20)
    p1.move_by(20, 60)
    print(p1.distance)
    print(p1.get_distance_traveled())
    print(p1.closer_to(p2, p3))
    print(p1.halfway_to(p2))

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.move = 0
        self.initial_x = x
        self.initial_y = y
        self.distance = 0

    def __repr__(self):
        value = "Point (" + str(self.x) + ", " + str(self.y) + ")"
        return value
    
    def move_to(self, dx, dy):
        dx = self.x - dx
        dy = self.y - dy
        d = (dx * dx + dy * dy) ** (1 / 2)
        self.x = dx
        self.y = dy
        self.move = self.move + 1
        self.distance = self.distance + d

    def move_by(self, dx, dy):
        d = (dx * dx + dy * dy) ** (1 / 2)
        self.x = self.x + dx
        self.y = self.y + dy
        self.distance = self.distance + d
        self.move = self.move + 1

    def get_number_of_moves_made(self):
        return self.move

    def clone(self):
        x = self.x
        y = self.y
        return Point(x, y)

    def get_distance_from(self, p2):
        dx = self.x - p2.x
        dy = self.y - p2.y
        d = (dx * dx + dy * dy) ** (1 / 2)
        return round(d, 3)

    def get_distance_from_start(self):
        dx = self.x - self.initial_x
        dy = self.y - self.initial_y
        d = (dx * dx + dy * dy) ** (1 / 2)
        return round(d, 3)

    def get_distance_traveled(self):
        return round(self.distance, 3)

    def closer_to(self, p1, p2):
        if self.get_distance_from(p1) > self.get_distance_from(p2):
            return p2
        if self.get_distance_from(p1) == self.get_distance_from(p2):
            return p2
        else:
            return p1

    def halfway_to(self, p):
        x = (self.x + p.x) / 2
        y = (self.y + p.y) / 2
        return Point(round(x, 3), round(y, 3))

main()

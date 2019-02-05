def main():
    test_point()

def test_point():
    p1 = Point(20, 30)
    p2 = Point(200, 150)
    p1.move(10, 20)
    p2.move(20, 60)
    print(p1)
    print(P2)

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moves = 0

    def __repr__(self):
        value = "Point (" + str(self.x) + ", " + str(self.y) + ") has moved: " + str(self.moves) + " times"
        return value
    
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        self.moves = self.moves + 1
        
main()
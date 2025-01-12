class Horse:
    x_distance = 0
    sound = 'Frrr'
    def __init__(self):
        super().__init__()

    def run(self, dx):
        self.dx = dx
        Horse.x_distance = self.x_distance+dx

class Eagle:
    y_distance = 0
    def __init__(self):
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.dy = dy
        Eagle.y_distance = self.y_distance+dy

class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print (self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
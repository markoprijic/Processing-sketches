flowers = []

class Flower:
    def __init__(self, x, y, radius, petal_count):
        self.x = x
        self.y = y
        self.radius = radius
        self.petal_count = petal_count
        self.angle = 0  # Initialize angle for animation
        self.speed = random(0.01, 0.05)  # Random rotation speed

    def draw_petal(self):
        angle = 360 / self.petal_count
        petal_color = color(random(255), random(255), random(255))

        for i in range(self.petal_count):
            pushMatrix()
            translate(self.x, self.y)
            rotate(radians(self.angle + i * angle))
            fill(petal_color)
            ellipse(0, self.radius, 40, 100)  # Adjust the petal shape here
            popMatrix()

    def move(self):
        self.angle += self.speed

def setup():
    size(400, 400)
    background(0)
    noStroke()

    x = width / 2
    y = height / 2

    for _ in range(10):
        radius = random(50, 150)
        petal_count = int(random(5, 12))
        flowers.append(Flower(x, y, radius, petal_count))

def draw():
    background(0)

    for flower in flowers:
        flower.draw_petal()
        flower.move()

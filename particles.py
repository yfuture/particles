import random

class Particle:
    def __init__(self, x, y, vx, vy, life):
        self.position = [x, y]
        self.velocity = [vx, vy]
        self.life = life
    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.life -= 0.5
        self.velocity[1] += 10
    def randomizer(self):
        self.velocity[0] += random.randint(-14,14)/5
        self.velocity[1] += random.randint(-15,0)
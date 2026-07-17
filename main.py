import pygame
import math


WIDTH, HEIGHT = 1280, 720
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("image.jpg")
pygame.display.set_caption("GRAVITY SIMULATOR")
clock = pygame.time.Clock()

running = True
G = 1000 
eps = 200

def apply_gravity(p, q):
    direction = q.pos - p.pos
    r = direction.length()

    direction = direction.normalize()  

    a_value = G * q.m / (r*r + eps*eps)
    p.a += direction * a_value
    

class Object:
    def __init__(self, name, color, x, y, m):
        self.name = name
        self.color = color
        self.pos= pygame.Vector2(x,y)
        self.a = pygame.Vector2(0, 0)
        self.vel = pygame.Vector2(0, 0)
        self.m = m
      # self.dx = 0
      # self.dy = 0
        self.trial = []
    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, 20)
        if len(self.trial) > 1:
            pygame.draw.lines(screen, self.color, False, self.trial, 2)
        # print(self.name, self.pos)
 
    def update(self, dt):
        self.vel += self.a * dt
        self.pos += self.vel * dt
        self.a *= 0
        self.trial.append(self.pos.copy())
        if len(self.trial) > 400:
            self.trial.pop(0)

object1 = Object("object1", "red", WIDTH * (1/3), HEIGHT * (2/3), pow(10, 4))
object2 = Object("object2", "blue", WIDTH * (2/3), HEIGHT * (2/3), pow(10, 4))
object3 = Object("object3", "green", WIDTH * (1/2), HEIGHT * (1/3), pow(10, 4))

objects = [object1, object2, object3]

while running:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000 #1000

    for obj in objects:
        obj.draw()
        for ob in objects:
            if obj != ob:
                apply_gravity(obj, ob)
        obj.update(dt)        

    pygame.display.update()
    
pygame.quit()

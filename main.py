import pygame
import math


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

radius = 40
color = 'red'
angle = 0
distance = 1
direction = 1

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
x = 0
y = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit")
            running = False

    x = screen.get_width() / 2 + distance * math.sin(math.radians(angle))
    y = screen.get_height() / 2 + distance * math.cos(math.radians(angle))
    player_pos = pygame.Vector2(x, y)

    screen.fill("black")
    pygame.draw.line(screen, 'red', (screen.get_width() / 2, screen.get_height() / 2), player_pos, 3)
    pygame.draw.circle(screen, 'red', player_pos, 40)
    if distance >= screen.get_height() - 350 or distance <= 0:
        direction = -direction
    angle += 1 * direction
    distance += 0.1 * direction
    pygame.display.flip()

pygame.quit()
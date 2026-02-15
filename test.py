import pygame
import random
import sys

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Dodge Game")

clock = pygame.time.Clock()

ball_y = 300
ball_x = 80

block_x = WIDTH
gap_size = 220
gap_y = random.randint(100, 300)

score = 0
running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        ball_y -= 5

    if keys[pygame.K_DOWN]:
        ball_y += 5

    if ball_y < 0:
        ball_y = 0

    if ball_y > HEIGHT - 20:
        ball_y = HEIGHT - 20

    block_x -= 4

    if block_x < -50:
        block_x = WIDTH
        gap_y = random.randint(100, 300)
        score += 1
        print("Score:", score)

    screen.fill((25, 25, 60))

    pygame.draw.circle(screen, (0, 255, 0), (ball_x, ball_y), 20)

    pygame.draw.rect(screen, (255, 0, 0), (block_x, 0, 50, gap_y))
    pygame.draw.rect(screen, (255, 0, 0), (block_x, gap_y + gap_size, 50, HEIGHT))

    if 60 < block_x < 100:
        if ball_y < gap_y or ball_y > gap_y + gap_size:
            print("Game Over! Final Score:", score)
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
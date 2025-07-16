import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Movement with Continuous Bounce")

clock = pygame.time.Clock()

desired_width = 200
desired_height = 200

player_image = pygame.image.load("football.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (desired_width, desired_height))

player_x = 100
player_y = 300
player_speed = 3

vel_x = 0
vel_y = 0

gravity = 1
bounce_factor = 1.0

# ✅ Define floor_y here:
floor_y = height - desired_height

running = True
while running:
    screen.fill((0, 0, 0))  # Sky blue background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    vel_x = 0
    if keys[pygame.K_LEFT]:
        vel_x = -player_speed
    if keys[pygame.K_RIGHT]:
        vel_x = player_speed

    # Optional: Remove space key check to make it bounce automatically
    if keys[pygame.K_SPACE] and player_y >= floor_y:
        vel_y = -20

    vel_y += gravity

    player_x += vel_x
    player_y += vel_y

    if player_y > floor_y:
        player_y = floor_y
        vel_y = -vel_y * bounce_factor

    player_x = max(0, min(player_x, width - desired_width))

    screen.blit(player_image, (player_x, player_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

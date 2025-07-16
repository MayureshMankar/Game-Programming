import pygame
import sys

pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Sprite Movement")

clock = pygame.time.Clock()

# Desired image size
frame_width = 400
frame_height = 500

# Load and resize animation frames
walk_frames = [
    pygame.transform.scale(pygame.image.load("car2.jpg").convert(), (frame_width, frame_height)),
    pygame.transform.scale(pygame.image.load("car2.jpg").convert(), (frame_width, frame_height)),
    pygame.transform.scale(pygame.image.load("car1.jpg").convert(), (frame_width, frame_height))
]


# Player variables
player_x = 100
player_y = 300
player_speed = 5
frame_index = 0
frame_delay = 8
frame_counter = 0
moving = False

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()
    moving = False

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        moving = True
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        moving = True
    if keys[pygame.K_UP]:
        player_y -= player_speed
        moving = True
    if keys[pygame.K_DOWN]:
        player_y += player_speed
        moving = True

    # Frame update
    if moving:
        frame_counter += 1
        if frame_counter >= frame_delay:
            frame_index = (frame_index + 1) % len(walk_frames)
            frame_counter = 0
    else:
        frame_index = 0

    # Draw sprite
    screen.blit(walk_frames[frame_index], (player_x, player_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

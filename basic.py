import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen Setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("All-in-One: Pygame Practical")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)

# Font
font = pygame.font.SysFont("Arial", 20)

# 1. Translation Setup
tx, ty = 100, 100
velocity = 5

# 2. Rotation Setup
angle = 0
rot_surf = pygame.Surface((100, 50), pygame.SRCALPHA)
rot_surf.fill(GREEN)

# 3. Scaling Setup
scale_surf = pygame.Surface((100, 50))
scale_surf.fill(BLUE)
scale_factor = 1.0
growing = True

# 4. Snowfall Setup
snowflakes = []
for _ in range(100):
    snowflakes.append([random.randint(0, WIDTH), random.randint(-HEIGHT, 0), random.randint(1, 3)])

# Game Loop
running = True
while running:
    screen.fill(BLACK)

    # Quit Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw axes
    pygame.draw.line(screen, WHITE, (0, HEIGHT//2), (WIDTH, HEIGHT//2), 1)
    pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 1)

    # 1. Translation - Red box moving with keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tx -= velocity
    if keys[pygame.K_RIGHT]:
        tx += velocity
    if keys[pygame.K_UP]:
        ty -= velocity
    if keys[pygame.K_DOWN]:
        ty += velocity
    pygame.draw.rect(screen, RED, (tx, ty, 60, 40))
    screen.blit(font.render("Translation", True, WHITE), (tx, ty - 25))

    # 2. Rotation - Rotating green rectangle
    angle += 2
    rotated = pygame.transform.rotate(rot_surf, angle)
    rot_rect = rotated.get_rect(center=(400, 150))
    screen.blit(rotated, rot_rect)
    screen.blit(font.render("Rotation", True, WHITE), (rot_rect.x + 10, rot_rect.y - 20))

    # 3. Scaling - Blue rectangle growing/shrinking
    if growing:
        scale_factor += 0.01
        if scale_factor >= 2.0:
            growing = False
    else:
        scale_factor -= 0.01
        if scale_factor <= 1.0:
            growing = True
    scaled = pygame.transform.scale(scale_surf, (int(100 * scale_factor), int(50 * scale_factor)))
    screen.blit(scaled, (500, 400))
    screen.blit(font.render("Scaling", True, WHITE), (500, 375))

    # 4. Vector-style circle + line
    center = (WIDTH // 2, HEIGHT // 2)
    end = (center[0] + 100, center[1] - 50)
    pygame.draw.circle(screen, YELLOW, center, 30, 2)
    pygame.draw.line(screen, BLUE, center, end, 3)
    screen.blit(font.render("Circle + Line", True, WHITE), (center[0] - 40, center[1] + 40))

    # 5. Snowfall
    for flake in snowflakes:
        flake[1] += flake[2]
        if flake[1] > HEIGHT:
            flake[1] = random.randint(-20, -1)
            flake[0] = random.randint(0, WIDTH)
        pygame.draw.circle(screen, WHITE, (flake[0], flake[1]), 3)

    # Update Display
    pygame.display.update()
    clock.tick(60)

pygame.quit()

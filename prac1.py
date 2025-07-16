import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vector Visualization")

# Colors
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)

# Center point
origin = (WIDTH // 2, HEIGHT // 2)

# Define Vectors A and B
A = pygame.math.Vector2(100, -50)   # Pygame uses screen coords: y is flipped
B = pygame.math.Vector2(50, -100)

# Scalar
scalar = 1.5

# Font
font = pygame.font.SysFont("Arial", 20)

# Function to draw a vector as arrow
def draw_vector(v, color, label, offset=(0, 0)):
    end_pos = (origin[0] + v.x + offset[0], origin[1] + v.y + offset[1])
    pygame.draw.line(screen, color, origin, end_pos, 3)
    pygame.draw.circle(screen, color, end_pos, 5)
    text = font.render(label, True, color)
    screen.blit(text, end_pos)

# Game Loop
running = True
while running:
    screen.fill(WHITE)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw axes
    pygame.draw.line(screen, BLACK, (0, HEIGHT//2), (WIDTH, HEIGHT//2), 1)
    pygame.draw.line(screen, BLACK, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 1)

    # Vector Calculations
    C = A + B
    D = A - B
    E = A * scalar

    # Draw vectors
    draw_vector(A, RED, "A")
    draw_vector(B, GREEN, "B")
    draw_vector(C, BLUE, "A + B")
    draw_vector(D, (255, 165, 0), "A - B", offset=(10, 10))
    draw_vector(E, (128, 0, 128), "1.5 * A", offset=(15, -15))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()


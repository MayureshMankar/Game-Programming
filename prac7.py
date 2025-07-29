import pygame
import sys
import math

pygame.init()

width, height = 600, 600
sprite_original_w, sprite_original_h = 100, 100

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Moves with Gradual Shrink/Enlarge")

clock = pygame.time.Clock()

original_image = pygame.image.load("football.png").convert_alpha()

# Positions for diagonals
top_left = (0, 0)
bottom_right = (width - sprite_original_w, height - sprite_original_h)
bottom_left = (0, height - sprite_original_h)
top_right = (width - sprite_original_w, 0)

# Start at top-left corner (diagonal 1)
player_x, player_y = top_left
vel_x = 10
vel_y = 10
moving_down_right = True

# Counters and states
repeat_count = 0
max_repeats = 3
in_second_diagonal = False
moving_down_left = True  # for second diagonal

# Size control
max_scale = 1.0
min_scale = 0.3

# Center position
center_x = (width - sprite_original_w) // 2
center_y = (height - sprite_original_h) // 2

def get_scale(x, y, center_x, center_y, max_dist):
    # Calculate distance from center
    dist = math.hypot(x - center_x, y - center_y)
    # Scale shrinks linearly with distance: closest -> min_scale, farthest -> max_scale
    scale = min_scale + (max_scale - min_scale) * (dist / max_dist)
    return max(min_scale, min(max_scale, scale))

# Max distance possible on screen diagonal (for scaling)
max_distance = math.hypot(center_x, center_y)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update scale based on distance to center
    scale = get_scale(player_x, player_y, center_x, center_y, max_distance)

    # Calculate current sprite size based on scale
    sprite_w = int(sprite_original_w * scale)
    sprite_h = int(sprite_original_h * scale)

    # Resize image with current scale
    player_image = pygame.transform.smoothscale(original_image, (sprite_w, sprite_h))

    if not in_second_diagonal:
        # Move on diagonal 1 (top-left <-> bottom-right)
        if moving_down_right:
            player_x += vel_x
            player_y += vel_y
            if player_x >= bottom_right[0] and player_y >= bottom_right[1]:
                player_x, player_y = bottom_right
                moving_down_right = False
        else:
            player_x -= vel_x
            player_y -= vel_y
            if player_x <= top_left[0] and player_y <= top_left[1]:
                player_x, player_y = top_left
                moving_down_right = True
                repeat_count += 1
                # After 3 repeats stop at center and switch
                if repeat_count >= max_repeats:
                    player_x = center_x
                    player_y = center_y
                    in_second_diagonal = True
                    moving_down_left = True
    else:
        # Move on second diagonal (bottom-left <-> top-right)
        if moving_down_left:
            player_x += vel_x
            player_y -= vel_y
            if player_x >= top_right[0] and player_y <= top_right[1]:
                player_x, player_y = top_right
                moving_down_left = False
        else:
            player_x -= vel_x
            player_y += vel_y
            if player_x <= bottom_left[0] and player_y >= bottom_left[1]:
                player_x, player_y = bottom_left
                moving_down_left = True

    # Draw the ball, adjusting for size to keep it centered
    draw_x = player_x + (sprite_original_w - sprite_w) // 2
    draw_y = player_y + (sprite_original_h - sprite_h) // 2
    screen.blit(player_image, (draw_x, draw_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

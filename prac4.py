import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Loop: Key & Mouse Events")

# Fonts
font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 24)

# State Variables
game_running = True
game_over = False
key_pressed_text = ""
mouse_click_text = ""

clock = pygame.time.Clock()
game_timer = 0  # Used instead of wait()

while game_running:
    dt = clock.tick(60)  # Time since last frame in ms
    screen.fill((255, 255, 255))  # White background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_running = False
            elif event.key == pygame.K_r:
                game_over = False
                game_timer = 0
                key_pressed_text = ""
                mouse_click_text = ""
            else:
                key_pressed_text = f"Key Pressed: {pygame.key.name(event.key)}"

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_text = f"Mouse Clicked at: {event.pos}"

    if not game_over:
        # Draw main game text
        text = font.render("Game Running - Press Q to Quit, R to Restart", True, (0, 0, 0))
        screen.blit(text, (50, height // 2))

        # Show key/mouse info
        if key_pressed_text:
            screen.blit(small_font.render(key_pressed_text, True, (0, 100, 0)), (50, height // 2 + 50))

        if mouse_click_text:
            screen.blit(small_font.render(mouse_click_text, True, (0, 0, 200)), (50, height // 2 + 90))

        # Start timer
        game_timer += dt
        if game_timer > 5000:  # after 3 seconds, end game
            game_over = True
    else:
        text = font.render("Game Over - Press R to Restart", True, (255, 0, 0))
        screen.blit(text, (200, height // 2))

    pygame.display.flip()

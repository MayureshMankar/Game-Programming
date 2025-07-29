import pygame
import random
import sys

pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect the Coins")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
coin_img = pygame.image.load("coin.png")

# Resize images
player_img = pygame.transform.scale(player_img, (40, 40))
enemy_img = pygame.transform.scale(enemy_img, (40, 40))
coin_img = pygame.transform.scale(coin_img, (20, 20))

# Load sounds
coin_sound = pygame.mixer.Sound("coin.wav")
death_sound = pygame.mixer.Sound("death.wav")

# Background music
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)

# Player setup
player = pygame.Rect(100, 100, 40, 40)
player_speed = 5

# Enemy setup
chasing_enemies = []
chaser_speed = 2

# Game state
game_over = False
game_won = False
coins = []
score = 0

def generate_enemies():
    chasing_enemies.clear()
    # Generate 5 chasing enemies
    for _ in range(1):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        chasing_enemies.append(pygame.Rect(x, y, 40, 40))

def generate_coins():
    coins.clear()
    # Generate 15 coins
    for _ in range(15):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        coins.append(pygame.Rect(x, y, 20, 20))

def reset_game():
    global player, game_over, game_won, score
    player.x, player.y = 100, 100
    generate_enemies()
    generate_coins()
    game_over = False
    game_won = False
    score = 0

def move_chasers():
    for chaser in chasing_enemies:
        if player.x > chaser.x:
            chaser.x += chaser_speed
        elif player.x < chaser.x:
            chaser.x -= chaser_speed
        if player.y > chaser.y:
            chaser.y += chaser_speed
        elif player.y < chaser.y:
            chaser.y -= chaser_speed

def draw_game():
    screen.fill(WHITE)
    screen.blit(player_img, player.topleft)
    for chaser in chasing_enemies:
        screen.blit(enemy_img, chaser.topleft)
    for coin in coins:
        screen.blit(coin_img, coin.topleft)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    coins_left_text = font.render(f"Coins Left: {len(coins)}", True, BLACK)
    screen.blit(coins_left_text, (10, 60))
    pygame.display.flip()

# Initialize game
reset_game()

# Game loop
running = True
while running:
    clock.tick(60)

    if not game_over and not game_won:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x -= player_speed
        if keys[pygame.K_RIGHT]: player.x += player_speed
        if keys[pygame.K_UP]: player.y -= player_speed
        if keys[pygame.K_DOWN]: player.y += player_speed

        # Keep player within screen bounds
        player.x = max(0, min(WIDTH - 40, player.x))
        player.y = max(0, min(HEIGHT - 40, player.y))

        # Coin collection
        for coin in coins[:]:
            if player.colliderect(coin):
                coins.remove(coin)
                score += 1
                coin_sound.play()

        # Chasing enemy movement
        move_chasers()

        # Check collisions with enemies
        for enemy in chasing_enemies:
            if player.colliderect(enemy):
                death_sound.play()
                game_over = True
                break

        draw_game()

        # Check win condition
        if not coins:
            game_won = True

    elif game_over:
        screen.fill(WHITE)
        over_text = font.render("Game Over", True, BLACK)
        screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2 - 50))
        final_score_text = font.render(f"Final Score: {score}", True, BLACK)
        screen.blit(final_score_text, (WIDTH//2 - final_score_text.get_width()//2, HEIGHT//2))
        instr_text = font.render("Press R to Restart, Q to Quit", True, BLACK)
        screen.blit(instr_text, (WIDTH//2 - instr_text.get_width()//2, HEIGHT//2 + 50))
        pygame.display.flip()

    elif game_won:
        screen.fill(WHITE)
        win_text = font.render("You Win!", True, BLACK)
        screen.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2 - 50))
        final_score_text = font.render(f"Final Score: {score}", True, BLACK)
        screen.blit(final_score_text, (WIDTH//2 - final_score_text.get_width()//2, HEIGHT//2))
        instr_text = font.render("Press R to Play Again, Q to Quit", True, BLACK)
        screen.blit(instr_text, (WIDTH//2 - instr_text.get_width()//2, HEIGHT//2 + 50))
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_r:
                reset_game()

pygame.quit()
sys.exit()

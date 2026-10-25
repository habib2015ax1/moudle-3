import math
import random
from pathlib import Path

import pygame


SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1500
PLAYER_START_X = (SCREEN_WIDTH - 64) // 2
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 250
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 10
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
NUM_OF_ENEMIES = 60


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Game")
clock = pygame.time.Clock()

# Load images from the same folder as this script, regardless of the launch folder.
ASSET_DIR = Path(__file__).resolve().parent
background = pygame.image.load(str(ASSET_DIR / "coolspacebackroung.png")).convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
player_image = pygame.image.load(str(ASSET_DIR / "spaceship.png")).convert_alpha()
player_image = pygame.transform.scale(player_image, (64, 64))
enemy_image = pygame.image.load(str(ASSET_DIR / "enemy.png")).convert_alpha()
enemy_image = pygame.transform.scale(enemy_image, (64, 64))
bullet_image = pygame.image.load(str(ASSET_DIR / "bullet.png")).convert_alpha()
bullet_image = pygame.transform.scale(bullet_image, (24, 32))

player_x = PLAYER_START_X
player_y = PLAYER_START_Y
player_x_change = 0

enemies = [
    {
        "x": random.randint(0, SCREEN_WIDTH - 64),
        "y": random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX),
        "speed_x": ENEMY_SPEED_X,
    }
    for _ in range(NUM_OF_ENEMIES)
]

bullet_x = 0
bullet_y = PLAYER_START_Y
bullet_state = "ready"
score = 0
font = pygame.font.Font(None, 36)
over_font = pygame.font.Font(None, 72)
game_over = False
running = True


def is_collision(enemy_x, enemy_y, shot_x, shot_y):
    distance = math.hypot(enemy_x - shot_x, enemy_y - shot_y)
    return distance < COLLISION_DISTANCE


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            elif event.key == pygame.K_RIGHT:
                player_x_change = 5
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if bullet_state == "ready" and not game_over:
                bullet_x = player_x + 20
                bullet_y = player_y
                bullet_state = "fire"
        elif event.type == pygame.KEYUP and event.key in (pygame.K_LEFT, pygame.K_RIGHT):
            player_x_change = 0

    if not game_over:
        player_x = max(0, min(player_x + player_x_change, SCREEN_WIDTH - 64))

        for enemy in enemies:
            enemy["x"] += enemy["speed_x"]
            if enemy["x"] <= 0 or enemy["x"] >= SCREEN_WIDTH - 64:
                enemy["speed_x"] *= -1
                enemy["y"] += ENEMY_SPEED_Y

            if enemy["y"] > 350:
                game_over = True

            if bullet_state == "fire" and is_collision(
                enemy["x"] + 32, enemy["y"] + 32, bullet_x + 12, bullet_y + 16
            ):
                score += 1
                bullet_state = "ready"
                enemy["x"] = random.randint(0, SCREEN_WIDTH - 64)
                enemy["y"] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        if bullet_state == "fire":
            bullet_y -= BULLET_SPEED_Y
            if bullet_y < -32:
                bullet_state = "ready"

    screen.blit(background, (0, 0))
    screen.blit(player_image, (player_x, player_y))
    for enemy in enemies:
        screen.blit(enemy_image, (enemy["x"], enemy["y"]))
    if bullet_state == "fire":
        screen.blit(bullet_image, (bullet_x, bullet_y))
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    if game_over:
        message = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(message, message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

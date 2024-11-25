import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions and settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("game Prototype")

# Colors
WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
RED = (0, 0, 255)

# FPS
FPS = 60
clock = pygame.time.Clock()

# Player settings
player_width = 50
player_height = 100
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 100
player_velocity = 5
jumping = False
jump_count = 10

# Load assets
player_image = pygame.Surface((player_width, player_height))
player_image.fill(RED)  # Placeholder red rectangle as the player sprite

# Ground settings
ground_height = 50

# Jumping function
def handle_jumping():
    global player_y, jumping, jump_count
    if jumping:
        if jump_count >= -10:
            neg = 0.5
            if jump_count < 0:
                neg = -0.5
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 5

# Main game loop
def main():
    global player_x, player_y, jumping, jump_count

    while True:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Key presses for movement and jumping
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_x -= player_velocity
        if keys[pygame.K_RIGHT]:
            player_x += player_velocity
        if not jumping and keys[pygame.K_SPACE]:
            jumping = True

        # Prevent player from going off screen
        if player_x < 0:
            player_x = 0
        if player_x > SCREEN_WIDTH - player_width:
            player_x = SCREEN_WIDTH - player_width

        # Handle jumping mechanics
        handle_jumping()

        # Platform collision (simple ground collision)
        if player_y >= SCREEN_HEIGHT - player_height - ground_height:
            player_y = SCREEN_HEIGHT - player_height - ground_height
            jumping = False
            jump_count = 10

        # Draw the player
        screen.blit(player_image, (player_x, player_y))

        # Draw ground
        pygame.draw.rect(screen, WHITE, (0, SCREEN_HEIGHT - ground_height, SCREEN_WIDTH, ground_height))
        pygame.draw.rect(screen, WHITE, (0, 50 - 100, 50, ground_height))

        
        # Update the screen
        pygame.display.update()

        # Set the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()

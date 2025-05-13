import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Russian Roulette")

# Load assets
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Sounds
click_sound = pygame.mixer.Sound("click.wav")
bang_sound = pygame.mixer.Sound("bang.wav")
spin_sound = pygame.mixer.Sound("spin.wav")

# Revolver image (replace with your own image file if available)
revolver_image = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.circle(revolver_image, BLACK, (100, 100), 100)
pygame.draw.circle(revolver_image, WHITE, (100, 100), 80)

# Game loop variables
running = True
chambers = [0, 0, 0, 0, 0, 1]
message = "Spin the cylinder and pull the trigger!"
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_over and event.key == pygame.K_SPACE:
                spin_sound.play()  # Play spin sound
                random.shuffle(chambers)
                if chambers[0] == 1:
                    bang_sound.play()  # Play bang sound
                    message = "Bang! You're out!"
                    game_over = True
                else:
                    click_sound.play()  # Play click sound
                    message = "Click! You're safe!"

            if game_over and event.key == pygame.K_r:
                # Reset the game
                chambers = [0, 0, 0, 0, 0, 1]
                message = "Spin the cylinder and pull the trigger!"
                game_over = False

    # Clear screen
    screen.fill(WHITE)

    # Draw revolver (simple representation)
    screen.blit(revolver_image, (WIDTH // 2 - 100, HEIGHT // 2 - 100))

    # Draw message
    text = font.render(message, True, RED if game_over else GREEN)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(text, text_rect)

    # Instructions
    instructions = small_font.render(
        "Press SPACE to play | Press R to restart (if game over)", True, BLACK
    )
    screen.blit(instructions, (20, 20))

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()

import pygame
import random
import sys

# --- Game Setup ---
pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Drop Game")
clock = pygame.time.Clock()

# --- Load Images ---
chicken_img = pygame.image.load("chicken.png").convert_alpha()
powerup_img = pygame.image.load("powerup.png").convert_alpha()
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((135, 206, 235))  # Sky blue fallback if no background


# Load catcher image
catcher_img = pygame.image.load("catcher.png").convert_alpha()
catcher_rect = catcher_img.get_rect(midbottom=(WIDTH // 2, HEIGHT - 50))
catcher_speed = 8
screen.blit(catcher_img, catcher_rect.topleft)

# --- Game Variables ---
chickens = []
powerup_active = True
POWERUP_POS = (random.randint(50, WIDTH - 50), random.randint(300, HEIGHT - 100))
powerup_rect = powerup_img.get_rect(center=POWERUP_POS)  # ✅ define once, reuse
score = 0
font = pygame.font.SysFont("Arial", 24)

# --- Classes ---
class Chicken:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = -50
        self.speed = random.randint(3, 6)
        self.rect = chicken_img.get_rect(center=(self.x, self.y))

    def update(self):
        self.y += self.speed
        self.rect.center = (self.x, self.y)

    def draw(self):
        screen.blit(chicken_img, self.rect.topleft)

    def check_powerup_collision(self, powerup_rect):
        global score, powerup_active
        if self.rect.colliderect(powerup_rect):
            score += 10
            powerup_active = False


# --- Game Loop ---
running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn chickens occasionally
    if random.randint(1, 20) == 1:
        chickens.append(Chicken())

    # Draw and update chickens
    for chicken in chickens[:]:
        chicken.update()
        chicken.draw()

        # Check collision with powerup
        if powerup_active:
            chicken.check_powerup_collision(powerup_rect)

        
        # Remove if off-screen
        if chicken.y > HEIGHT:
            chickens.remove(chicken)
        # Remove if caught
        if chicken.rect.colliderect(catcher_rect):
            score += 5
            chickens.remove(chicken)
            continue  # skip drawing since removed


    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and catcher_rect.left > 0:
        catcher_rect.x -= catcher_speed
    if keys[pygame.K_RIGHT] and catcher_rect.right < WIDTH:
        catcher_rect.x += catcher_speed

    # Draw powerup
    if powerup_active:
        screen.blit(powerup_img, powerup_rect.topleft)

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

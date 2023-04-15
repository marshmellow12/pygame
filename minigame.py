import math
import pygame
import random

from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN

pygame.init()
pygame.font.init()

# screen size
WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# -------------------
# Initialize global variables

frame_count = 0
score = 0
timer = 1000
game_over = 0 

score_font = pygame.font.SysFont("Comic Sans MS", 30)
circle_radius = 50

# targets
target_x = random.randrange(0, 600)
target_y = random.randrange(0, 600)

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            
            mouse_x, mouse_y = event.pos
            a = target_x - mouse_x
            b = target_y - mouse_y
            distance = math.sqrt(a**2 + b**2)
            if distance < circle_radius:
                score += 1
                frame_count = 0
                target_x = random.randrange(0, 600)
                target_y = random.randrange(0, 600)

    # target boundery
    if target_x <= 150:
        target_x = 150
    elif  target_x <= 300:
        target_x = 300
    elif target_x > 300:
        target_x = 450
    
    if target_y <= 150:
        target_y = 150
    elif target_y <= 300:
        target_y = 300
    elif target_y > 300:
        target_y = 450  

    frame_count += 1
    timer -= 1

    screen.fill("black") # background colour
    # collum 1
    pygame.draw.circle(screen, "white", (WIDTH/2, HEIGHT/2), circle_radius)
    pygame.draw.circle(screen, "white", (WIDTH/2, HEIGHT/4), circle_radius)
    pygame.draw.circle(screen, "white", (WIDTH/2, HEIGHT/1.33), circle_radius)

    # collum 2
    pygame.draw.circle(screen, "white", (WIDTH/4, HEIGHT/2), circle_radius)
    pygame.draw.circle(screen, "white", (WIDTH/4, HEIGHT/4), circle_radius)
    pygame.draw.circle(screen, "white", (WIDTH/4, HEIGHT/1.33), circle_radius)

    # collum 3
    pygame.draw.circle(screen, "white", (WIDTH/1.33, HEIGHT/2), circle_radius)
    pygame.draw.circle(screen, "white", (WIDTH/1.33, HEIGHT/4), circle_radius)
    pygame.draw.circle(screen, "white", (WIDTH/1.33, HEIGHT/1.33), circle_radius)        
    
# LEVEL 1 -----------------
    # drawing targets
    if frame_count < 10:
        pygame.draw.circle(screen, "#7AD3FF", (target_x, target_y), circle_radius)

    score_text = score_font.render(f"Score: {score}", False, (0, 0, 0), "white")
    screen.blit(score_text, (0,0))

# LEVEL 2 ------------------
    if score == 30:
        circle_radius = 40

# LEVEL 3 ------------------
    if score == 60:
       frame_count = 0
       circle_radius = 30
     
    # drawing targets faster
    if frame_count < 5: 
        pygame.draw.circle(screen, "#7AD3FF", (target_x, target_y), circle_radius)

    timer_text = score_font.render(f"Time: {timer}", False, (0, 0, 0), "white")
    screen.blit(timer_text, (450,0))
 
#  END OF GAME ----------------------
    if timer <= 0:
        game_over = True

        screen.fill(("black"))
        score_text = score_font.render(f"SCORE: {score}", False, (0, 0, 0))
        screen.blit(score_text, (10, 10))

    if game_over:
        game_over_text = score_font.render("GAME OVER", False, (255, 0, 0))
        screen.blit(game_over_text, (200, 250))
        final_score_text = score_font.render(f"FINAL SCORE: {score}", False, (255, 0, 0))
        screen.blit(final_score_text, (200, 300))
        
        
    pygame.display.flip()
    clock.tick(30)


pygame.quit()

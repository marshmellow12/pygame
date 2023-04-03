# pygame template

import pygame
pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

sun_x = 250
sun_y = 10

day_time = 0
night_time = 0

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DAYTIME -----------------------------------------------
    # DRAWING
    screen.fill("#6ACAFE")  # always the first drawing command-----(the sky)
    # sun ----------------
    sun = pygame.draw.circle(screen, "#F7E619", (sun_x, sun_y), 45)
    day_time += 1
    if day_time == 10: 
        day_time = 0
        sun_y += 20
        
    if sun_y > 300:
        screen.fill("#120F4C")
    # stars ------------------------ 
        pygame.draw.circle(screen, "#FFFFFF", (149, 25), 2)
        pygame.draw.circle(screen, "#FFFFFF", (100, 75), 2)
        pygame.draw.circle(screen, "#FFFFFF", (50, 105), 2)
        pygame.draw.circle(screen, "#FFFFFF", (17, 25), 2)

        pygame.draw.circle(screen, "#FFFFFF", (207, 40), 2)
        pygame.draw.circle(screen, "#FFFFFF", (223, 94), 2)

        pygame.draw.circle(screen, "#FFFFFF", (300, 65), 2)
        pygame.draw.circle(screen, "#FFFFFF", (310, 158), 2)
        pygame.draw.circle(screen, "#FFFFFF", (560, 25), 2)
        pygame.draw.circle(screen, "#FFFFFF", (530, 55), 2)
        pygame.draw.circle(screen, "#FFFFFF", (440, 75), 2)
        pygame.draw.circle(screen, "#FFFFFF", (410, 60), 2)

        pygame.draw.circle(screen, "#FFFFFF", (605, 100), 2)
        pygame.draw.circle(screen, "#FFFFFF", (750, 85), 2)
        pygame.draw.circle(screen, "#FFFFFF", (459, 25), 2)

    # ground --------------
    pygame.draw.rect(screen, "#3DA036", (0, 360, 10000, 1000))

    # mountains --------------
    pygame.draw.polygon(screen, "#706E6E",[(630,360), (475,68), (475,70), (360,360)])
    pygame.draw.polygon(screen, "#706E6E",[(160,70), (25,360), (300,360), (160, 68)])
    pygame.draw.polygon(screen, "#8A8787", [(360,30), (500,360), (180,360), (360, 27)])

    # tree_1 ------------------------
    pygame.draw.polygon(screen, "#6F4616",[(280, 380), (300, 380), (300, 430), (280, 430)])
    pygame.draw.circle(screen, "#1D8617", (290, 355), 40, 1000)

    pygame.draw.polygon(screen, "#6F4616",[(30, 400), (50, 400), (50, 470), (30, 470)])
    pygame.draw.circle(screen, "#1D8617", (40, 390), 45, 1000)

    # house_base ------------------
    pygame.draw.polygon(screen, "#FFE496",[(530, 390), (615, 390), (615, 462), (530, 462)])
    pygame.draw.polygon(screen, "#FFE496",[(90, 390), (170, 390), (170, 462), (90, 462)])
    pygame.draw.polygon(screen, "#FFE496",[(320, 355), (400, 355), (400, 430), (320, 430)])

    # house_roof ----------------
    pygame.draw.polygon(screen, "#9E1515",[(650,400), (570,350), (570,350), (500,400)])
    pygame.draw.polygon(screen, "#9E1515",[(130,350), (58,400), (200,400), (130, 350)])
    pygame.draw.polygon(screen, "#9E1515", [(360,320), (430,370), (290,370), (360, 320)])

    # tree_2 ------------
    pygame.draw.polygon(screen, "#6F4616",[(460, 400), (480, 400), (480, 462), (460, 462)])
    pygame.draw.circle(screen, "#1D8617", (470, 380), 45, 1000)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()

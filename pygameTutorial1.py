import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("The Coding Protocol")

x = 150
y = 150
width = 30
height = 30
velocity = 10

run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x += velocity

    if keys[pygame.K_LEFT]:
        x -= velocity

    if keys[pygame.K_UP]:
        y -= velocity

    if keys[pygame.K_DOWN]:
        y += velocity

    win.fill((0,0,0))
    pygame.draw.rect(win, (0,250,0), (x,y,width,height))
    pygame.display.update()

pygame.quit()
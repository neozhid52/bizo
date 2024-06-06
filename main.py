import pygame
import random
pygame.init()

window = pygame.display.set_mode((500, 500))
back_color = (215, 10, 255)
game = True
clock = pygame.time.Clock()
player1 = pygame.Rect(225,225,50,50)
bullets = []
while game:

    pygame.draw.rect(window, (0,0,0) ,player1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player1.x > 0:
        player1.x -= 8
    if keys[pygame.K_s] and player1.y > 0:
        player1.y += 8
    if keys[pygame.K_d] and player1.x < 450:
        player1.x += 8
    if keys[pygame.K_w] and player1.y < 450:
        player1.y -= 8

    if random.randint(0, 200) < 10:
        x = random.randint(0, 480)
        y = -10
        bullets.append(pygame.Rect(x,y,20,30))

    for b in bullets:
        pygame.draw.rect(window, (0, 0, 0), b)
        
    for b in bullets:
        b.y += 15
        if b.colliderect(player1):
            game = False
        if b.y > 500:
            bullets.remove(b)




    clock.tick(30)
    pygame.display.update()
    window.fill(back_color)

    
    
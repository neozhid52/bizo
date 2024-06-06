import pygame
import random
pygame.init()

window = pygame.display.set_mode((500, 500))
font = pygame.font.Font(None, 24)
text = font.render("Хрюкни", True,(0,0,0))
clock = pygame.time.Clock()
score = "хрю"


players = [pygame.Rect(25, 225, 75, 100),
           pygame.Rect(150, 225, 75, 100),
           pygame.Rect(275, 225, 75, 100),
           pygame.Rect(400, 225, 75, 100)
]
text_on_area = random.choice(players)
start_time = pygame.time.get_ticks()

back_color = (112, 96, 132)
game = True

clock = pygame.time.Clock()
while game:
    window.fill(back_color)
    window.blit(text,(25, 225))
    for pl in players:
            pygame.draw.rect(window,(250,250,250),pl)
    curent_time = pygame.time.get_ticks()
    elapsed_time = curent_time - start_time
    if elapsed_time > 1000:
        text_on_area = random.choice(players)
        start_time = pygame.time.get_ticks()
    window.blit(text,(text_on_area.x+5,text_on_area.y+40))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            if text_on_area.collidepoint(x,y):
                print(score)
        elif event.type == pygame.KEYDOWN:
            print(20)
    clock.tick(30)
    pygame.display.update()
    

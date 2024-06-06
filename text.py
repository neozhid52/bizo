# імпорт бібліотеки pygame
import pygame
pygame.init()

# створення головного вікна
window = pygame.display.set_mode((500, 500))

# кольори
white = (255, 255, 255)


# створення об'єкту "годинник" для встановлення частоти кадрів
clock = pygame.time.Clock()

'''----------start----------'''
# Шрифт та розмір
font = pygame.font.Font(None, 36) # 36 - це розмір тексту, при потребі можна змінити на бажаний розмір
text = font.render("Привіт!", True, (0,0,0)) # "Привіт!" - текст, який виводиться; (0,0,0) - колір у форматі RGB
'''-----------end-----------'''

# головний цикл гри
game = True
while game:
    window.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    '''----------start----------'''
    window.blit(text, (10,10)) # (10,10) - координати розміщення тексту
    '''-----------end-----------'''

    # задання частоти кадрів та оновлення екрану
    clock.tick(30)
    pygame.display.update()

pygame.quit()
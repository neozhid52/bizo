# імпорт бібліотеки pygame
import pygame
pygame.init()

# створення головного вікна
window = pygame.display.set_mode((500, 500))

# кольори
white = (255, 255, 255)
black = (0, 0, 0)

# створення об'єкту "годинник" для встановлення частоти кадрів
clock = pygame.time.Clock()

# головний цикл гри
game = True

class Player(): # клас для створення шаблону персонажа
    def __init__(self,x,y,width,height,image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect() # "межі" персонажа
        self.rect.x = x # координати по ширині
        self.rect.y = y # координати по висоті
        self.width = width # ширина
        self.height = height # висота

player = Player(100, 100, 100, 100, 'nosatiy1.png')

white = (255, 255, 255)
black = (0, 0, 0)
while game:
    window.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(player.image, (player.rect.x, player.rect.y))

    # задання частоти кадрів та оновлення екрану
    clock.tick(30)
    pygame.display.update()

pygame.quit()
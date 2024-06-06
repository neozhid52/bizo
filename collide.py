# імпорт бібліотеки pygame
import pygame
pygame.init()


class Player(): # клас для створення шаблону персонажа
    def __init__(self,x,y,width,height,image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect() # "межі" персонажа
        self.rect.x = x # координати по ширині
        self.rect.y = y # координати по висоті
        self.width = width # ширина
        self.height = height # висота


# створення головного вікна
window = pygame.display.set_mode((500, 500))



# створення персонажа
# player - назва об'єкту персонажа (може бути змінена)
#              ( x    y  width height    'name_image')         
player = Player(100, 100, 100, 100, 'bird.png')
player2 = Player(200, 200, 100, 100, 'bird.png')


# кольори
white = (255, 255, 255)
black = (0, 0, 0)

# створення об'єкту "годинник" для встановлення частоти кадрів
clock = pygame.time.Clock()

# головний цикл гри
game = True
while game:
    window.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    # відображення персонажа на екрані
    window.blit(player.image, (player.rect.x, player.rect.y))  
    window.blit(player2.image, (player2.rect.x, player2.rect.y))  

    '''----------start----------'''
    if player.rect.colliderect(player2.rect):
       print('Зіткнення відбулося')
    '''-----------end-----------'''
    # задання частоти кадрів та оновлення екрану
    clock.tick(30)
    pygame.display.update()

pygame.quit()
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
        '''----------start----------'''
        self.is_jump = False  # змінна для визначення стану прижку
        self.jump_count = 10  # лічильник для керування прижком
        '''-----------end-----------'''

    '''----------start----------'''
    def jumping(self):  # функція для виконання прижку
        if not self.is_jump:  # якщо персонаж не в стані прижку
            self.is_jump = True  # зміна стану прижку
            self.jump_count = 10  # початкове значення лічильника прижку
    '''-----------end-----------'''

    '''----------start----------'''
    def jump(self):  # метод для руху персонажа
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:  # якщо натиснута клавіша пробілу
            self.jumping()  # виконати прижок

        if self.is_jump:  # якщо персонаж у стані прижку
            if self.jump_count >= -10:  # поки лічильник більше або рівний -10
                neg = 1  # коефіцієнт для керування напрямком прижку
                if self.jump_count < 0:  # якщо лічильник менше 0
                    neg = -1  # змінити напрямок прижку
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg  # формула для прижку
                self.jump_count -= 1  # зменшення лічильника
            else:  # якщо лічильник вийшов за межі -10
                self.is_jump = False  # зміна стану прижку
    '''-----------end-----------'''


# створення головного вікна
window = pygame.display.set_mode((500, 500))


# створення персонажа
# player - назва об'єкту персонажа (може бути змінена)
#              ( x    y  width height    'name_image')         
player = Player(100, 200, 100, 100, 'bird.png')


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

    '''----------start----------'''
    # виклик функції прижку до персонажу
    player.jump()
    '''-----------end-----------'''


    # відображення персонажа на екрані
    window.blit(player.image, (player.rect.x, player.rect.y))  


    # задання частоти кадрів та оновлення екрану
    clock.tick(60)
    pygame.display.update()

pygame.quit()
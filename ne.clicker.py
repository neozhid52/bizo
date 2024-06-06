# імпорт бібліотеки pygame
import pygame
import random
pygame.init()

# створення головного вікна
window = pygame.display.set_mode((1366, 700))


white = (255, 255, 255)
black = (0, 0, 0)

# створення об'єкту "годинник" для встановлення частоти кадрів
clock = pygame.time.Clock()

# головний цикл гри
game = True

class Bullet1():
    # def __init__(self, x, y):
    #     self.rect = pygame.Rect(x, y, 5, 5) # 5,5 - розміри пулі

    def __init__(self,x,y,width,height,image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect() # "межі" персонажа
        self.rect.x = x # координати по ширині
        self.rect.y = y # координати по висоті

    def move(self): # функція для створення руху пулі
        self.rect.x += 20 # 10 - швидкість пулі
    def move2(self): # функція для створення руху пулі
        self.rect.x -= 20 # 10 - швидкість пулі
        

class Player(): # клас для створення шаблону персонажа
    def __init__(self,x,y,width,height,image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect() # "межі" персонажа
        self.rect.x = x # координати по ширині
        self.rect.y = y # координати по висоті
        self.width = width # ширина
        self.height = height # висота
        self.is_jump = False  # змінна для визначення стану прижку
        self.jump_count = 5  # лічильник для керування прижком
        self.speed = 5

    def jumping(self):  # функція для виконання прижку
        if not self.is_jump:  # якщо персонаж не в стані прижку
            self.is_jump = True  # зміна стану прижку
            self.jump_count = 10  # початкове значення лічильника прижку
        
    def jump(self):  # метод для руху персонажа
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:  # якщо натиснута клавіша пробілу
            self.jumping()  # виконати прижок
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              player1.shoot()

        if self.is_jump:
            if self.jump_count >= -10:  # поки лічильник більше або рівний -10
                neg = 1  # коефіцієнт для керування напрямком прижку
                if self.jump_count < 0:  # якщо лічильник менше 0
                    neg = -1 # змінити напрямок прижку
                self.rect.y -= (self.jump_count ** 2) * 0.4 * neg  # формула для прижку
                self.jump_count -= 1  # зменшення лічильника
            else:  # якщо лічильник вийшов за межі -10
                self.is_jump = False  # зміна стану прижку

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 99:
            self.rect.x -= 8
        if keys[pygame.K_d] and self.rect.x < 1175:
            self.rect.x += 8
        
        
    def shoot(self):
        bullet = Bullet1(self.rect.centerx, self.rect.centery, 50,50,"1679297133148179378__2_-removebg-preview.png") # створення пулі
        bullets_right.append(bullet) # додавання пулі до списку пуль
    def shoot2(self):
        bullet = Bullet1(self.rect.centerx, self.rect.centery, 50,50,"1679297133148179378__2_-removebg-preview.png") # створення пулі
        bullets_left.append(bullet) # додавання пулі до списку пуль
    def move_enemy1(self):
        self.rect.x += self.speed
        if self.rect.colliderect(player1.rect) or self.rect.x > 1470:
            self.rect.x = -1 * random.randint(100,1000)
            self.speed += 1
    
    def move_enemy2(self):
        self.rect.x -= self.speed
        if self.rect.colliderect(player1.rect) or self.rect.x < -75:
            self.rect.x = random.randint(1466, 2466)
            self.speed += 1

background_image = pygame.image.load("temple.jpg")  # Замість 'background.jfif' вкажіть шлях до вашого зображення фону
background_image = pygame.transform.scale(background_image, (1366, 700)) # задання розмірів фонового зображення

bullets_left = []
bullets_right = []
player1 = Player(500, 575, 100, 100, 'primat-remove.png')
enemy1 = Player(100, 600, 100, 100, "dusha.moyshi.png" )
enemy2 = Player(1266, 600, 100, 100, "dusha.moyshi.png" )

pygame.mixer.music.load('kingdom-of-fantasy-version-60s-10817.mp3')
# Відтворення музики 
pygame.mixer.music.play()

white = (255, 255, 255)
black = (0, 0, 0)


while game:
    window.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                player1.shoot()
            if event.key == pygame.K_l:
                player1.shoot2()
    
    

    window.blit(background_image, (0, 0))
    window.blit(player1.image, (player1.rect.x, player1.rect.y))
    window.blit(enemy1.image, (enemy1.rect.x, enemy1.rect.y))
    window.blit(enemy2.image, (enemy2.rect.x, enemy2.rect.y))
    player1.move()
    player1.jump()
    enemy1.move_enemy1()
    enemy2.move_enemy2()

    

    for bullet in bullets_right:
        bullet.move()
        pygame.draw.rect(window, (255, 0, 0), bullet.rect)
        if bullet.rect.colliderect(enemy1.rect):  
            bullets_right.remove(bullet)
            enemy1.rect.x = -1 * random.randint(100,1000)
            enemy1.speed += 1
        if bullet.rect.colliderect(enemy2.rect):
            bullets_right.remove(bullet)
            enemy2.rect.x = random.randint(1466, 2466)
            enemy2.speed += 1
    for bullet in bullets_left:
        bullet.move2()
        pygame.draw.rect(window, (255, 0, 0), bullet.rect)
        if bullet.rect.colliderect(enemy1.rect):  
            bullets_left.remove(bullet)
            enemy1.rect.x = -1 * random.randint(100,1000)
            enemy1.speed += 1
        if bullet.rect.colliderect(enemy2.rect):  
            bullets_left.remove(bullet)
            enemy2.rect.x = random.randint(1466, 2466)
            enemy2.speed += 1

    # задання частоти кадрів та оновлення екрану
    clock.tick(30)
    pygame.display.update()

pygame.quit()
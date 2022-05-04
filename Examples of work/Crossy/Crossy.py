######################################
# Shane Donivan
# PM Class
# Senior
# 8/26/21
# 01 - Game Refresher
# A Crossy type game where you get
# to the other side
#######################################

import pygame
# Pygame setup screen + Variables
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = '001'
GRAY = (84,84,84)
BLACK = (0,0,0)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS',65)
Level = 1

# Parent Class that controls the entire game
class Game:
    TICK = 60
    running = True

    def __init__(self, image, title, width, height):
        self.image = image
        self.title = title
        self.width = width
        self.height = height

        self.SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.SCREEN.fill(GRAY)
        pygame.display.set_caption(SCREEN_TITLE)

        background = pygame.image.load(image)
        self.image = pygame.transform.scale(background, (width, height))

    # Shows stuff on screen, and runs events
    def gameloop(self,level_speed):
        running = True
        win = False
        direction = 0

        player = Player('./imgs/players/p.png','./imgs/players/p2.png',375,500, 50, 50)
        enemy1 = Enemy('./imgs/enemies/e.png','./imgs/enemies/ee.png', 20, 400,50,50)
        enemy1.speed *= level_speed
        enemy2 = Enemy('./imgs/enemies/e2.png','./imgs/enemies/ee2.png', 50, 300, 50, 50)
        enemy2.speed *= level_speed
        enemy3 = Enemy('./imgs/enemies/e3.png','./imgs/enemies/ee3.png', 100, 200, 50, 50)
        enemy3.speed *= level_speed
        enemies = [enemy1, enemy2, enemy3]

        treasure = GameObject('./imgs/t.png','./imgs/t.png',375, 50, 50, 50)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0

            self.SCREEN.fill(GRAY)
            self.SCREEN.blit(self.image,(0,0))

            treasure.draw(self.SCREEN)
            player.move(direction, self.height)
            player.draw(self.SCREEN)

            enemy1.move(self.width)
            enemy1.draw(self.SCREEN)

            # Increases the number of enemies for the rest of the levels
            if level_speed > 2:
                enemy2.move(self.width)
                enemy2.draw(self.SCREEN)
            if level_speed > 4:
                enemy3.move(self.width)
                enemy3.draw(self.SCREEN)

            # Collision for every enemy, changes animation, and shows Score
            for enemy in enemies:
                if player.detection(enemy):
                    global Level
                    running = False
                    win = False
                    player.draw2(self.SCREEN)
                    enemy1.draw2(self.SCREEN)
                    if level_speed > 2:
                        enemy2.draw2(self.SCREEN)

                    if level_speed > 4:
                        enemy3.draw2(self.SCREEN)
                    text = font.render('You Lose', True, BLACK)
                    self.SCREEN.blit(text, (270, 150))
                    text2 = font.render('You made it to level: ' + str(Level), True, BLACK)
                    self.SCREEN.blit(text2, (100, 300))
                    pygame.display.update()
                    clock.tick(0.3)

            if player.detection(treasure):
                Level += 1
                print(Level)
                running = False
                win = True
                text = font.render('Level ' + str(Level), True, BLACK)
                self.SCREEN.blit(text, (285, 150))
                player.draw(self.SCREEN)
                pygame.display.update()
                clock.tick(0.5)
            pygame.display.update()
            clock.tick(self.TICK)

        # For every Level completed the game gets harder
        if win == True:
            self.gameloop(level_speed + 0.5)
        else:
            pass

# Parent Class for the Player and Enemies
class GameObject:

    # Sets up animation, position on screen, and scale of object
    def __init__(self, img,img2, x, y, width, height):
        object_image = pygame.image.load(img)
        object_image2 = pygame.image.load((img2))
        self.image = pygame.transform.scale(object_image, (width, height))
        self.image2 = pygame.transform.scale(object_image2, (width, height))

        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self,background):
        background.blit(self.image,(self.x_pos,self.y_pos))

    def draw2(self, background):
        background.blit(self.image2, (self.x_pos, self.y_pos))

# Sets up movement calculations
class Player(GameObject):
    speed = 20
    def __init__(self,img,img2, x, y, width, height):
        super().__init__(img,img2, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.speed
        elif direction < 0:
            self.y_pos += self.speed

        if self.y_pos >= max_height - 50:
            self.y_pos = max_height - 50

    def detection(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False

        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False

        return True

# Makes Enemy bounce back and forth
class Enemy(GameObject):
    speed = 5
    def __init__(self, img,img2, x, y, width, height):
        super().__init__(img,img2, x, y, width, height)

    def move(self,max_width):
        if self.x_pos <= 20:
            self.speed = abs(self.speed)
        elif self.x_pos >= max_width - 60:
            self.speed = -abs(self.speed)
        self.x_pos += self.speed

# Runs the game
new_game = Game('./imgs/backgrounds/b.png',SCREEN_TITLE,SCREEN_WIDTH,SCREEN_HEIGHT)
new_game.gameloop(1)


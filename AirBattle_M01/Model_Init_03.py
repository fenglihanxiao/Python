"""
    1. 03_XXX -> init game models
"""

# 1. Import system package
import sys
import random

# 2. Import third party package
import pygame
import pygame.locals
#from pygame.locals import *

# 08_XXX
IMG_BACKGROUND = "res/img_bg_level_1.jpg"
IMG_ENEMYIES = ("res/img-plane_1.png", "res/img-plane_2.png",
                "res/img-plane_3.png", "res/img-plane_4.png",
                "res/img-plane_5.png", "res/img-plane_6.png")
IMG_PALYER = "res/hero2.png"
IMG_BULLET = "res/bullet_13.png"


# 09_XXX -> abstract those data member to base class Model
class Model:
    window = None

    def __init__(self, img_path, x ,y):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y

    # 09_XXX -> Model Method Extraction
    def display(self):
        Model.window.blit(self.img, (self.x, self.y))


# TODO: Background class
# 09_XXX -> abstract those data member to base class Model
class Background(Model):
    # 07_XXX
    """
    # 1. 09_XXX -> Abstract those data init to base class Model
    def __init__(self, img_path, x ,y):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
    """

    # 10_XXX -> Move the background
    def move(self):
        # 11_XXX -> Repeat move the background image
        if self.y <= Game.WINDOW_HEIGHT:
            self.y += 1
        else:
            self.y = 0

    # 12_XXX -> Add anther image to background
    def display(self):
        # 12_XXX -> Add anther image to background by make y -700
        # Call super method
        super().display()
        # Model.window.blit(self.img, (self.x, self.y))
        Model.window.blit(self.img, (self.x, self.y - Game.WINDOW_HEIGHT))


# TODO: PlayerPlane class
class PlayerPlane(Model):
    # 21_XXX -> Send up bullets
    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        self.bullets = []

    def display(self, enemies):
        super().display()
        # 21_XXX -> Set bullets display in player plane.
        remove_bullets = []
        for b in self.bullets:
            b.move()
            b.display()

            # 22_XXX -> Remove upper screen bullets
            if b.y < -29:
                remove_bullets.append(b)
            else:
                # 23_XXX -> Collision of enemies and bullets
                bullet_rec = pygame.locals.Rect(b.x, b.y, 20, 29)
                for enemy in enemies:
                    enemy_rec = pygame.locals.Rect(enemy.x, enemy.y, 100, 68)
                    if pygame.Rect.colliderect(bullet_rec, enemy_rec):
                        # 24_XXX -> Collision of processing
                        idx = random.randint(0, 5)
                        enemy.img = pygame.image.load(IMG_ENEMYIES[idx])
                        enemy.x = random.randint(0, Game.WINDOW_WIDTH - 100)
                        enemy.y = random.randint(-Game.WINDOW_HEIGHT, -68)
                        remove_bullets.append(b)



        # 22_XXX -> Iterate remove list to clean up memory
        for b in remove_bullets:
            self.bullets.remove(b)





# TODO: EnemyPlane class
class EnemyPlane(Model):
    # 16_XXX
    def __init__(self):
        idx = random.randint(0, 5)
        self.img = pygame.image.load(IMG_ENEMYIES[idx])
        self.x = random.randint(0, Game.WINDOW_WIDTH - 100)
        self.y = random.randint(-Game.WINDOW_HEIGHT, -68)

    # 10_XXX -> Move the background
    def move(self):
        # 14_XXX -> Repeat move the background image
        if self.y <= Game.WINDOW_HEIGHT:
            self.y += 4
        else:
            # self.y = 0 - 68
            self.x = random.randint(0, Game.WINDOW_WIDTH - 100)
            self.y = random.randint(-Game.WINDOW_HEIGHT, -68)


# TODO: Bullet class
class Bullet(Model):
    # 22_XXX -> bullet move
    def move(self):
        self.y -= 12


# TODO: Game class
class Game:
    # 08_XXX
    WINDOW_WIDTH = 480
    WINDOW_HEIGHT = 700

    # TODO: 1. Game entry point
    def run(self):
        print("Run ...")
        self.init_frame()

        # 07_XXX
        self.mode_init()

        while True:
            # 10_XXX -> Move the background
            self.background.move()
            # 10-XXX -> put image in the WINDOW screen
            self.background.display()

            # 15_XXX -> Add multiple enemies
            for enemy in self.enemies:
                # 14_XXX -> Move enemy
                enemy.move()
                # 13_XXX -> Add single enemy
                enemy.display()

            # 18_XXX -> Add player
            # 23_XXX -> Collision of enemies and bullets
            self.player.display(self.enemies)

            pygame.display.update()

            self.event_init()

    # TODO: 3. Init window frame
    def init_frame(self):
        print("Init frame ...")
        # 08_XXX
        self.window = pygame.display.set_mode((Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT))
        # Make sure base class variable window points to self.window
        Model.window = self.window

        # 05_XXX
        image = pygame.image.load("res/app.ico")    #  加载图标文件为图片对象
        pygame.display.set_icon(image)  #  设置窗体图标为图片
        pygame.display.set_caption("Plane Battle v1.0")

    # 06_XXX
    def event_init(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                print("Exit now ......")
                sys.exit()

            # 19_XXX -> Move player's pos by index by mouse motion
            if event.type == pygame.locals.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                self.player.x = pos[0] - 60
                self.player.y = pos[1] - 39

        # 20_XXX get right click action
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0] == 1:
            pos = pygame.mouse.get_pos()
            self.player.bullets.append(Bullet(IMG_BULLET, pos[0] - 20/2, pos[1] - 29 - 40))

    # 07_XXX
    def mode_init(self):
        self.background = Background(IMG_BACKGROUND, 0, 0)

        # 15_XXX -> Add multiple enemies
        self.enemies = []
        for _ in range(5):
            # enemy = EnemyPlane(IMG_ENEMY1, random.randint(0, Game.WINDOW_WIDTH - 100), 200)
            # 16_XXX -> Enemy move random
            # enemy = EnemyPlane(IMG_ENEMY1,
            #                    random.randint(0, Game.WINDOW_WIDTH - 100),
            #                    random.randint(-Game.WINDOW_HEIGHT, -68))
            # print("====================", random.randint(0, Game.WINDOW_WIDTH - 100))

            # 16_XXX -> Enemy move random, move parameter list to init
            self.enemies.append(EnemyPlane())

        """
        # 09_XXX -> Model Extraction
        # 1. Draw on the screen
        self.window.blit(background.img, (background.x, background.y))
        """

        """
            1. 10_XXX -> No effect any more since in main loop it will call display
        """
        # self.background.display()

        # 18_XXX -> Add player
        self.player = PlayerPlane(IMG_PALYER, 200, 500)


# TODO: 2. Testing entry point
if __name__ == "__main__":
    Game().run()

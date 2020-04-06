"""
飞机大战——传智播客·黑马程序员出品
"""
import sys  # 导入系统模块

import pygame   # 导入pygame模块
import pygame.locals    # 导入pygame本地策略
# from pygame.locals import *

APP_ICON = "res/app.ico"    # 设计公共的图片常量，定义在文件中，方便管理
IMG_BACKGROUND = "res/img_bg_level_1.jpg"   # 设计公共的图片常量，定义在文件中，方便管理
IMG_ENEMY = "res/img-plane_5.png"   # 初始化敌机图片

# 创建所有显示的图形父类Model
class Model:
    window = None   # 定义主窗体对象，用于模型访问使用
    # 构造方法
    def __init__(self,img_path,x,y):
        self.img = pygame.image.load(img_path)  # 背景图片
        self.x = x  # 窗体中放置的x坐标
        self.y = y  # 窗体中放置的y坐标

    # 将模型加入窗体的方法抽取到父类
    def display(self):
        Model.window.blit(self.img, (self.x, self.y))  # 使用Model的类变量访问窗体对象  # 调用bilt方法，将图片加入到窗体中

# 背景类
class Background(Model):
    # 定义背景移动的方法
    def move(self):
        # 加入背景移动的情况判定
        if self.y <= Game.WINDOW_HEIGHT:    # 如果没有超出屏幕就正常移动
            self.y += 1  # 纵坐标自增1
        else:   # 如果超出屏幕，恢复图片位置为原始位置
            self.y = 0  # 纵坐标 = 0

    # 覆盖父类display方法，制作原始背景贴图+辅助背景贴图
    def display(self):
        Model.window.blit(self.img, (self.x, self.y))   # 原始背景贴图，推荐使用super().display()
        Model.window.blit(self.img, (self.x, self.y - Game.WINDOW_HEIGHT)) # 辅助背景，坐标位置与原始背景贴图上下拼接吻合

# 玩家类
class PlayerPlane(Model):
    pass
# 敌机类
class EnemyPlane(Model):
    #  TODO 1.定义敌机移动的方法
    def move(self):
        # TODO 2.判断敌机是否超出屏幕
        if self.y > Game.WINDOW_HEIGHT: # TODO 3.如果超出屏幕
            self.y = -68    # TODO 4.敌机纵坐标设置为-68，返回屏幕顶端
        else:   # TODO 5.敌机未超出屏幕
            self.y += 4     # TODO 6.控制敌机向下移动，移动速度设置为4

# 子弹类
class Bullet(Model):
    pass
# 游戏类
class Game:
    WINDOW_WIDTH = 512      # 设计窗体尺寸常量，定义在类中，缩小作用范围
    WINDOW_HEIGHT = 768     #设计窗体尺寸常量，定义在类中，缩小作用范围

    # 主程序，运行游戏入口
    def run(self):
        self.frame_init()   # 执行窗体初始化

        self.model_init()   # 执行对象初始化

        while True:     # 构造反复执行的机制，刷新窗体，使窗体保持在屏幕上

            self.background.move()  # 调用背景移动操作，构造背景图片向下移动的效果
            self.background.display()   # 移动完毕后，将移动后的图片加入到窗体中

            self.enemy.move()       # TODO 7.调用敌机移动操作
            self.enemy.display()    # 敌机显示到窗体中


            pygame.display.update()     # 刷新窗体

            self.event_init()   # 反复调用事件监听方法

    # 初始化窗体
    def frame_init(self):
        self.window = pygame.display.set_mode((Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT))  # 使用窗体常量替换原始格式  # 初始化窗体
        Model.window = self.window  # 将窗体对象传入模型类中
        img = pygame.image.load(APP_ICON)  # 使用图片常量替换原始格式 # 加载图标文件为图片对象
        pygame.display.set_icon(img)    # 设置窗体图标为图片
        pygame.display.set_caption("Plane Battle v1.0 传智播客·黑马程序员出品")    # 设置窗体的标题

    #  定义事件处理的方法
    def event_init(self):
        for event in pygame.event.get():    # 获取当前发生的所有事件
            if event.type == pygame.locals.QUIT :   # 判断当前事件类别是不是点击窗体的关闭按钮
                sys.exit()      # 执行退出系统操作

    # 初始化窗体中的对象
    def model_init(self):
        self.background = Background(IMG_BACKGROUND,0,0) # 扩大背景对象的使用范围  # 使用图片常量替换原始格式 # 初始化背景对象，传入图片路径，放置在0,0位
        self.enemy = EnemyPlane(IMG_ENEMY,200,200)  #  初始化敌机对象，放置在200,200坐标处（临时）


# 设置测试类入口操作
if __name__ == "__main__":
    Game().run()




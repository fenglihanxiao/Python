"""
飞机大战——传智播客·黑马程序员出品
"""
import sys  # 导入系统模块

import pygame   # 导入pygame模块
import pygame.locals    # 导入pygame本地策略
# from pygame.locals import *

APP_ICON = "res/app.ico"    # 设计公共的图片常量，定义在文件中，方便管理
IMG_BACKGROUND = "res/img_bg_level_1.jpg"   # 设计公共的图片常量，定义在文件中，方便管理

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
    # TODO 1.定义背景移动的方法
    def move(self):
        self.y += 1     # TODO 2.纵坐标自增1

# 玩家类
class PlayerPlane(Model):
    pass
# 敌机类
class EnemyPlane(Model):
    pass
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

            self.background.move()  # TODO 4.调用背景移动操作，构造背景图片向下移动的效果
            self.background.display()   # TODO 5.移动完毕后，将移动后的图片加入到窗体中

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
        self.background = Background(IMG_BACKGROUND,0,0) # TODO 3.扩大背景对象的使用范围  # 使用图片常量替换原始格式 # 初始化背景对象，传入图片路径，放置在0,0位
        """ TODO 6.删除单独的将背景图片加入窗体的操作（不影响结果）
        self.background.display()  # TODO 3.更新调用方式  # 使用抽取的Model类中的display方法完成
        """

# 设置测试类入口操作
if __name__ == "__main__":
    Game().run()







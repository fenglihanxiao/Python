"""
飞机大战——传智播客·黑马程序员出品
"""
import sys  # 导入系统模块

import pygame   # 导入pygame模块
import pygame.locals    # 导入pygame本地策略
# from pygame.locals import *

# 背景类
class Background:
    # TODO 1.制作背景构造方法，传入图片路径，x,y
    def __init__(self,img_path,x,y):
        self.img = pygame.image.load(img_path)  # TODO 2.背景图片,传入图片路径
        self.x = x      # TODO 2.窗体中放置的x坐标
        self.y = y      # TODO 2.窗体中放置的y坐标
# 玩家类
class PlayerPlane:
    pass
# 敌机类
class EnemyPlane:
    pass
# 子弹类
class Bullet:
    pass
# 游戏类
class Game:
    # 主程序，运行游戏入口
    def run(self):
        self.frame_init()   # 执行窗体初始化

        self.model_init()   # TODO 4.执行对象初始化

        while True:     # 构造反复执行的机制，刷新窗体，使窗体保持在屏幕上
            pygame.display.update()     # 刷新窗体

            self.event_init()   # 反复调用事件监听方法

    # 初始化窗体
    def frame_init(self):
        self.window = pygame.display.set_mode((512, 768))    # 初始化窗体

        img = pygame.image.load("res/app.ico")  # 加载图标文件为图片对象
        pygame.display.set_icon(img)    # 设置窗体图标为图片
        pygame.display.set_caption("Plane Battle v1.0 传智播客·黑马程序员出品")    # 设置窗体的标题

    #  定义事件处理的方法
    def event_init(self):
        for event in pygame.event.get():    # 获取当前发生的所有事件
            if event.type == pygame.locals.QUIT :   # 判断当前事件类别是不是点击窗体的关闭按钮
                sys.exit()      # 执行退出系统操作

    # TODO 3.初始化窗体中的对象
    def model_init(self):
        background = Background("res/img_bg_level_1.jpg",0,0)   # TODO 5.初始化背景对象，传入图片路径，放置在0,0位
        self.window.blit(background.img, (background.x, background.y)) # TODO 6.调用bilt方法，将图片加入到窗体中

# 设置测试类入口操作
if __name__ == "__main__":
    Game().run()




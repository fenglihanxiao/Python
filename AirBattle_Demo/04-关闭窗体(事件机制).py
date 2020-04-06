"""
飞机大战——传智播客·黑马程序员出品
"""
import sys  # TODO 6.导入系统模块

import pygame   #  导入pygame模块
import pygame.locals    # TODO 5.导入pygame本地策略
# from pygame.locals import *


# 背景类
class Background:
    pass
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
    #  主程序，运行游戏入口
    def run(self):
        self.frame_init()   #  执行窗体初始化

        while True:     #  构造反复执行的机制，刷新窗体，使窗体保持在屏幕上
            pygame.display.update()     #  刷新窗体

            self.event_init()   # TODO 2.反复调用事件监听方法

    #  初始化窗体
    def frame_init(self):
        window = pygame.display.set_mode((512, 768))    #  初始化窗体

        img = pygame.image.load("res/app.ico")  # 加载图标文件为图片对象
        pygame.display.set_icon(img)    # 设置窗体图标为图片
        pygame.display.set_caption("Plane Battle v1.0 传智播客·黑马程序员出品")    # 设置窗体的标题

    # TODO 1.定义事件处理的方法
    def event_init(self):
        for event in pygame.event.get():    # TODO 3.获取当前发生的所有事件
            if event.type == pygame.locals.QUIT :   # TODO 4.判断当前事件类别是不是点击窗体的关闭按钮
                sys.exit()      # TODO 7.执行退出系统操作

#  设置测试类入口操作
if __name__ == "__main__":
    Game().run()




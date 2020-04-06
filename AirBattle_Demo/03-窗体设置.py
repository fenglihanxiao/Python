"""
飞机大战——传智播客·黑马程序员出品
"""
import pygame   #  导入pygame模块

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

    #  初始化窗体
    def frame_init(self):
        window = pygame.display.set_mode((512, 768))    #  初始化窗体

        img = pygame.image.load("res/app.ico")  # TODO 1.加载图标文件为图片对象
        pygame.display.set_icon(img)    # TODO 2.设置窗体图标为图片
        pygame.display.set_caption("Plane Battle v1.0 传智播客·黑马程序员出品")    # TODO 3.设置窗体的标题

#  设置测试类入口操作
if __name__ == "__main__":
    Game().run()




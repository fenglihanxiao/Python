"""
飞机大战——传智播客·黑马程序员出品
"""
import pygame   # TODO 5.导入pygame模块

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
    # TODO 1.主程序，运行游戏入口
    def run(self):
        self.frame_init()   # TODO 4.执行窗体初始化

        while True:     # TODO 7.构造反复执行的机制，刷新窗体，使窗体保持在屏幕上
            pygame.display.update()     # TODO 8.刷新窗体

    # TODO 3.初始化窗体
    def frame_init(self):
        window = pygame.display.set_mode((512, 768))    # TODO 6.初始化窗体


# TODO 2.设置测试类入口操作
if __name__ == "__main__":
    Game().run()
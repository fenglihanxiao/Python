"""
飞机大战——传智播客·黑马程序员出品
"""
import sys  #  导入系统模块
import random   #  导入随机数

import pygame   #  导入pygame模块
import pygame.locals    #  导入pygame本地策略

APP_ICON = "res/app.ico"    #  设计图片常量
IMG_BACKGROUND = "res/img_bg_level_1.jpg"   #  设计图片常量
#  设置敌机图片库常量元组
IMG_ENEMYS = ("res/img-plane_1.png","res/img-plane_2.png","res/img-plane_3.png","res/img-plane_4.png","res/img-plane_5.png","res/img-plane_6.png","res/img-plane_7.png")
IMG_PLAYER = "res/hero2.png"    #  设置玩家飞机图片
IMG_BULLET = "res/bullet_13.png"    #  设置子弹图片
#  创建所有显示的图形父类Model
class Model:
    window = None   #  主窗体对象，用于模型访问使用
    #  构造方法
    def __init__(self, img_path, x, y):
        self.img = pygame.image.load(img_path)  #  背景图片
        self.x = x  #  窗体中放置的x坐标
        self.y = y  #  窗体中放置的y坐标
    #  将模型加入窗体的方法抽取到父类
    def display(self):
        self.window.blit(self.img, (self.x, self.y))  # 填充图片到窗体中
    @staticmethod   #  碰撞操作与模型对象无关，属于模型相关操作，定义为静态方法
    def is_hit(rect1,rect2):     #  定义双方是否碰撞的静态方法
        return pygame.Rect.colliderect(rect1, rect2)     #  返回两个矩形是否相交，即是否碰撞
# 背景类
class Background(Model):
    #  定义背景移动的方法
    def move(self):
        #  加入判断
        if self.y <= Game.WINDOW_HEIGHT:   #  更新高度的引用  #  如果没有超出屏幕就正常移动
            self.y += 1  #  纵坐标自增1
        else:   #  如果超出屏幕，恢复图片位置为原始位置
            self.y = 0  #  纵坐标 = 0
    #  覆盖父类display方法，做辅助背景贴图
    def display(self):
        self.window.blit(self.img, (self.x, self.y))            #  原始背景贴图，推荐使用super().display()
        self.window.blit(self.img, (self.x, self.y - Game.WINDOW_HEIGHT))      #  更新高度的引用  #  辅助背景即将原始背景图片展示第二遍，坐标位置与第一遍展示上下拼接吻合
# 玩家类
class PlayerPlane(Model):
    #  覆盖init方法
    def __init__(self,img_path, x, y):
        super().__init__(img_path, x, y)    #  调用父类构造方法
        self.bullets = []   #  定义子弹列表为空，默认没有子弹
    #  覆盖display方法
    def display(self,enemys):   #  在显示飞机和子弹的同时，传入敌机列表，判断子弹是否与敌机相撞，添加enemys形参
        super().display()    #  调用父类方法
        remove_bullets = []     #  定义被删除的子弹列表
        for bullet in self.bullets:     #  循环子弹
            #  优化子弹存储队列，超出屏幕移出子弹
            if bullet.y < -29 :     #  如果子弹位置超出屏幕
                remove_bullets.append(bullet)   #  将要删除的子弹加入列表
            else:   #  如果子弹位置未超出屏幕范围
                rect_bullet = pygame.locals.Rect(bullet.x, bullet.y, 20, 29)    #  创建子弹矩形对象，传入x,y,width,height
                for enemy in enemys:    #  对未超出屏幕显示范围的子弹与所有敌机进行碰撞检测
                    rect_enemy = pygame.locals.Rect(enemy.x,enemy.y,100,68)     #  创建敌机矩形对象，传入x,y,width,height
                    #  调用碰撞检测方法，传入当前子弹对象，传入敌机对象，判断是否碰撞
                    if Model.is_hit(rect_bullet,rect_enemy) :   #  如果碰撞
                        enemy.is_hited = True   #  击中敌机即设置当前敌机为被击中状态
                        enemy.bomb.is_show = True       #  设置爆破效果状态开启
                        enemy.bomb.x = enemy.x  #  设置爆破效果开启位置x坐标
                        enemy.bomb.y = enemy.y  #  设置爆破效果开启位置y坐标
                        remove_bullets.append(bullet)   #  将产生碰撞的子弹加入删除列表
                        sound = pygame.mixer.Sound("res/bomb.wav")  #  添加混音音效文件
                        sound.play()    #  播放爆破效果音
                        break       #  当前子弹击中了一架敌机，终止对剩余敌机的碰撞检测，终止敌机循环
        for bullet in remove_bullets:   #  循环删除子弹列表
            self.bullets.remove(bullet)  #  从原始子弹列表中删除要删除的子弹

        rect_player = pygame.locals.Rect(self.x, self.y, 120, 78)   #  创建玩家矩形对象
        for enemy in enemys :   #  循环敌机列表
            #  调用碰撞检测方法，传入玩家对象，传入敌机对象，判断是否碰撞
            rect_enemy = rect_enemy = pygame.locals.Rect(enemy.x,enemy.y,100,68)    #  创建敌机矩形对象
            if Model.is_hit(rect_player,rect_enemy) :   #  如果碰撞
                enemy.is_hited = True   #  设置当前敌机为被击中状态
                pygame.mixer.music.load("res/gameover.wav")  #  加载游戏背景音乐文件为游戏结束
                pygame.mixer.music.play(loops=1)   #  播放背景音乐  loops=1 控制播放次数
                return 2    #  设置当前操作返回2,表示游戏结束
        return 1    #  设置正常操作状态下返回1，表示游戏进行中
# 敌机类
class EnemyPlane(Model):
    #  覆盖init方法
    def __init__(self):
        img = IMG_ENEMYS[random.randint(0,len(IMG_ENEMYS)-1)]   #  设置图片路径随机从元组中获取
        x = random.randint(0, Game.WINDOW_WIDTH - 100)  #  设置x坐标随机生成 横向位置 0 到 屏幕宽度 - 飞机宽度(100)
        y = random.randint(-Game.WINDOW_HEIGHT, -68)    #  设置y坐标随机生成 纵向位置 -屏幕高度 到 -飞机高度
        super().__init__(img,x,y)   #  调用父类构造方法
        self.is_hited = False   #  添加敌机被击中的状态
        self.bomb = Bomb()      #  为敌机添加绑定的爆破效果对象
    #   定义敌机移动的方法
    def move(self):
        #  控制敌机到达底部后，返回顶部
        if self.y < Game.WINDOW_HEIGHT and not self.is_hited : #  添加敌机被击中的状态判定     #  敌机未超出屏幕
            self.y += 4 #  控制敌机移动速度
        else:   #  敌机超出屏幕
            self.img = pygame.image.load(IMG_ENEMYS[random.randint(0, len(IMG_ENEMYS) - 1)])    #  修改敌机到达底部后返回的图片随机生成，同初始化策略
            self.x = random.randint(0, Game.WINDOW_WIDTH - 100) #  修改敌机到达底部后返回顶部的策略，x随机生成，同初始化策略
            self.y = random.randint(-Game.WINDOW_HEIGHT, -68)   #  修改敌机到达底部后返回顶部的策略，y随机生成，同初始化策略
            self.is_hited = False       #  重置敌机是否被击中状态为未被击中，False

    def display(self):  #  覆盖父类显示方法
        super().display()   #  调用父类显示方法，用于显示敌机自身
        if self.bomb.is_show :  #  如果开启爆破效果
            self.bomb.display() #  调用爆破对象的显示方法
# 子弹类
class Bullet(Model):
    #   定义子弹移动的方法
    def move(self):
        self.y -= 12    #  控制子弹移动速度
# 爆炸效果类
class Bomb(Model): #  创建爆炸效果类
    def __init__(self):     #  定义单独的初始化方法
        self.x = None       #  定义爆炸显示的横坐标x
        self.y = None       #  定义爆炸显示的纵坐标y
        self.imgs = [ pygame.image.load("res/bomb-"+str(i)+".png") for i in range(1,7)]     #  加载爆炸效果使用的所有图片列表
        self.is_show = False    #  定义是否开启爆破效果属性
        self.times = 0      #  定义爆破图片展示控制变量

    def display(self):      #  定义单独的贴图显示方法
        if self.is_show and self.times < len(self.imgs) * 10 : #  延长播放次数，放大循环次数，拉长播放时间  #  控制爆破展示每次一轮，不能超过边界  #  如果开启爆破效果
            self.window.blit(self.imgs[self.times // 10], (self.x, self.y)) #  延长播放次数，放大循环次数，拉长播放时间  #  修改爆破图片展示每次递增  #  展示爆破图片第一张图片，用于测试效果
            self.times += 1     #  控制变量每次+1
        else:   #  控制爆破展示完毕后恢复状态
            self.times = 0          #  控制爆破展示完毕后恢复后下次展示图片从第一个开始
            self.is_show = False    #  控制爆破展示完毕后恢复后设置为不开始爆炸效果

        # 游戏类
class Game:
    WINDOW_WIDTH = 512  #  定义窗体宽度常量
    WINDOW_HEIGHT = 768 #  定义窗体高度常量

    #  定义构造方法
    def __init__(self):
        self.game_status = 0  #  初始化游戏状态，0（默认）表示游戏未开始，1 表示游戏进行中，2 表示游戏结束

    #  主程序，运行游戏入口
    def run(self):
        pygame.init()   #  初始化pygame读取系统操作
        pygame.mixer.init() #  初始化背景音乐模块

        self.frame_init()   #  执行窗体初始化
        self.model_init()   #  执行元素初始化

        pygame.mixer.music.load("res/bg.wav")   #  加载背景音乐文件
        pygame.mixer.music.play()                #  播放背景音乐

        while True:     #  构造反复执行的机制，刷新窗体，使窗体保持在屏幕上
            self.background.move()  #  背景操作放置在游戏状态判定外面，始终保持   # 调用背景移动操作，反复执行，构造背景向下的画面
            self.background.display()  #  背景操作放置在游戏状态判定外面，始终保持 # 反复刷新背景

            if self.game_status == 0 :  #  判定游戏未开始状态操作
                font_over = pygame.font.Font("res/DENGB.TTF", 40)  # TODO  设置大字体
                text_over = font_over.render("飞机大战", 1, (255, 255, 0))  # TODO  设置文字
                self.window.blit(text_over, pygame.locals.Rect(256 - 80, 200, 226, 43))  # TODO  设置显示位置

                font_over = pygame.font.Font("res/DENGB.TTF", 18)  # TODO  设置小字体
                text_over = font_over.render("请选择难度", 1, (255, 255, 255))
                self.window.blit(text_over, pygame.locals.Rect(256 - 45, 300, 226, 43))

                font_over = pygame.font.Font("res/DENGB.TTF", 30)  # TODO  设置中字体
                text_over = font_over.render("1-简单", 1, (0, 255, 0))
                self.window.blit(text_over, pygame.locals.Rect(256 - 46, 340, 226, 43))

                text_over = font_over.render("2-普通", 1, (255, 255, 255))
                self.window.blit(text_over, pygame.locals.Rect(256 - 46, 390, 226, 43))

                text_over = font_over.render("3-别开玩笑", 1, (255, 0, 0))
                self.window.blit(text_over, pygame.locals.Rect(256 - 152 / 2, 440, 226, 43))
            elif self.game_status == 1 :  #  判定游戏进行中状态
                for enemy in self.enemys:  # 加入所有敌机
                    enemy.move()  # 每驾敌机移动
                    enemy.display()  # 每驾敌机贴图

                self.game_status = self.player.display(
                    self.enemys)  # 接收到游戏状态，备用   #  飞机加入时，传入敌机列表实参self.enemys #  玩家飞机贴图

                for bullet in self.player.bullets:  # 循环子弹
                    bullet.display()  # 每个子弹贴图
                    bullet.move()  # 调用子弹移动操作
            elif self.game_status == 2 :  #  判定游戏结束状态
                font_over = pygame.font.Font("res/DENGB.TTF", 40)               #  创建字体对象
                text_obj = font_over.render("GAME OVER", 1, (255, 0, 0))        #  创建文本对象
                self.window.blit(text_obj, pygame.locals.Rect(143,300,226,43))  # 添加文本对象到屏幕上

            pygame.display.update()  #  界面刷新操作，始终保持 # 刷新窗体
            self.event_init()  #  事件相关操作，始终保持 # 反复监控是否存在事件执行

    #  初始化窗体
    def frame_init(self):
        self.window = pygame.display.set_mode((Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT))    #  更新宽度和高度的引用  #  初始化窗体
        Model.window = self.window  #  将窗体对象传入模型类中
        img = pygame.image.load(APP_ICON)  #  修改图片地址为常量引用 #  加载图标文件为图片对象
        pygame.display.set_icon(img)    #  设置窗体图标为图片
        pygame.display.set_caption("Plane Battle v1.0 传智播客·黑马程序员出品")    #  设置窗体的标题


    #  初始化事件
    def event_init(self):
        for event in pygame.event.get():    #  获取所有的事件
            if event.type == pygame.locals.QUIT:    #  判断是不是点击的关闭按钮
                sys.exit()  #  系统退出
            if event.type == pygame.locals.MOUSEMOTION and self.game_status == 1: #  设置监听鼠标移动事件
                pos = pygame.mouse.get_pos()        #  获取鼠标位置
                self.player.x = pos[0]  - 120/2     #  设置飞机中心位置在鼠标位置(x)  横坐标 - 飞机宽度1半
                self.player.y = pos[1]  -78/2 +5    #  设置飞机中心位置在鼠标位置(y)  纵坐标 - 飞机高度1半 +-微调数据

            if event.type == pygame.locals.KEYDOWN and self.game_status == 0 :
                if event.key == 49 or event.key == pygame.locals.K_1:
                    for _ in range(5):  # 循环产生5架敌机
                        self.enemys.append(EnemyPlane())  # 修改创建敌机操作 # 初始位置x为横向随机，纵向200
                        self.game_status = 1
                elif event.key == pygame.locals.K_2:
                    for _ in range(30):  # 循环产生5架敌机
                        self.enemys.append(EnemyPlane())  # 修改创建敌机操作 # 初始位置x为横向随机，纵向200
                        self.game_status = 1
                elif event.key == 51:
                    for _ in range(300):  # 循环产生5架敌机
                        self.enemys.append(EnemyPlane())  # 修改创建敌机操作 # 初始位置x为横向随机，纵向200
                        self.game_status = 1
            if event.type == pygame.locals.KEYDOWN and self.game_status == 1 :
                if event.key == 61:
                    self.enemys.append(EnemyPlane())
                elif event.key == 45:
                    self.enemys.pop()
        if self.game_status == 1:
            press = pygame.mouse.get_pressed() #  获取鼠标按键压下状态，返回得到元组，其中保存鼠标左中右键按下状态（1,0,0）
            if press[0] == 1 :  #  判断左键是否按下
                pos = pygame.mouse.get_pos()  #  获取鼠标位置
                bullet = Bullet(IMG_BULLET,pos[0] - 20 / 2 , pos[1]  - 78 / 2 - 29)  #  创建子弹，横坐标为鼠标x坐标 - 子弹宽度1半，纵坐标为鼠标y坐标 - 飞机高度1版 - 子弹高度
                self.player.bullets.append(bullet)  #  加入飞机子弹列表



    #  初始化窗体中的元素
    def model_init(self):
        self.background = Background(IMG_BACKGROUND, 0 , 0 )     #  初始化背景对象，使用图片路径常量，放置在0,0位
        self.enemys = []    #  定义敌机列表，保存多驾敌机
        self.player = PlayerPlane(IMG_PLAYER,200,500)       #  初始化玩家飞机对象，放置在200,500

#  设置测试类入口操作
if __name__ == "__main__":
    Game().run()
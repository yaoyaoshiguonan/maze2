import pygame
import config

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 50
        self.forward_angle = 30 # 在游戏坐标系中，顺时针转动的角度
        self.image_source = pygame.image.load("static/images/car.png").convert()
        self.image = pygame.transform.scale(self.image_source,(self.width,self.height))
        self.image = pygame.transform.rotate(self.image, -self.forward_angle)

        self.image.set_colorkey("black")

        self.rect = self.image.get_rect()
        self.rect.center = (config.SCREEN_WIDTH/2,config.SCREEN_HEIGHT/2)
        self.last_time = pygame.time.get_ticks()#返回当前时刻
        self.delta_time = 0 #相邻两帧之间时间间隔

        self.move_velocity_limit = 220  # 移动速度的上限
        self.move_velocity = 0  # 当前的移动速度
        self.move_acc = 600  # 每秒将速度增加600
        self.friction = 0.9  # 摩擦力



    def update_delta_time(self):
        cur_time = pygame.time.get_ticks()
        self.delta_time = cur_time - self.last_time/1000 #将单位转化程秒
        self.last_time = cur_time


    def input(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            self.move_velocity += self.move_acc * self.delta_time
            self.move_velocity = min(self.move_velocity_limit, self.move_velocity)
        elif key_pressed[pygame.K_s]:
            self.move_velocity -= self.move_acc * self.delta_time
            self.move_velocity = max(self.move_velocity, -self.move_velocity_limit)
        else:
            self.move_velocity = int(self.move_velocity * self.friction)
    def move(self):
        self.rect.x+= self.move_velocity * self.delta_time


    def update(self):
        self.update_delta_time()
        self.input()
        self.move()
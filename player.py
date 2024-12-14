import pygame
import config
import math
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
        self.rotate_velocity = 0  # 角速度
        self.rotate_velocity_limit = 140  # 角速度上限

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
        sign = 1
        if self.move_velocity < 0:
            sign = -1
        if key_pressed[pygame.K_d]:
            self.rotate_velocity = self.rotate_velocity_limit*sign
        elif key_pressed[pygame.K_a]:
            self.rotate_velocity = -self.rotate_velocity_limit*sign
        else:
            self.rotate_velocity = 0

    def rotate(self):
        self.forward_angle += self.rotate_velocity*self.delta_time
        self.image = pygame.transform.scale(self.image_source, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, -self.forward_angle)
        self.image.set_colorkey("black")
        #更新中心点位置
        #使转动中心变为中心点
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def move(self):
        if abs(self.move_velocity) > 50:
            self.rotate()# 只有车在前进或后退时，车身角度才会变化；原地不动打方向班，车身角度是不变的
            vx = self.move_velocity * math.cos(math.pi*self.forward_angle/180)
            vy = self.move_velocity * math.sin(math.pi*self.forward_angle/180)
            self.rect.x += vx * self.delta_time
            self.rect.y += vy * self.delta_time

    def update(self):
        self.update_delta_time()
        self.input()
        self.move()
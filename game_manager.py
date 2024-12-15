import pygame
from player import Player
from wall import Wall
from star import Star
from target import Target
from utils.collided import collided_rect, collided_circle

class GameManager:
    def __init__(self,screen,level):
        self.screen = screen
        self.player = None
        self.level = level
        self.walls = pygame.sprite.Group()
        self.stars_cnt = 0
        self.stars = pygame.sprite.Group()
        self.targets = pygame.sprite.Group()
        wall = Wall(200,200,500,5)
        wall.add(self.walls)

    def load_walls(self, walls):
        self.walls.empty()  # 清空
        for x, y, width, height in walls:
            wall = Wall(x, y, width, height)
            wall.add(self.walls)

    def load_stars(self, stars):
        self.stars.empty()
        for x, y in stars:
            star = Star(x, y)
            star.add(self.stars)

    def load_player(self, center_x, center_y, forward_angle):
        if self.player:
            self.player.kill()
        self.player = Player(center_x, center_y, forward_angle)

    def load(self):  # 加载当前这一关的地图信息
        with open("static/maps/level%d.txt" % self.level, 'r') as fin:
            walls_cnt = int(fin.readline())
            walls = []
            for i in range(walls_cnt):
                x, y, width, height = map(int, fin.readline().split())
                walls.append((x, y, width, height))
            self.load_walls(walls)
            self.stars_cnt = int(fin.readline())
            stars = []
            for i in range(self.stars_cnt):
                x, y = map(int, fin.readline().split())
                stars.append((x, y))
            self.load_stars(stars)


    def check_collide(self):  # 检测碰撞
        if pygame.sprite.spritecollide(self.player, self.walls, False,collided_rect):
            self.player.crash()

    def updates(self):
        self.stars.update()
        self.stars.draw(self.screen)
        self.targets.update()
        self.targets.draw(self.screen)
        self.player.update()
        self.check_collide()
        self.screen.blit(self.player.image, self.player.rect)
        self.walls.update()
        self.walls.draw(self.screen)


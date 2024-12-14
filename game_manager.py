import pygame
from player import Player
from wall import Wall
from utils.collided import collided_rect, collided_circle

class GameManager:
    def __init__(self,screen,level):
        self.screen = screen
        self.player = Player()
        self.level = level
        self.walls = pygame.sprite.Group()
        wall = Wall(200,200,500,5)
        wall.add(self.walls)

    def load_walls(self, walls):
        self.walls.empty()  # 清空
        for x, y, width, height in walls:
            wall = Wall(x, y, width, height)
            wall.add(self.walls)

    def load(self):  # 加载当前这一关的地图信息
        with open("static/maps/level%d.txt" % self.level, 'r') as fin:
            walls_cnt = int(fin.readline())
            walls = []
            for i in range(walls_cnt):
                x, y, width, height = map(int, fin.readline().split())
                walls.append((x, y, width, height))
            self.load_walls(walls)


    def check_collide(self):  # 检测碰撞
        if pygame.sprite.spritecollide(self.player, self.walls, False,collided_rect):
            self.player.crash()

    def updates(self):
        self.player.update()
        self.check_collide()
        self.screen.blit(self.player.image, self.player.rect)
        self.walls.update()
        self.walls.draw(self.screen)


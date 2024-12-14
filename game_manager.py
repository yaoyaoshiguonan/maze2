import pygame
from player import Player
from wall import Wall
from utils.collided import collided_rect, collided_circle

class GameManager:
    def __init__(self,screen):
        self.screen = screen
        self.player = Player()
        self.walls = pygame.sprite.Group()
        wall = Wall(200,200,500,5)
        wall.add(self.walls)


    def check_collide(self):  # 检测碰撞
        if pygame.sprite.spritecollide(self.player, self.walls, False,collided_rect):
            self.player.crash()

    def updates(self):
        self.player.update()
        self.check_collide()
        self.screen.blit(self.player.image, self.player.rect)
        self.walls.update()
        self.walls.draw(self.screen)


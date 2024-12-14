import pygame
from player import Player
from wall import Wall

class GameManager:
    def __init__(self,screen):
        self.screen = screen
        self.player = Player()
        self.walls = pygame.sprite.Group()
        wall = Wall(200,200,500,5)
        wall.add(self.walls)


    def updates(self):
        self.player.update()
        self.screen.blit(self.player.image, self.player.rect)
        self.walls.update()
        self.walls.draw(self.screen)
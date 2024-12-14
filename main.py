import pygame
import config
from player import Player

pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH,config.SCREEN_WIDTH))
clock = pygame.time.Clock()

player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    player.update()
    screen.blit(player.image,player.rect)#画屏幕之后再画小车
    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
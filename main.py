import pygame
import config
from game_manager import GameManager

pygame.init()
pygame.mixer.init()  # 初始化声音

screen = pygame.display.set_mode((config.SCREEN_WIDTH,config.SCREEN_WIDTH))
clock = pygame.time.Clock()




game_manager=GameManager(screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    game_manager.updates()

    pygame.display.flip()

    clock.tick(config.FPS)

pygame.quit()
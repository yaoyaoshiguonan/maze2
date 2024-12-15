import pygame


class Target(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__()
        self.image_source = pygame.image.load("static/images/target.png")
        self.image = pygame.transform.scale(self.image_source, (100, 100))
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect()
        self.rect.center = (center_x, center_y)
        self.scale = 1
        self.scale_delta = 0.01

    def update(self):
        pass
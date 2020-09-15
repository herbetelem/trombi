import pygame


class Student(pygame.sprite.Sprite):
    
    def __init__(self, avatar, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(avatar)
        self.image = pygame.transform.scale(self.image, (220, 176))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
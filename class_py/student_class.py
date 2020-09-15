import pygame


class Student(pygame.sprite.Sprite):
    
    def __init__(self, x, y, id_student, name, first_name, avatar, prescriber, project, why, job):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(avatar)
        self.image = pygame.transform.scale(self.image, (220, 176))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.id = id_student
        self.name = name
        self.first_name = first_name
        self.prescriber = prescriber
        self.project = project
        self.why = why
        self.job = job
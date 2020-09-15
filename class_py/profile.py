import pygame


class Profile():
    
    def __init__(self, width, height):
        self.profile_selected = False
        self.background = pygame.image.load("asset/background_profile.jpg")
        self.background = pygame.transform.scale(self.background, (width, height))
        
    def launch_profile(self, name):
        self.profile_selected = True
        self.name = name
        # modifier plus tard
        self.avatar = pygame.image.load("asset/" + self.name + ".jpg")
        ####################
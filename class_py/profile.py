import pygame

from class_py.home import Home
from class_py.requeteSQL import SQL

class Profile():
    
    def __init__(self, width, height):
        self.profile_selected = False
        self.background = pygame.image.load("asset/background_profile.jpg")
        self.background = pygame.transform.scale(self.background, (width, height))
        # ? self.rect_story = self.story_blit.get_rect()      
        # ? self.rect_future = self.future_blit.get_rect()  méthode à tester pour création rect en fonction du texte
        self.text_font = pygame.font.Font(None, 50)
        self.test = "J'aime la nature et les petits oiseaux"
        # self.story = result requete sql
        # self.future = result requete sql
        self.story_blit = self.text_font.render(self.test, 1, (0, 0, 0))
        self.future_blit = self.text_font.render("caca", 1, (0, 0, 0))


    def launch_profile(self, name):
        self.profile_selected = True
        self.home = Home()
        self.name = name
        # modifier plus tard
        self.avatar = pygame.image.load("asset/" + self.name + ".png")
        self.avatar = pygame.transform.scale(self.avatar, (300, 280))
        ####################
        
    def return_home(self):
        self.profile_selected = False
        
    def update(self, screen):
        screen.blit(self.avatar, (50, 50))
        screen.blit(self.story_blit, (450, 50))
        screen.blit(self.future_blit, (450, 350))

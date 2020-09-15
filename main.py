import pygame
import math

from class_py.student_class import Student
from class_py.profile import Profile



pygame.init()


# set la taille de l'écran
screen_width = 1060
screen_height = 730

# generer la fenetre du jeu
pygame.display.set_caption("Trombinoscope")
screen = pygame.display.set_mode((screen_width, screen_height))

# importer et charger le background*
background = pygame.image.load('asset/background.jpg')
background = pygame.transform.scale(background, (screen_width, screen_height))

list_licorne = []

##############################
#   Recuperation des avatars #
#   pour Laura               #
##############################
list_coordone = [[100, 50], [420, 50], [740, 50], 
                 [100, 276], [420, 276], [740, 276], 
                 [100, 502], [420, 502], [740, 502]]

# a virer apres ton travail
#########################################
list_licorne.append(Student("asset/laura.png", 100, 50, "Laura"))
list_licorne.append(Student("asset/aurelia.png", 420, 50, "Aurélia"))
list_licorne.append(Student("asset/avatar.png", 740, 50, "Mélanie"))
list_licorne.append(Student("asset/alex.png", 100, 276, "Alex"))
list_licorne.append(Student("asset/alexandre.png", 420, 276, "Alexandre"))
list_licorne.append(Student("asset/guillaume.png", 740, 276, "Guillaume"))
list_licorne.append(Student("asset/willfried.png", 100, 502, "Willfried"))
list_licorne.append(Student("asset/hadrien.jpg", 420, 502, "Hadrien"))
list_licorne.append(Student("asset/javier.png", 740, 502, "Javier"))

#########################################

# Instance de profile
profile = Profile(screen_width, screen_height)

running = True

# boucle tant que running est vrai
while running:
    if profile.profile_selected:
        screen.blit(profile.background, (0,0))
        profile.update(screen)
    else:
        # appliquer le background
        screen.blit(background, (0,0))

        for avatar in list_licorne:
            screen.blit(avatar.image, avatar.rect)

    # update le screen
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # check que l'event est le fait de fermer la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Le jeu ce ferme")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if profile.profile_selected == False:
                for avatar in list_licorne:
                    if avatar.rect.collidepoint(event.pos):
                        profile.launch_profile(avatar.name)
            else:
                if profile.home.rect.collidepoint(event.pos):
                    profile.return_home()

import pygame
import math

from class_py.student_class import Student
from class_py.requeteSQL import SQL
from class_py.profile import Profile



pygame.init()


# set la taille de l'écran
screen_width = 1500
screen_height = 1000

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
list_coordonnée = [[100, 50],  [420, 50],  [740, 50], 
                 [100, 276], [420, 276], [740, 276], 
                 [100, 502], [420, 502], [740, 502]]
                 

sql = SQL()
sql.requeteSQL()

def create_student():
    for num in range(10) :
        list_licorne.append(Student(list_coordonnée[num][0], list_coordonnée[num][1], 
        sql.MyResult[num][0], sql.MyResult[num][1], sql.MyResult[num][2], sql.MyResult[num][3], 
        sql.MyResult[num][4], sql.MyResult[num][5], sql.MyResult[num][6], sql.MyResult[num][9]))



# a virer apres ton travail
#########################################
# list_licorne.append(Student("asset/laura.png", 100, 50, "Laura"))
# list_licorne.append(Student("asset/avatar.png", 420, 50, "Aurélia"))
# list_licorne.append(Student("asset/avatar.png", 740, 50, "Mélanie"))
# list_licorne.append(Student("asset/alex.png", 100, 276, "Alex"))
# list_licorne.append(Student("asset/avatar.png", 420, 276, "Alexandre"))
# list_licorne.append(Student("asset/avatar.png", 740, 276, "Guillaume"))
# list_licorne.append(Student("asset/avatar.png", 100, 502, "Willfried"))
# list_licorne.append(Student("asset/hadrien.jpg", 420, 502, "Hadrien"))
# list_licorne.append(Student("asset/javier.png", 740, 502, "Javier"))

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
            print("Le jeu se ferme")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if profile.profile_selected == False:
                for avatar in list_licorne:
                    if avatar.rect.collidepoint(event.pos):
                        profile.launch_profile(avatar.name)
            else:
                if profile.home.rect.collidepoint(event.pos):
                    profile.return_home()

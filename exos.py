import pygame
import sys

# Initialiser Pygame
pygame.init()

# Créer une fenêtre de jeu
screen = pygame.display.set_mode((800, 600))

# Charger une texture (une image)
texture = pygame.image.load('C:\Users\eline\OneDrive\Images\Captures décran\2023-10-08184710')

# Boucle de jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    # Appliquer la texture à un objet (par exemple, un rectangle)
    screen.blit(texture, (100, 100))
   
    # Mettre à jour l'affichage
    pygame.display.flip()



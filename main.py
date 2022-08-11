import pygame
import math
from game import Game
pygame.init()



pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')

# importenotre baniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importe le bouton de commancement
play_button = pygame.image.load('assets/button.png')
play_button= pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)


#charger notre jeu
game = Game()

running = True



# boucle tant que cette condition est vrai
while running:

    screen.blit(background, (0, -200))

    # verifier si notre jeu a commenceou non .
    if game.is_playing:
        # declencher les instructions de la partie
         game.update(screen)
    # verifier si le jeu a pas commance
    else:
        # ajoute l'ecrant de bienveunue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)



    #mettre a jour l'ecran
    pygame.display.flip()


    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture...")

       #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est enclanche pour lance notre projectile
            if event.key == pygame.K_SPACE:
               game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # metre le jeu en mode (lance)
                game.start()


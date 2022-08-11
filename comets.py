import pygame
import random


# creer une clase pour genere cette comete

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definir l'image de la comets
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(-0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        #
        if len (self.comet_event.all_comets) == 0 :
            # remetre la barre a 0
            self.comet_event.reset_percent()
            # apparaitre les 2 premiers montre
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()


    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            print("sol")
            # retire la boule de feu
            self.remove()


            # si il n'y a plus de boule de feu
            if len (self.comet_event.all_comets) == 0:
                print("l'evenement est fini")
                # remetre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False


        # verigier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_player
        ):
            print("joueur touche !")
            # retire la boule de feu
            self.remove()
            # subire 20 points de vie
            self.comet_event.game.player.damage(20)

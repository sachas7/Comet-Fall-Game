import pygame
from comets import Comet


# creet une class pour gere evenemtn a interval regulier
class CometFallEvent:

    # lors du chargement -> creer un compyeur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 15
        self.game = game
        self.fall_mode = False

        # definir un groupe de striker nos comets
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def reset_percent(self):
        self.percent = 0

    def is_Full_loaded(self):
        return self.percent >= 100

    def meteor_fall(self):
        # apparaitre 1 premiere boule de feu
        self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'evenement est totalement charge
        if self.is_Full_loaded() and len (self.game.all_monster) == 0:
            print("pluie de comets !!")
            self.meteor_fall()
            self.fall_mode = True # pour active l'evenement

    def update_bar(self, surface):
        # ajoute du pourcentge a la bar
        self.add_percent()

        # barre noir (en arrier plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # l'axe des x
            surface.get_height() - 20,  # l'axe des y
            surface.get_width(),  # longeur de la fennetre
            10  # epaisseur de la barre
        ])
        # barre rouge (jauge d'avent)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l'axe des x
            surface.get_height() - 20,  # l'axe des y
            (surface.get_width() / 100) * self.percent,  # longeur de la fennetre
            10  # epaisseur de la barre
        ])

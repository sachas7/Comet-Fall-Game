import pygame
from monster import Monster
from comet_event import CometFallEvent
from player import Player


# creer une seconde classe qui va represente notre jeu
class Game:


    def __init__(self):
        # definir si notre jeu a commence ou non
        self.is_playing = False
        # generer notre joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        # generer l 'evenement
        self.comet_event = CometFallEvent(self)
        # groupe de monstre
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}



    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # remetre le jeu a neuf , retire les monstre remetre le joueur a 100 de vie remtre le jeu en attente
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)


        # actualise la barre devement du jeux
        self.comet_event.update_bar(screen)


        # recupere les projectile du joueur
        for projectile in self.player.all_projectile:
            projectile.move()

        # recupere les monstre de notre jeu
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)

        # recupere les comets de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()


        # applique l'ansemble des image de mon groupe de projectile
        self.player.all_projectile.draw(screen)

        # appliquer l'ensemble des image de mon groupe de monster
        self.all_monster.draw(screen)

        # applique l'emsemble des image de mon groupe de commet
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueur veut alle a droite ou a gauche
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monster.add(monster)

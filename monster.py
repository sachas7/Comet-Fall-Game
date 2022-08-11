import pygame
import random




class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 70
        self.max_health = 70
        self.attack = 0.3
        self.velocity = random.randint(1, 2)
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540


    def damage(self,amount):
        # Inflige les degats
        self.health -= amount

        # verifier si son nouveau nombre de points de vie est infrieure ou egale a 0
        if self.health <= 0:
            # reaparaitre comme un nouveau montre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health

            #si la barre d'evenement est charge a son max
            if self.game.comet_event.is_Full_loaded():
                # retire du jeu
                self.game.all_monster.remove(self)
                # appel de la metode pour esseye de declanche la plui
                self.game.comet_event.attempt_fall()






    def update_health_bar(self, surface):

        # defiinire la position de notre jauge de vie ainsi que la largeur et son epaisseur
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]

        #definir la position de l'arriere plan de notre jauge de vie
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), back_bar_position)
        pygame.draw.rect(surface, (111, 210, 46), bar_position)


    def forward(self):
        #le deplacement ne se fait que si ya pas de colision avec un joueur
        if not self.game.check_collision(self, self.game.all_player):
          self.rect.x -= self.velocity
        #si le onstre est en collision avec le joueur
        else:
            #inflige des degats (au joueur )
            self.game.player.damage(self.attack)





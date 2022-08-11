import pygame
from projectile import Projectile

# creer une premier classe qui va represente notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 300
        self.max_health = 300
        self.attack = 10
        self.velocity = 3
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load('assets/Player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur na plus de vie
            self.game.game_over()

    def update_health_bar(self, surface):
        # defiinire la position de notre jauge de vie ainsi que la largeur et son epaisseur
        bar_position = [self.rect.x + 10, self.rect.y + 20, self.health, 12]

        # definir la position de l'arriere plan de notre jauge de vie
        back_bar_position = [self.rect.x + 10, self.rect.y + 20, self.max_health, 12]

        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), back_bar_position)
        pygame.draw.rect(surface, (111, 210, 46), bar_position)

    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile
        self.all_projectile.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monster):
           self.rect.x += self.velocity

    def move_left(self):

        self.rect.x -= self.velocity

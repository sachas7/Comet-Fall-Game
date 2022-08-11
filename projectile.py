import pygame

# definire la classe qui va gere le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    #definire le constructeur de cette class
    def __init__(self,  player):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourne le projectile
        self.angle += 50
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self):
       self.rect.x += self.velocity
       self.rotate()

       # verifier si le projectile entre en colisionavec un monstre
       for monster in  self.player.game.check_collision(self, self.player.game.all_monster):
           # supprime le projectile
           self.remove()
           # inflige des degats
           monster.damage(self.player.attack)


       # verifier si notre projectile n'est plus prsent sur l'ecran
       if self.rect.x > 1080:

          # supprime le projectile (en dehors de l'ecran)
        self.remove()
        print("projectile suprime")



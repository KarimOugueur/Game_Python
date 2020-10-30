import pygame


#Sprite : GUI Class
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player= player
        self.velocity = 10 # projectile speed
        self.image= pygame.image.load('assets/projectile.png')  # load image
        self.image= pygame.transform.scale(self.image, (50,50)) #resize image
        self.rect = self.image.get_rect()   #size image
        self.rect.x= player.rect.x + 120
        self.rect.y=player.rect.y + 82
        self.origin_image= self.image
        self.angle = 0

    def rotate(self):
        #rotate projectile
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect= self.image.get_rect(center=self.rect.center)  #turn on the center

    #delete prjectile
    def remove(self):
        self.player.all_projectiles.remove(self)


    def move(self):
        self.rect.x += self.velocity  # projectiles go right
        self.rotate()

        # if projectile is not collides with monster
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # delete projectile
            self.remove()
            #infliger les dégats
            monster.damage(self.player.attack)

        if self.rect.x > 1080: # delete projectile if go out
            self.remove()




import pygame
import random
from projectile import Projectile



# class Player
class Player(pygame.sprite.Sprite):


    def __init__(self, game): # charging class player
        super().__init__()
        self.game= game
        self.health = 100
        self.max_health= 100
        self.attack = 5
        self.velocity = 20
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()  # recover player
        self.rect.x = 400
        self.rect.y = 500



    def launch_projectile(self):
        projectile = Projectile(self)  #instance projectiles
        self.all_projectiles.add(projectile)


    def move_right(self):

        # if the player is not a collides with monster
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        else:
            self.game.player.damage(self.attack)

    def move_left(self):
        self.rect.x -= self.velocity


    def update_health_bar(self, surface):

        # Set the monster's life gauge position, thickness and width
        bar_position = [self.rect.x +50 , self.rect.y + 15, self.health, 10]
        #postion back bar
        back_bar_position = [self.rect.x +50, self.rect.y +15, self.max_health, 10]

        # draw the life bar
        pygame.draw.rect(surface, (60, 63, 60), back_bar_position)
        pygame.draw.rect(surface, (111, 210, 46), bar_position)

    def damage(self, amount):
        #inflict damage
        if self.health-amount > amount:
            self.health -= amount
        else:
            self.game.game_over()


    def remove_player(self):
        if self.game.check_collision(self, self.game.all_monsters):
            self.health = self.max_health-self.health
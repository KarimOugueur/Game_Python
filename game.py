import pygame

from player import Player
from monster import Monster

# classe game
class Game:

    def __init__(self):
          self.is_playing = False
          self.all_players = pygame.sprite.Group()  #groupe players
          self.player = Player(self)  # generate player
          self.all_players.add(self.player)  #add player in group
          self.all_monsters = pygame.sprite.Group()  # group of monster
          self.pressed = {}


    def start(self):
         self.is_playing = True
         self.spawn_monter()
         self.spawn_monter()

    def game_over(self):
         self.all_monsters= pygame.sprite.Group()
         self.player.health = self.player.max_health
         self.is_playing = False


    def update(self, scrren):
         # apply player on the GUI
         scrren.blit(self.player.image, self.player.rect)

         # player life bar
         self.player.update_health_bar(scrren)

         # retrieve the projectiles
         for projectile in self.player.all_projectiles:
             projectile.move()

         # retrieve the monster
         for monster in self.all_monsters:
             monster.go_forward()
             monster.update_health_bar(scrren)

         # apply projectile
         self.player.all_projectiles.draw(scrren)

         # apply monster on GUI
         self.all_monsters.draw(scrren)  # draw monster on GUI

         # go left or right
         if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < scrren.get_width():
             self.player.move_right()
         elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
             self.player.move_left()



    #collisions
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monter(self):
        monster=Monster(self)  # creat a monster object
        self.all_monsters.add(monster)  # add a new monster every thing
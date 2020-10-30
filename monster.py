import pygame
import random
class Monster(pygame.sprite.Sprite):


    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image= pygame.image.load('assets/mummy.png')
        self.rect= self.image.get_rect()
        self.rect.x =1000 + random.randint(0,350)
        self.rect.y = 540
        self.velocity = random.randint(1,3)

    def damage(self, amount):
        #inflict damage
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 350)
            self.velocity = random.randint(1,3)
            self.health = self.max_health

    def update_health_bar(self, surface):
        #color for monster
        bar_color = (111, 210, 46)
        # back bar color
        back_bar_color = (60, 63, 60)

        # Set the monster's life gauge position, thickness and width
        bar_position = [self.rect.x +20, self.rect.y - 20, self.health, 10]

        #postion back bar
        back_bar_position = [self.rect.x +20, self.rect.y -20, self.max_health, 10 ]

        # draw the life bar
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)




    def go_forward(self):
        # if monster is not collides with player
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

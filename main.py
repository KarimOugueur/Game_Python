import pygame
import math
from game import Game

pygame.init()


# genrate a window of our game

pygame.display.set_caption("Comet fall Game")    # window title
scrren= pygame.display.set_mode((1080, 720))   # window dimension

# game background
background= pygame.image.load('assets/bg.jpg')

#upade the banner
banner = pygame.image.load('assets/banner.png')
banner =  pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x= math.ceil(scrren.get_width() / 4)

#update button play
play_button= pygame.image.load('assets/button.png')
play_button =pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(scrren.get_width() / 3.33)
play_button_rect.y = math.ceil(scrren.get_height() / 2)


# load player
game = Game()

#light up
running= True

while running:

    # apply backroun window
    scrren.blit(background,(0, -200))

    # check if the game has started
    if game.is_playing:
        game.update(scrren)
    else:
        scrren.blit(play_button, play_button_rect)
        scrren.blit(banner, banner_rect)

    # update window
    pygame.display.flip()



    for event in pygame.event.get():
        if event.type==pygame.QUIT:   #close the window
            running=False
            pygame.quit()
            print("close window")

        # detetc displacement

        elif event.type== pygame.KEYDOWN:
            game.pressed[event.key] = True

            #laucnh projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key]=False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if the mouse is in collision with the button
            if play_button_rect.collidepoint(event.pos):
                game.start()






          #  if event.key== pygame.K_RIGHT:
           #     game.player.move_right()
           # elif event.key == pygame.K_LEFT:
            #    game.player.move_left()
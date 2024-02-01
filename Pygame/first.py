import pygame
pygame.init()

white=(255, 255, 255)
game_window=pygame.display.set_mode((900,600))
pygame.display.set_caption("Snake Game")

exit_game=False

while exit_game==False:

    game_window.fill(white)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
            
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("You pressed right key!")


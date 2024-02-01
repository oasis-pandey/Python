import pygame

pygame.init() #initializing pygame module

pygame.display.set_mode((1200,500)) #creating a game window
pygame.display.set_caption("My First Game") #title for the window

#game specific variables
game_over=False
game_exit=False

# while game_exit==False:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             game_exit=True

#         if event.type==pygame.KEYDOWN:
#             if event.key==pygame.K_RIGHT:
#                 print("You pressed right key!")
# pygame.quit()
# quit()

while game_exit==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_exit=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("You pressed right arrow key!")

pygame.quit()
quit()


    
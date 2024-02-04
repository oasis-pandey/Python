import pygame
import random
pygame.init()

#GAME WINDOW
length=900
width=600
game_window=pygame.display.set_mode((length, width))
pygame.display.set_caption("Snake Game!")

#GAME VARIABLES
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
snake_x=20
snake_y=20
snake_size=20
quit_game=False
velocity_x=0
velocity_y=0

#Food 
food_x=random.randint(10,width/2)
food_y=random.randint(10,length/2)




clock=pygame.time.Clock()
fps=30

while quit_game==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                quit_game=True

        if event.type==pygame.KEYDOWN:
            velocity_x=0
            velocity_y=0
            if event.key==pygame.K_LEFT:
                velocity_x-=5
                velocity_y=0
            elif event.key==pygame.K_RIGHT:
                velocity_x+=5
                velocity_y=0
            elif event.key==pygame.K_UP:
                velocity_y-=5
                velocity_x=0
            elif event.key==pygame.K_DOWN:
                velocity_y+=5
                velocity_x=0

    snake_x+=velocity_x
    snake_y+=velocity_y
    game_window.fill(white)
    pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(game_window, black,[snake_x,snake_y, snake_size, snake_size])   
    pygame.display.update() 
    clock.tick(fps)
    


                
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
snake_x=50
snake_y=50
snake_size=20
quit_game=False
velocity_x=0
velocity_y=0
score=0

#Food 
food_x=random.randint(20,width/2)
food_y=random.randint(20,length/2)

def display_score(score,color,x,y):
    font=pygame.font.SysFont(None, 55)
    text=font.render("Score: "+ str(score), True, color)
    game_window.blit(text,(x,y))
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
                velocity_x-=8
                velocity_y=0
            elif event.key==pygame.K_RIGHT:
                velocity_x+=8
                velocity_y=0
            elif event.key==pygame.K_UP:
                velocity_y-=8
                velocity_x=0
            elif event.key==pygame.K_DOWN: 
                velocity_y+=8
                velocity_x=0
                   
    if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<8:
        score+=10
        food_x=random.randint(10,width/2)
        food_y=random.randint(10,length/2)
       
              
    snake_x+=velocity_x
    snake_y+=velocity_y
    game_window.fill(white)
    display_score(score, black, 10, 10)  
    pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(game_window, black,[snake_x,snake_y, snake_size, snake_size])   
    pygame.display.update() 
    clock.tick(fps)
    


                
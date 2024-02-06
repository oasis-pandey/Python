import pygame
import random
pygame.init()

#GAME WINDOW
length=900
width=600
game_window=pygame.display.set_mode((length, width))
pygame.display.set_caption("Snake Game!")






def display_score(score,color,x,y):
    font=pygame.font.SysFont(None, 55)
    text=font.render("Score: "+ str(score), True, color)
    game_window.blit(text,(x,y))

def plot_snake(game_window, color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window, color,[x, y, snake_size, snake_size]) 

def generate_food(game_window, color,x, y, food_size):
    pygame.draw.rect(game_window, color, [x, y, food_size, food_size])

#FPS for the game
clock=pygame.time.Clock()
fps=30

def gameloop():
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
    snake_length=1

    #SNK_LIST is empty , but "head" list will be appended into it everytime ( check line 74)
    snk_list=[]
    #Food 
    food_x=random.randint(20,width/2)
    food_y=random.randint(20,length/2)
    while quit_game==False:
    #GAME CONTROLS 
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

        #takes the coordinate of snake, appends into the head list and then appends "head " list into snk_list
        head=[]
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        #Prevents the snake from leaving black trace everywhere it goes.
        if len(snk_list)>snake_length:
            del snk_list[0]

        #Condition if snake eats the food:
        if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<8:
            score+=10
            food_x=random.randint(10,width/2)
            food_y=random.randint(10,length/2)
            snake_length+=5
        
                
        snake_x+=velocity_x # changing x coordinate of snake 
        snake_y+=velocity_y # changing y coordinate of snake 
        game_window.fill(white) # fills the entire game window with white color
        display_score(score, black, 10, 10)  #displays score into game window intead of terminal
        generate_food(game_window, red, food_x, food_y, 20) # generates food randomly 
        plot_snake(game_window, black,snk_list, snake_size) # plots the snake
        pygame.display.update() #updates the display 
        clock.tick(fps) # implementing the clock feature

gameloop()
    
 

                
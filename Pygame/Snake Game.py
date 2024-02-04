import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snake Game!")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0

food_x = random.randint(20, screen_width/2)
food_y = random.randint(20, screen_height/2)
score = 0
init_velocity = 5
snake_size = 30
fps = 60

clock = pygame.time.Clock()

# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = - init_velocity
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = - init_velocity
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
        score +=1
        print("Score: ", score * 10)
        food_x = random.randint(20, screen_width / 2)
        food_y = random.randint(20, screen_height / 2)

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()



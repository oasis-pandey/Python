import pygame
pygame.init()

white=(255, 255, 255)
black=(0, 0, 0)

snake_size=10
snake_x=500
snake_y=100
velocity_x=4
velocity_y=4

game_window=pygame.display.set_mode((900,600))
pygame.display.set_caption("Snake Game")
fps=30

exit_game=False
clock=pygame.time.Clock()

while exit_game==False:
    clock.tick(fps)
    game_window.fill(white)

    snake_x += velocity_x
    snake_y+=velocity_y
#Creating a rectangle(snake's head):
    pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_size, snake_size])
# arguments in order: where to draw, which color (RGB value),[x coordinate, y coordinate, length, width]

    pygame.display.update()   

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                snake_x+=10
            elif event.key==pygame.K_LEFT:
                snake_x-=10
            elif event.key==pygame.K_DOWN:
                snake_y+=10
            elif event.key==pygame.K_UP:
                snake_y-=10
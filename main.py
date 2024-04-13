import pygame
import random
import sys

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WIDTH, HEIGHT = 1000, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SnakeGame')
snake_block = 10
snake_speed = 15

font = pygame.font.SysFont('Arial', 25)


def message(msg, color):
  mesg = font.render(msg, True, color)
  screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def draw_snake(snake_block, snake_list):
  for x in snake_list:
    pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])


def generate_food():
  foodx = round(
      random.randrange(snake_block, WIDTH - snake_block) / 10.0) * 10.0
  foody = round(
      random.randrange(snake_block, HEIGHT - snake_block) / 10.0) * 10.0
  return foodx, foody


def gameLoop():
  game_over = False
  game_close = False

  x1, y1 = WIDTH / 2, HEIGHT / 2
  x1_change, y1_change = 0, 0

  snake_list = []
  snake_length = 1

  foodx, foody = generate_food()

  while not game_over:
    while game_close:
      screen.fill(WHITE)
      message('Вы проиграли. Нажмите R-чтобы играть снова.', RED)
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            game_over = True
            game_close = False
          elif event.key == pygame.K_r:
            gameLoop()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_over = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          x1_change = -snake_block
          y1_change = 0
        elif event.key == pygame.K_RIGHT:
          x1_change = snake_block
          y1_change = 0
        elif event.key == pygame.K_UP:
          y1_change = -snake_block
          x1_change = 0
        elif event.key == pygame.K_DOWN:
          y1_change = snake_block
          x1_change = 0
    if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
      game_close = True
    x1 += x1_change
    y1 += y1_change

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, [0, 0, WIDTH, snake_block])
    pygame.draw.rect(screen, BLUE,
                     [0, HEIGHT - snake_block, WIDTH, snake_block])
    pygame.draw.rect(screen, BLUE, [0, 0, snake_block, HEIGHT])
    pygame.draw.rect(screen, BLUE,
                     [WIDTH - snake_block, 0, snake_block, HEIGHT])
    pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])
    snake_head = [x1, y1]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
      del snake_list[0]
    for segment in snake_list[:-1]:
      if segment == snake_head:
        game_close = True
    draw_snake(snake_block, snake_list)
    pygame.display.update()
    if x1 == foodx and y1 == foody:
      foodx, foody = generate_food()
      snake_length += 1
    pygame.time.Clock().tick(snake_speed)

  pygame.quit()
  sys.exit()


gameLoop()

import pygame, random

FOOD_AMOUNT = 5

class Food:
  def __init__(self, dis, block_size: tuple, snake_body: list) -> None:
    self.dis = dis
    self.block_size = block_size
    self.snake_body = snake_body

  def restart(self) -> None:
    self.food = []
    for _ in range(FOOD_AMOUNT):
      self.spawn()

  def spawn(self) -> None:
    size = self.dis.get_size()

    new_food = tuple([
      round(random.randrange(0, size[0] - self.block_size[0]) / 10.0) * 10.0,
      round(random.randrange(0, size[1] - self.block_size[1]) / 10.0) * 10.0
    ])

    if new_food in self.snake_body or new_food in self.food:
      self._createFood(size)
    else:
      self.food.append(new_food)

  def checkCollision(self, next_pos: tuple) -> bool:
    return next_pos in self.food
  
  def draw(self):
    for pos in self.food:
      pygame.draw.rect(
        self.dis, (0, 0, 255),
        pos + self.block_size
      )

  def remove(self, value):
    self.food.remove(value)

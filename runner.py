import pygame, random

from snake import Snake

TICKRATE = 15
BLOCK_SIZE = (10, 10)
FOOD_AMOUNT = 5

class Runner:
  # Create pygame window
  def __init__(self, size):
    pygame.init()

    self.dis = pygame.display.set_mode(size)
    self.clock = pygame.time.Clock()

    self.snake = Snake(self.dis, BLOCK_SIZE)
    self._restart()

  # Game loop
  def run(self):
    # try/catch handles KeyboardInterrupt
    try:
      while True:
        for event in pygame.event.get():
          match event.type:
            # Break from while True loop if user closes window
            case pygame.QUIT:
              break
            case pygame.KEYDOWN:
              self._controls(event)
        else:
          if self.status != "Game Over":
            next_pos = self.snake.nextPos()

            if self.snake.checkCollision(next_pos):
              self.status = "Game Over"
              self.snake.color = (255, 0, 0)
              self._updateCaption()
            else:
              self.snake.move(next_pos)
              self._checkFood()
            self._draw()

          self.clock.tick(TICKRATE)
          continue
        break
    except KeyboardInterrupt:
      pass

    pygame.quit()
    quit()

  def _updateCaption(self):
    pygame.display.set_caption(f'Cobrinha by Caio Stoduto © 2023 | Score: {self.score} | Status: {self.status}')

  def _checkFood(self):
    if self.snake.body[0] in self.food:
      self.food.remove(self.snake.body[0])
      self.snake.size += 1
      self.score += 1
      self._updateCaption()
      self._createFood(self.dis.get_size())

  def _createFood(self, size):
    new_food = tuple([
      round(random.randrange(0, size[0] - BLOCK_SIZE[0]) / 10.0) * 10.0,
      round(random.randrange(0, size[1] - BLOCK_SIZE[1]) / 10.0) * 10.0
    ])

    if new_food in self.snake.body or new_food in self.food:
      self._createFood(size)
    else:
      self.food.append(new_food)

  def _restart(self):
    self.status = "Running"
    self.snake.restart()
    self.score = 0
    self._updateCaption()

    self.food = []
    for _ in range(FOOD_AMOUNT):
      self._createFood(self.dis.get_size())

  def _controls(self, event):
    match event.key:
      case pygame.K_LEFT | pygame.K_a:
        self.snake.setVel((-BLOCK_SIZE[0], 0))
      case pygame.K_RIGHT | pygame.K_d:
        self.snake.setVel((+BLOCK_SIZE[0], 0))
      case pygame.K_UP | pygame.K_w:
        self.snake.setVel((0, -BLOCK_SIZE[1]))
      case pygame.K_DOWN | pygame.K_s:
        self.snake.setVel((0, +BLOCK_SIZE[1]))
      case pygame.K_r:
        self._restart()

  def _draw(self):
    self.dis.fill((0, 0, 0))
    self.snake.draw()
    self._drawFood()
    pygame.display.update()

  def _drawFood(self):
    for pos in self.food:
      pygame.draw.rect(
        self.dis, (0, 0, 255),
        pos + BLOCK_SIZE
      )

if __name__ == '__main__':
  Runner((990, 490)).run()

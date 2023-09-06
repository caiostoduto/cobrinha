import pygame, snake, food

TICKRATE = 15
BLOCK_SIZE = (10, 10)

class Runner:
  # Create pygame window
  def __init__(self, size):
    pygame.init()

    self.dis = pygame.display.set_mode(size)
    self.clock = pygame.time.Clock()

    self.snake = snake.Snake(self.dis, BLOCK_SIZE)
    self.food = food.Food(self.dis, BLOCK_SIZE, self.snake.body)
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
              self._checkFood(next_pos)
              self.snake.move(next_pos)
            self._draw()

          self.clock.tick(TICKRATE)
          continue
        break
    except KeyboardInterrupt:
      pass

    pygame.quit()
    quit()

  def _updateCaption(self):
    pygame.display.set_caption(f'Cobrinha by Caio Stoduto © 2023 | Score: {self.snake.size - snake.SNAKE_SIZE} | Status: {self.status}')

  def _checkFood(self, next_pos: tuple):
    if self.food.checkCollision(next_pos):
      self.food.remove(next_pos)
      self.snake.size += 1
      self.food.spawn()
      self._updateCaption()

  def _restart(self):
    self.status = "Running"
    self.snake.restart()
    self.food.restart()
    self._updateCaption()

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
    self.food.draw()
    pygame.display.update()

if __name__ == '__main__':
  Runner((990, 490)).run()

import pygame


class Runner:
  # Create pygame window
  def __init__(self, size):
    pygame.init()
    self.dis = pygame.display.set_mode(size)
    self.clock = pygame.time.Clock()

    self.tickrate = 15
    self.block_size = (10, 10)
    self._reload(size)

    pygame.display.set_caption('Cobrinha by Caio Stoduto © 2023')

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
          if self.game_over == False:
            next_snake_pos = self._calcNextSnakePos()
            if self._checkCollision(next_snake_pos):
              self.game_over = True
              self.snake_color = (255, 0, 0)
            else:
              self._moveSnake(next_snake_pos)
            self._draw()

          self.clock.tick(self.tickrate)
          continue
        break
    except KeyboardInterrupt:
      pass

    pygame.quit()
    quit()

  def _reload(self, size):
    self.vel = (0, 0)
    self.game_over = False
    self.snake_color = (0, 255, 0)
    self.snake_pos = tuple(
      sum(ti) / 2 for ti in zip(size, self.block_size)
    )

  def _calcNextSnakePos(self) -> tuple:
    return tuple(
      sum(ti) for ti in zip(self.snake_pos, self.vel)
    )

  def _moveSnake(self, next_snake_pos: tuple):
    self.snake_pos = next_snake_pos

  def _checkCollision(self, next_snake_pos: tuple) -> bool:
    return next_snake_pos[0] < 0 or next_snake_pos[1] < 0 \
      or next_snake_pos[0] > self.dis.get_width() - self.block_size[0] / 2 \
      or next_snake_pos[1] > self.dis.get_height() - self.block_size[1] / 2 

  def _controls(self, event):
    match event.key:
      case pygame.K_LEFT | pygame.K_a:
        if self.vel != (+self.block_size[0], 0):
          self.vel = (-self.block_size[0], 0)
      case pygame.K_RIGHT | pygame.K_d:
        if self.vel != (-self.block_size[0], 0):
          self.vel = (+self.block_size[0], 0)
      case pygame.K_UP | pygame.K_w:
        if self.vel != (0, +self.block_size[1]):
          self.vel = (0, -self.block_size[1])
      case pygame.K_DOWN | pygame.K_s:
        if self.vel != (0, -self.block_size[1]):
          self.vel = (0, +self.block_size[1])
      case pygame.K_r:
        self._reload(self.dis.get_size())

  def _draw(self):
    self.dis.fill((0, 0, 0))
    self._drawSnake()
    pygame.display.update()

  def _drawSnake(self):
    pygame.draw.rect(
      self.dis, self.snake_color,
      self.snake_pos + self.block_size
    )

if __name__ == '__main__':
  Runner((990, 490)).run()

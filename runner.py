import pygame


class Runner:
  # Create pygame window
  def __init__(self, size):
    pygame.init()
    self.dis = pygame.display.set_mode(size)
    self.clock = pygame.time.Clock()

    self.tickrate = 15
    self.vel = (0, 0)

    self.snake_color = (0, 255, 0)
    self.block_size = (10, 10)
    self.snake_pos = tuple(
      sum(ti) / 2 for ti in zip(size, self.block_size)
    )

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
          self._draw()
          self.clock.tick(self.tickrate)
          continue
        break
    except KeyboardInterrupt:
      pass

    pygame.quit()
    quit()

  def _controls(self, event):
    match event.key:
      case pygame.K_LEFT | pygame.K_a:
        self.vel = (-self.block_size[0], 0)
      case pygame.K_RIGHT | pygame.K_d:
        self.vel = (+self.block_size[0], 0)
      case pygame.K_UP | pygame.K_w:
        self.vel = (0, -self.block_size[1])
      case pygame.K_DOWN | pygame.K_s:
        self.vel = (0, +self.block_size[1])

  def _draw(self):
    self.dis.fill((0, 0, 0))
    self._drawSnake()
    pygame.display.update()

  def _drawSnake(self):
    self.snake_pos = tuple(
      sum(ti) for ti in zip(self.snake_pos, self.vel)
    )
    
    pygame.draw.rect(
      self.dis, self.snake_color,
      self.snake_pos + self.block_size
    )

if __name__ == '__main__':
  Runner((1000, 500)).run()

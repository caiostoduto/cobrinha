import pygame, random

BLOCK_SIZE = (10, 10)
FOOD_AMOUNT = 5

class Runner:
  # Create pygame window
  def __init__(self, size):
    pygame.init()
    self.dis = pygame.display.set_mode(size)
    self.clock = pygame.time.Clock()

    self.tickrate = 15
    self._restart(size)

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
            next_head_pos = self._calcNextSnakePos()

            if self._checkCollision(next_head_pos):
              self.status = "Game Over"
              self.snake_color = (255, 0, 0)
              self._updateCaption()
            else:
              self._moveSnake(next_head_pos)
              self._checkFood()
            self._draw()

          self.clock.tick(self.tickrate)
          continue
        break
    except KeyboardInterrupt:
      pass

    pygame.quit()
    quit()

  def _updateCaption(self):
    pygame.display.set_caption(f'Cobrinha by Caio Stoduto © 2023 | Score: {self.score} | Status: {self.status}')

  def _checkFood(self):
    if self.snake_body[0] in self.food:
      self.food.remove(self.snake_body[0])
      self.snake_size += 1
      self.score += 1
      self._updateCaption()
      self._createFood(self.dis.get_size())

  def _createFood(self, size):
    new_food = tuple([
      round(random.randrange(0, size[0] - BLOCK_SIZE[0]) / 10.0) * 10.0,
      round(random.randrange(0, size[1] - BLOCK_SIZE[1]) / 10.0) * 10.0
    ])

    if new_food in self.snake_body or new_food in self.food:
      self._createFood(size)
    else:
      self.food.append(new_food)

  def _restart(self, size):
    self.vel = (0, 0)
    self.last_vel = (0, 0)
    self.status = "Running"
    self.snake_color = (0, 255, 0)
    self.snake_size = 4
    self.score = 0
    self._updateCaption()
    self.snake_body = [
      tuple(sum(ti) / 2 for ti in zip(size, BLOCK_SIZE))
    ]

    self.food = []
    for _ in range(FOOD_AMOUNT):
      self._createFood(self.dis.get_size())

  def _calcNextSnakePos(self) -> list:
    return tuple(
      sum(ti) for ti in zip(self.snake_body[0], self.vel)
    )

  def _moveSnake(self, next_head_pos: list):
    self.snake_body = [next_head_pos] + self.snake_body[0:self.snake_size - 1]
    self.last_vel = self.vel

  def _checkCollision(self, next_head_pos: tuple) -> bool:
    return self._checkCollisionBorder(next_head_pos) \
      or self._checkCollisionSnakeBody(next_head_pos)
  
  def _checkCollisionSnakeBody(self, next_head_pos: tuple) -> bool:
    return next_head_pos in self.snake_body and next_head_pos != self.snake_body[0]

  def _checkCollisionBorder(self, next_head_pos: tuple) -> bool:
    return next_head_pos[0] < 0 or next_head_pos[1] < 0 \
      or next_head_pos[0] > self.dis.get_width() - BLOCK_SIZE[0] \
      or next_head_pos[1] > self.dis.get_height() - BLOCK_SIZE[1]

  def _controls(self, event):
    match event.key:
      case pygame.K_LEFT | pygame.K_a:
        if self.last_vel != (+BLOCK_SIZE[0], 0):
          self.vel = (-BLOCK_SIZE[0], 0)
      case pygame.K_RIGHT | pygame.K_d:
        if self.last_vel != (-BLOCK_SIZE[0], 0):
          self.vel = (+BLOCK_SIZE[0], 0)
      case pygame.K_UP | pygame.K_w:
        if self.last_vel != (0, +BLOCK_SIZE[1]):
          self.vel = (0, -BLOCK_SIZE[1])
      case pygame.K_DOWN | pygame.K_s:
        if self.last_vel != (0, -BLOCK_SIZE[1]):
          self.vel = (0, +BLOCK_SIZE[1])
      case pygame.K_r:
        self._restart(self.dis.get_size())

  def _draw(self):
    self.dis.fill((0, 0, 0))
    self._drawSnake()
    self._drawFood()
    pygame.display.update()

  def _drawFood(self):
    for pos in self.food:
      pygame.draw.rect(
        self.dis, (0, 0, 255),
        pos + BLOCK_SIZE
      )

  def _drawSnake(self):
    for pos in self.snake_body:
      pygame.draw.rect(
        self.dis, self.snake_color,
        pos + BLOCK_SIZE
      )

if __name__ == '__main__':
  Runner((990, 490)).run()

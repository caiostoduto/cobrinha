import pygame, re, snake, food

TICKRATE = 15
BLOCK_SIZE = (10, 10)

class Runner:
  # Create pygame window
  def __init__(self, size):
    pygame.init()

    self.dis = pygame.display.set_mode(size)
    self.clock = pygame.time.Clock()
    self.score = (0, 0)

    self.player0 = snake.Snake(
      self.dis,
      BLOCK_SIZE,
      tuple(10 * round(ti[0] / 40) for ti in zip(self.dis.get_size(), BLOCK_SIZE))
    )

    self.player1 = snake.Snake(
      self.dis,
      BLOCK_SIZE,
      tuple(10 * round(3 * ti[0] / 40) for ti in zip(self.dis.get_size(), BLOCK_SIZE))
    )

    self.food = food.Food(self.dis, BLOCK_SIZE)
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
          if self.status == "Running":
            collision = [False, False]

            for idx, player in enumerate([self.player0, self.player1]):
              next_pos = player.nextPos()

              if player.checkCollision(next_pos):
                collision[idx] = True
                player.color = (255, 0, 0)
              else:
                self._checkFood(player, next_pos)
                player.move(next_pos)
            
            self._draw()

            if collision[0] != collision[1]:
              idx = collision.index(True)

              self.status = f"Player {0 if idx == 1 else 1} wins"
              self.score = tuple(
                self.score[i] + (0 if i == idx else 1) for i in range(2)
              )

              self._updateCaption()
            elif collision[0] and collision[1]:
              self.status = "Draw"
              self._updateCaption()

          self.clock.tick(TICKRATE)
          continue
        break
    except KeyboardInterrupt:
      pass

    pygame.quit()
    quit()

  def _updateCaption(self):
    pygame.display.set_caption(f'Cobrinha by Caio Stoduto © 2023 | Score: {" v ".join(map(str, self.score))} | Status: {self.status}')

  def _checkFood(self, player: snake.Snake, next_pos: tuple):
    if self.food.checkCollision(next_pos):
      self.food.remove(next_pos)
      player.size += 1
      self.food.spawn(self.player0.body + self.player1.body)
      self._updateCaption()

  def _restart(self):
    self.status = "Running"
    self.player0.restart()
    self.player1.restart()
    self.food.restart(self.player0.body + self.player1.body)
    self._updateCaption()

  def _controls(self, event):
    match event.key:
      case pygame.K_a:
        self.player0.setVel((-BLOCK_SIZE[0], 0))
      case pygame.K_d:
        self.player0.setVel((+BLOCK_SIZE[0], 0))
      case pygame.K_w:
        self.player0.setVel((0, -BLOCK_SIZE[1]))
      case pygame.K_s:
        self.player0.setVel((0, +BLOCK_SIZE[1]))
      case pygame.K_LEFT | pygame.K_a:
        self.player1.setVel((-BLOCK_SIZE[0], 0))
      case pygame.K_RIGHT | pygame.K_d:
        self.player1.setVel((+BLOCK_SIZE[0], 0))
      case pygame.K_UP | pygame.K_w:
        self.player1.setVel((0, -BLOCK_SIZE[1]))
      case pygame.K_DOWN | pygame.K_s:
        self.player1.setVel((0, +BLOCK_SIZE[1]))
      case pygame.K_r:
        self._restart()

  def _draw(self):
    self.dis.fill((0, 0, 0))
    for player in [self.player0, self.player1]:
      player.draw()
    self.food.draw()
    pygame.display.update()

if __name__ == '__main__':
  Runner((990, 490)).run()

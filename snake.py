import pygame

SNAKE_SIZE = 4

class Snake:
  def __init__(self, dis, block_size: tuple, start_pos) -> None:
    self.dis = dis
    self.block_size = block_size
    self.start_pos = start_pos

  def restart(self) -> None:
    self.size = SNAKE_SIZE
    self.color = (0, 255, 0)
    self.body = [self.start_pos]
    self._vel = (0, 0)
    self._last_vel = (0, 0)

  def move(self, next_pos: tuple) -> None:
      self.body = [next_pos] + self.body[0:self.size - 1]
      self._last_vel = self._vel

  def nextPos(self) -> tuple:
    return tuple(
      sum(ti) for ti in zip(self.body[0], self._vel)
    )
  
  def draw(self) -> None:
    for pos in self.body:
      pygame.draw.rect(
        self.dis, self.color,
        pos + self.block_size
      )
  
  def setVel(self, vel: tuple) -> None:
    if self._last_vel != (-vel[0], -vel[1]):
      self._vel = vel

  def checkCollision(self, next_pos: tuple, oponnent) -> bool:
    return self._checkBorderCollision(next_pos) \
      or self._checkBodyCollision(next_pos) \
      or self._checkOpponentCollision(next_pos, oponnent)

  def _checkBorderCollision(self, next_pos: tuple) -> bool:
    return next_pos[0] < 0 or next_pos[1] < 0 \
      or next_pos[0] > self.dis.get_width() - self.block_size[0] \
      or next_pos[1] > self.dis.get_height() - self.block_size[1]

  def _checkBodyCollision(self, next_pos: tuple) -> bool:
    return next_pos in self.body and next_pos != self.body[0]
 
  def _checkOpponentCollision(self, next_pos: tuple, oponnent) -> bool:
    return next_pos in tuple(oponnent.body[0:oponnent.size - 1]) + oponnent.nextPos()

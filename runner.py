import pygame

class Runner:
  # Create pygame window
  def __init__(self, size):
    pygame.init()
    self.dis = pygame.display.set_mode(size)
    pygame.display.update()
    pygame.display.set_caption('Cobrinha by Caio Stoduto © 2023')

  # Game loop
  def run(self):
    while True:
      for event in pygame.event.get():
        # Break from while True loop if user closes window
        if event.type == pygame.QUIT:
          break
      else:
         continue
      break
    
    pygame.quit()
    quit()

if __name__ == '__main__':
  Runner((1000, 500)).run()

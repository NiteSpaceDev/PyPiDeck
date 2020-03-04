# PyPiDeck - Main app control class

# Bring in pygame module
import pygame

class app:
  def __init__(self):
    print("App loading")

  def main(self):
    # Initialize things
    pygame.init()

    # Load some stuff
    pygame.display.set_caption("PyPiDeck")

    # Create a screen surface
    screen = pygame.display.set_mode([640,480])

    # Setup loop
    running = True
    while running:
      running = loopEvent()
      loopUpdate(screen)
      pygame.display.flip()

  def loopEvent(self): # return false if we're exiting
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return False
    return True

  def loopUpdate(self, screen):
    screen.fill((255,255,255))
    color = (255,0,255)
    pos = (100,100)
    size = 50
    pygame.draw.circle(screen, color, pos, size)


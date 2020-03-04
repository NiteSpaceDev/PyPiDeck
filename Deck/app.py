# PyPiDeck - Main app control class

# Bring in pygame module
import pygame

from sys import exit

class app:
  def __init__(self):
    print("App loading")
    self.running = True

  def main(self):
    # Initialize things
    pygame.display.init()

    # Load some stuff
    pygame.display.set_caption("PyPiDeck")

    # Create a screen surface
    self.screen = pygame.display.set_mode([640,480])

    # Setup loop
    while self.running:
      self.running = self.loopEvent()
      self.loopUpdate()
      pygame.display.flip()

    print("we're quitting")
    pygame.quit()
    print("we're out")

  def loopEvent(self): # return false if we're exiting
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
        return False
      if event.type == pygame.MOUSEBUTTONDOWN:
        print("click")
        self.running = False
        return False
    return True

  def loopUpdate(self):
    self.screen.fill((255,255,255))
    color = (255,0,255)
    pos = (100,100)
    size = 50
    pygame.draw.circle(self.screen, color, pos, size)


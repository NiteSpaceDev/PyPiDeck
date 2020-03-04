# Start building round 1 in PyGame
# Target Platform is Raspberry Pi w/ Touchscreen input

# Bring in pygame module
import pygame

def main():
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

def loopEvent(): # return false if we're exiting
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      return False
  return True

def loopUpdate(screen):
  screen.fill((255,255,255))
  color = (255,0,255)
  pos = (100,100)
  size = 50
  pygame.draw.circle(screen, color, pos, size)

# Start things up if we're being run from here
if __name__ == "__main__":
  main()
import pygame

white = (255, 255, 255)
black = (0, 0, 0)
(width, height) = (300, 300) # Dimension of the window
screen = pygame.display.set_mode((width, height)) # Making of the screen

gridSize = 10
 
def grid():
  for y in range(1, gridSize):
    pygame.draw.line(screen, white, (0, (height / gridSize) * y), (width, (height / gridSize) * y), 1)
    
  for x in range(1, gridSize):
    pygame.draw.line(screen, white, ((width / gridSize) * x, 0), ((width / gridSize) * x, height), 1)
      
def fillCell(x, y):
  if x < 1 or x > gridSize or y < 1 or y > gridSize:
    raise Exception("Invalid coords: " + str(x) + ":" + str(y)); 

  pygame.draw.rect(screen, white, (x * (width / gridSize), y * (height / gridSize), (width / gridSize), (height / gridSize)))

running = True
while running:
  screen.fill(black)
  
  grid()
  fillCell(3, 3)
  fillCell(5, 7)

  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()


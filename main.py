import pygame
import random
from datetime import datetime

white = (255, 255, 255)
black = (0, 0, 0)
(width, height) = (300, 300) # Dimension of the window
screen = pygame.display.set_mode((width, height)) # Making of the screen

gridSize = 10
updateTime = 0.5

def drawGrid():
  for y in range(1, gridSize):
    pygame.draw.line(screen, white, (0, (height / gridSize) * y), (width, (height / gridSize) * y), 1)
    
  for x in range(1, gridSize):
    pygame.draw.line(screen, white, ((width / gridSize) * x, 0), ((width / gridSize) * x, height), 1)
      
def fillCell(x, y):
  if x < 0 or x > gridSize or y < 0 or y > gridSize:
    raise Exception("Invalid coords: " + str(x) + ":" + str(y)); 

  pygame.draw.rect(screen, white, (x * (width / gridSize), y * (height / gridSize), (width / gridSize), (height / gridSize)))

board = [
  [0,0,0,0,0,0,0,0,0,0],
  [0,1,1,0,0,0,0,0,0,0],
  [0,0,1,1,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,1,1,0,0,0,0],
  [0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,1,0,0,0,0],
  [0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,0,0,1],
  [0,0,0,0,0,0,0,0,1,1]
]

def neighbourCount(x,y):
  count = 0;
  
  if x > 0:
    count = count + board[y][x-1]
    
  if x > 0 and y > 0:
    count = count +board[y-1][x-1]

  if x > 0 and y < gridSize - 1:
    count = count +board[y+1][x-1]
    
  if y > 0:
    count = count +board[y-1][x]

  if y < gridSize - 1:
    count = count +board[y+1][x]  
    
  if x < gridSize - 1:
    count = count +board[y][x+1]
    
  if x < gridSize - 1 and y > 0:
    count = count +board[y-1][x+1]

  if x < gridSize - 1 and y < gridSize - 1:
    count = count +board[y+1][x+1]
    
  return count

def processBoard():
  global board
  boardCopy = board
  for y in range(len(board)):
    for x in range(len(board[y])):
      nc = neighbourCount(x, y)
      if board[y][x] == 1 and (nc == 2 or nc ==3):
        boardCopy[y][x] = 1
      elif board[y][x] == 0 and nc == 3:
        boardCopy[y][x] = 1
      else:
        boardCopy[y][x] = 0
      
  board = boardCopy

def drawCells():
  for y in range(len(board)):
    for x in range(len(board[y])):
      if board[y][x] == 1:
        fillCell(x, y)

running = True
prevTime = datetime.now()

while running:
  time = datetime.now()
  screen.fill(black)
  
  if (time - prevTime).total_seconds() > updateTime:
    processBoard()
    prevTime = time

  drawGrid()
  drawCells()
  pygame.display.flip()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()


import pygame
import random
from datetime import datetime

white = (255, 255, 255)
black = (0, 0, 0)
(width, height) = (800, 800) # Dimension of the window
screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption("Cellular automaton")

gridSize = 100
drawGridLines = False
updateTime = 0.05

board = [];

def initBoard():
  for y in range(gridSize):
    row = []
    for x in range(gridSize):
      row.append(0)
    board.append(row)

def drawGrid():
  for y in range(1, gridSize):
    pygame.draw.line(screen, white, (0, int((height / gridSize) * y)), (width, int((height / gridSize) * y)), 1)
    
  for x in range(1, gridSize):
    pygame.draw.line(screen, white, (int((width / gridSize) * x), 0), (int((width / gridSize) * x), height), 1)
      
def fillCell(x, y):
  if x < 0 or x > gridSize or y < 0 or y > gridSize:
    raise Exception("Invalid coords: " + str(x) + ":" + str(y)); 

  pygame.draw.rect(screen, white, (x * int(width / gridSize), int(y * (height / gridSize)), int(width / gridSize), int(height / gridSize)))

def placePattern(pattern, offset_x, offset_y):
  global board
  for y in range(len(pattern)):
    for x in range(len(pattern[y])):
      if offset_y + y < len(board) and offset_x + x < len(board[offset_y + y]):
        board[offset_y + y][offset_x + x] = pattern[y][x]

def neighbourCount(x,y):
  count = 0;
  
  if x > 0:
    count = count + board[y][x-1]
    
  if x > 0 and y > 0:
    count = count + board[y-1][x-1]

  if x > 0 and y < gridSize - 1:
    count = count + board[y+1][x-1]
    
  if y > 0:
    count = count + board[y-1][x]

  if y < gridSize - 1:
    count = count + board[y+1][x]  
    
  if x < gridSize - 1:
    count = count + board[y][x+1]
    
  if x < gridSize - 1 and y > 0:
    count = count + board[y-1][x+1]

  if x < gridSize - 1 and y < gridSize - 1:
    count = count + board[y+1][x+1]
    
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


pattern = [
  [1,1,1,0,0,0,0,0,0,1],
  [0,1,0,0,0,0,0,1,1,1],
  [0,1,0,0,0,0,0,1,0,1],
  [1,0,1,0,0,0,0,0,0,0],
  [1,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,1,0],
  [0,0,0,0,0,0,0,0,0,0],
]


initBoard()
placePattern(pattern, 0, 0)

running = True
prevTime = datetime.now()
input("ttt")
while running:
  time = datetime.now()
  screen.fill(black)
  
  if (time - prevTime).total_seconds() > updateTime:
    processBoard()

    prevTime = time

  if drawGridLines:
    drawGrid()

  drawCells()
  pygame.display.flip()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()


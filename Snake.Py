import pygame as pg
import random

class Box():
    rows = 50
    width = 250
    def __init__(self,color =(255,0,0), _x = 0, _y = 0):
        self.x = _x                  # position of x and y
        self.y = _y
        self.color = color            # Red

    def drawBox(self, wind):
        dist = self.width // self.rows
        pg.draw.rect(wind,self.color,(self.x,self.y,dist,dist))

    def apple(self):
        self.x = random.randint(1,40) * 6
        self.y = random.randint(1,40) * 6

class Snake():
    def __init__(self, currentX = 0, currentY = 0):
        self.y = currentX                                # current x
        self.x = currentY                                # current y
        self.snake = []
        self.color = (255,0,0)
        self.snake.insert(0,Box(self.color,self.x,self.y))
        self.DX = 0                                      # Direction of Snake at first instance
        self.DY = 0                                      # move right at first instance


    def updateDir(self,keys,scor):
        if keys[pg.K_DOWN]:                         # if down, change direction to down
            if self.DX == 0 and self.DY == -1 and scor > 1:
                return
            self.DX = 0
            self.DY = 1
        elif keys[pg.K_LEFT]:                       # if left, change direction to left
            if self.DX == 1 and self.DY == 0 and scor > 1:
                return
            self.DX = -1
            self.DY = 0
        elif keys[pg.K_UP]:                         # if up, change direction to up
            if self.DX == 0 and self.DY == 1 and scor > 1:
                return
            self.DX = 0
            self.DY = -1
        elif keys[pg.K_RIGHT]:                      # if right, change direction to right
            if self.DX == -1 and self.DY == 0 and scor > 1:
                return
            self.DX = 1
            self.DY = 0


    def updatePos(self):
        self.x = self.x + (self.DX * 6)          # update x
        self.y = self.y + (self.DY * 6)          # update y


    def newHead(self):
        new = Box(self.color,self.x, self.y)
        self.snake.insert(0, new)            # insert new head at snake[0]


    def deleteTail(self):
        self.snake.pop()                   # delete last in snake[]


    def printSnake(self,window):            # print out the whole snake
        for i in self.snake:                # for every box in vector print it out
            i.drawBox(window)

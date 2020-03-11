
import pygame as pg
import Snake as sn
import random as rn


def  refillAndUpdate(s,a,window):
    window.fill((0,0,0))                    # fill window black
    s.printSnake(window)                    # print out the snake
    a.drawBox(window)                       # draw apple
    pg.display.update()                     # update Display

def eat(s,apple):                           # Check if snake ate the apple
    if (s.x,s.y) == (apple.x,apple.y):      # if the snakes head is at the apple
        return True                         # return True
    return False                            # return False

def checkColisions(s):
    for i in range(len(s.snake) - 1):       # Check if snake ate its self
        s0 = (s.snake[0].x, s.snake[0].y)       # set s0 to head x y
        si = (s.snake[i+1].x, s.snake[i+1].y)   # set si to x y of bodys parts
        if s0 == si:                            # if x y of head == any body part
            return False                        # return False
    if s.x >= 251 or s.x <= -1:                 # if snake is off board on x axis
        return False                            # return false
    if s.y >= 251 or s.y <= -1:                 # if snake is off board on y axis
        return False                            # return false
    else:
        return True                             # else return True to keep game going

def main():
    width = 250         # width and height because of square game
    score = 0
    pg.init()
    sound = pg.mixer.Sound('biteSound.wav')
    window = pg.display.set_mode((width,width)) # Set window size
    pg.display.set_caption("Snake")         # Window Caption

    s = sn.Snake()
    a = sn.Box((0,255,0))                   # initiate apple
    a.apple()                               # randomize the apple
    keys = pg.key.get_pressed()             # set default key pres
    playing = True                          # bool to keep game running
    clock = pg.time.Clock()                 # controll fps
    while playing:
        pg.time.delay(100)                  # delay move by 100/1000 of a second
        clock.tick(10)                      # keeps it at 10fps
        for event in pg.event.get():
            if event.type == pg.QUIT:       # if user quits
                pg.quit()
            if event.type == pg.KEYDOWN:    # if the user presses a key
                keys = pg.key.get_pressed() # set the key

        s.updateDir(keys,score)                   # update direction
        s.updatePos()                       # update the currentX and CurrentY based on direction
        s.newHead()                         # insert the new head
        if eat(s,a) == False:               # check is snake is eating the apple
            s.deleteTail()                  # if it did not eat delete the tail
        else:
            pg.mixer.Sound.play(sound)
            score += 1
            a.apple()                       # else rerandomize the apple
        refillAndUpdate(s,a,window)         # replace and reprint game scrren
        playing = checkColisions(s)         # check for collisions
    print("Your score is: {}".format(score))
main()

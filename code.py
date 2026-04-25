import pygame
pygame.init()
import math
import random
import time

WIDTH, HEIGHT = 800, 600

win = pygame.display.set_mode((WIDTH, HEIGHT ))
pygame.display.set_caption("aim trainer")

target_increment = 400 
target_event = pygame.USEREVENT

target_padding = 30

bg_color = (0, 25, 40)

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "white"


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0 
        self.grow = True

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False


        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x , self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x , self.y), self.size *0.8)
        pygame.draw.circle(win, self.COLOR, (self.x , self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x , self.y), self.size*0.4)


    def collide(self, x,y):
       dis = math.sqrt((self.x- x)**2 +(self.y - y)**2)
       return dis <= self.size
    

def draw(win, targets):
    win.fill(bg_color)

    for target in targets:
        target.draw(win)


    pygame.display.update()



def main():
    run = True
    targets = []
    clock = pygame.time.Clock()

    target_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()


    pygame.time.set_timer(target_event, target_increment)

    while run:
        clock.tick(60)
        click = False
        mouse_pos = pygame.mouse.get_pos()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == target_event:
                x = random.randint(target_padding, WIDTH - target_padding)
                y = random.randint(target_padding, HEIGHT - target_padding)
                target = Target(x , y)
                targets.append(target)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1


        for target in targets:
            target.update()


            if target.size <= 0:
                targets.remove(target)
                misses += 1
            if click and target.collide(*mouse_pos):
                targets.remove(target)
                target_pressed += 1



        draw(win, targets)
            


    pygame.quit()



if __name__ == "__main__":
    main()


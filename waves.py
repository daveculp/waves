# Import and initialize the pygame library
import pygame
import time
import random
import math

def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n
       

def get_random_color():
    return ((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
pygame.init()

WIDTH = 800
HEIGHT = 800

# Set up the drawing window
screen = pygame.display.set_mode((WIDTH, HEIGHT))


clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
font = pygame.font.SysFont("Arial", 18)
print("Window set up!")
time.sleep(3)
r = WIDTH//2
frame=100
start_time = pygame.time.get_ticks()
max_i = 0
min_i =100
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    # Fill the background with black
    screen.fill((0,0, 0))
    i=0
    z=0
    for y in range(-r,r,3):
        for x in range(-r,r,2):
            dist=math.sqrt(x*x+y*y)
            i=(dist/40-frame)
            """if i > max_i:
                max_i=i
                print("max: ", max_i)
            if i < min_i:
                min_i=i
                print("min: ", min_i)
            #print(max_i,min_i)"""
            z=math.cos(i)
            z=math.degrees(z)
            screen.set_at((int(r+x), int(r+y-z)), (0,255,255))
   
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("coral"))
    screen.blit(fps_text, (10, 0))

    # Flip the display
    dt = clock.tick(30)
    pygame.display.flip()
    frame+=1

# Done! Time to quit.
pygame.quit()

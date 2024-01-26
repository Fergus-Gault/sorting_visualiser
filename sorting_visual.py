import pygame
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

GAP = .05

DELAY = 100

def __gen_arr():
    return [random.randint(1,100) for _ in range(10)]

def __render_bars(arr, c):
    bar_width = (SCREEN_WIDTH/len(arr)) - GAP
    max_value = max(arr)
    scaling_factor = SCREEN_HEIGHT/max_value
    screen.fill("white")
    
    for i, value in enumerate(arr):
        bar_height = int(value * scaling_factor)
        if i == c:
            pygame.draw.rect(screen, (255, 0, 0), (i * (bar_width + (bar_width *GAP)), SCREEN_HEIGHT - bar_height, bar_width, bar_height))
        else:
            pygame.draw.rect(screen, (0, 255, 0), (i * (bar_width + (bar_width *GAP)), SCREEN_HEIGHT - bar_height, bar_width, bar_height))
    
    pygame.display.flip()
    clock.tick(30)
    pygame.time.delay(DELAY)
    
def __sort_arr(arr):
    sorted = False
    while sorted == False:
        for i in range(1, len(arr)):
            key = arr[i]
            
            j = i-1
            while j >= 0 and key < arr[j] :
                    arr[j + 1] = arr[j]
                    j -= 1
            __render_bars(arr, j+1)
            arr[j + 1] = key
            
        sorted = True


def __startup(arr):
    __render_bars(arr, 0)

def __update(arr):
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                break
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                __sort_arr(arr)
        clock.tick(30)
    
    pygame.quit()
    


def main():
    pygame.init()
    
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    global clock
    clock = pygame.time.Clock()
    
    arr = __gen_arr()
    
    __startup(arr)
    __update(arr)
    

if __name__ == "__main__":
    main()

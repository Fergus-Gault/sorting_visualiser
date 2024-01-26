import pygame
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

GAP = .05

DELAY = 10


ALG = 3

def __gen_arr():
    return [random.randint(1,100) for _ in range(100)]

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
    
def __insertsort(arr):
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
        
def __mergesort(arr):
    sorted = False
    while sorted == False:
        if len(arr) > 1:
            
            mid =  len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            __mergesort(L)
            
            __mergesort(R)
            
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    __render_bars(arr, k)
                    arr[k] = L[i]
                    i += 1
                else:
                    __render_bars(arr, k)
                    arr[k] = R[j]
                    j += 1
                k += 1
            
            while i < len(L):
                __render_bars(arr, k)
                arr[k] = L[i]
                i += 1
                k += 1
            
            while j < len(R):
                __render_bars(arr, k)
                arr[k] = R[j]
                j += 1
                k += 1
        
        __render_bars(arr, len(arr)-1)
        sorted = True

def __counting_sort(arr):
    buckets = [[] for _ in range(max(arr)+ 1)]
    for i in range(len(arr)):
        buckets[arr[i]].append(arr[i])
        
    l = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            arr[l] = buckets[i][j]
            __render_bars(arr, l)
            l += 1
                       

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
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_1:
                        __mergesort(arr)
                        break
                    case pygame.K_2:
                        __counting_sort(arr)
                        break
                    case pygame.K_3:
                        __insertsort(arr)
                        break
                    case pygame.K_SPACE:
                        arr = __gen_arr()
                        __startup(arr)
                        break
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

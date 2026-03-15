# this script runs visualizations of insertion and gnome sort.
import pygame, sys
import gnome_sort as GSort
import list_generator as lg
import Insertion_sort as InSort
pygame.init()
SCR_WIDTH = 800
SCR_HEIGHT = 600
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
clock = pygame.time.Clock() 

ul = InSort.InsertionSort(lg.generate_list(100)) # this runs insertion sort visualization
# ul = InSort.InsertionSort(lg.generate_list(100)) # this runs gnome sort visualization 
max_value = max(ul.array)
rect_width = SCR_WIDTH/len(ul.array)
font = pygame.font.SysFont(None, 48)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 200, 255))
    if not ul.list_sorted: # will run the sorting logic until the list is sorted
        ul.sort_frame()
    text = font.render(f"{ul.iterations} iterations. {ul.comparisons} swaps", True, (0,0,0))
    text_rect = text.get_rect()
    text_rect.topleft = (10, 10)
    for l in range(len(ul.array)):
        rect_height = (SCR_HEIGHT-100) * ul.array[l]/max_value
        rect = pygame.Rect(rect_width*l, SCR_HEIGHT-rect_height, rect_width, rect_height)
        blue = (0, 0, 255)
        if l == ul.i or l==ul.j:
            color = blue
        else:
            color = (0, 255, 0)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen,(0, 0, 0),rect,1)
    screen.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(60)
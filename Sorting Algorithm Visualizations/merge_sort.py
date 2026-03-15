import pygame, sys
import list_generator as lg
import random
import time
def merge(lst: list, left: int, right: int, mid: int):
    n1 = mid - left + 1
    n2 = right - mid
    run = False
    if (n1 + n2 == len(lst)):
        run = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((0, 200, 255))
    
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = lst[left+i]
    for j in range(n2):
        R[j] = lst[mid+1+j]

    i = 0
    j = 0
    k = left
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lst[k] = L[i]
            i +=1
        else:
            lst[k] = R[j]
            j +=1
        k +=1
    
    while i < n1:
        lst[k] = L[i]
        i+=1
        k+=1

    while j < n2:
        lst[k] = R[j]
        j+=1
        k+=1
    for l in range(len(lst)):
        rect = pygame.Rect(1280/len(lst)*l, 720-((lst[l]/len(lst))*720), 1280/len(lst),(lst[l]/len(lst))*720)
        if l == mid:
            pygame.draw.rect(screen,(0, 0, 255),rect)
            pygame.draw.rect(screen,(0, 0, 0),rect,1)    
        pygame.draw.rect(screen,(0, 255, 0),rect)
        pygame.draw.rect(screen,(0, 0, 0),rect,1)
    pygame.display.flip()
    time.sleep(1/10) # controlling fps
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
lst = lg.generate_list(400)
def merge_sort(lst: list, left: int, right: int, screen):
    if left < right:
        mid = (left + right) // 2
    
        merge_sort(lst, left, mid,screen)
        merge_sort(lst, mid+1, right, screen)
        merge(lst,left, right, mid)


merge_sort(lst, 0, len(lst)-1, screen)
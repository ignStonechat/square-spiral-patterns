from numpy import pi
import pygame

import random

pygame.init()
DISPLAY_SIZE = (10_000, 10_000)
display = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption('Squre Spiral Patterns')

font = pygame.font.SysFont('sans', 6)

RECT_SIZE = 1
cx = (DISPLAY_SIZE[0]/2)-(RECT_SIZE/2) # Center X
cy = (DISPLAY_SIZE[1]/2)-(RECT_SIZE/2) # Center Y
x = cx
y = cy

farthest_x = x

step = 0
stepX = 0
stepNum = 1
direction = 'right'
num = 0

BINARY_PALINDROMES = open('BinaryPalindromes.txt', 'r').read().split(' ')
BINARY_PALINDROMES = [int(x) for x in BINARY_PALINDROMES]

# MAX_NUM = int(BINARY_PALINDROMES[-1])
MAX_NUM = 200_000_000

def isPrime(num):
    for i in range(2, round(num/2)):
        if num % i == 0:
            return False
    return True

def isBinaryPalindrome(num):
    if num in BINARY_PALINDROMES:
        return True
    else:
        return False

def isMod(n1, n2):
    try:
        if n1 % n2 == 0: return True
    except:
        None
    return False

def isModOfPercentOf(num, percent):
    try:
        perc = int(percent/num*100)
        m = isMod(num, perc)
        return m
    except:
        None
    return False


while True:
    print(f'{DISPLAY_SIZE[0]-farthest_x} ({MAX_NUM-num})')
    if x > farthest_x:
        farthest_x = x

    if num % 255 == 0:
        pygame.draw.rect(display, (166, 50, 168), pygame.Rect(x, y, RECT_SIZE, RECT_SIZE))
    num+=1
    # pygame.draw.rect(display, (166, 50, 168), pygame.Rect(x+RECT_SIZE, y, RECT_SIZE, RECT_SIZE))
    # text = font.render(str(num), True, (255,255,255))
    # display.blit(text, (x, y))
    if step == stepNum:
        stepX+=1
        if direction == 'right': direction = 'up'
        elif direction == 'up':    direction = 'left'
        elif direction == 'left':  direction = 'down'
        elif direction == 'down':  direction = 'right'
    elif step == stepNum*2:
        step = 0
        stepX = 0
        stepNum += 1
        if direction == 'right': direction = 'up'
        elif direction == 'up':    direction = 'left'
        elif direction == 'left':  direction = 'down'
        elif direction == 'down':  direction = 'right'
    step+=1


    if direction == 'right': x+=RECT_SIZE
    if direction == 'up': y-=RECT_SIZE
    if direction == 'left': x-=RECT_SIZE
    if direction == 'down': y+=RECT_SIZE

    if num == MAX_NUM or x > DISPLAY_SIZE[0]:
        break

pygame.display.update()
pygame.image.save(display, './spiral.png')
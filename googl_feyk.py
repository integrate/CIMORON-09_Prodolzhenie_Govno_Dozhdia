import pygame
from pygame import display,event

# def orabotka_sobity():]
def risovanie():
    y.fill([255, 60, 90])
    display.flip()
def obrabotka():

    lodka = pygame.event.get()
    for did in lodka:
        if did.type == pygame.QUIT:
            exit()

while 1 == 1:
    y = display.set_mode([500, 800])
    risovanie()

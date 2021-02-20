import pygame
from pygame import display, event
platforma=pygame.Rect(200,200,100,100)

# def orabotka_sobity():]
def risovanie():
    y.fill([255, 60, 90])
    rtyu = [200, 120, 10]
    pygame.draw.rect(y,rtyu,platforma)
    display.flip() #Показывает окно пользователю

def obrabotka():
    lodka = pygame.event.get()
    for did in lodka:
        if did.type == pygame.QUIT:

            exit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        print("a")


while 1 == 1:
    y = display.set_mode([500, 800])
    obrabotka()
    risovanie()



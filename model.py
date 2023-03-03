import pygame, random, time
from pygame import display, event

platforma = pygame.Rect(200, 200, 100, 100)
protivnik = pygame.Rect(100, 100, 100, 100)
protivnik_2 = pygame.Rect(14, 140, 100, 100)
red = [protivnik, protivnik_2]
patroni = []
patron_spedy = 10
monety = 0
hp = 5
max_patroni=3

def slezhu_za_granicami():
    if platforma.bottom > 725:
        platforma.bottom = 725

    if platforma.y < 0:
        platforma.y = 0

    if platforma.right > 750:
        platforma.right = 750

    if platforma.x < 0:
        platforma.x = 0




def sozdat_leviy_patron():
        a = pygame.Rect(300, 200, 9, 50)
        patroni.append(a)
        a.x = platforma.x
        a.y = platforma.y
        if monety>105:
            a2 = pygame.Rect(330, 200, 9, 50)
            patroni.append(a2)
            a2.x = platforma.x-10
            a2.y = platforma.y

            a.x = platforma.x+10

def sozdat_pravuy_patron():
        b = pygame.Rect(300, 200, 9, 50)
        patroni.append(b)
        b.right = platforma.right
        b.y = platforma.y

        if monety>105:
            b2 = pygame.Rect(170, 200, 9, 50)
            patroni.append(b2)
            b2.right = platforma.right+10
            b2.y = platforma.y

            b.right = platforma.right - 10


def dvizhenie_protivnika():
    global korabl_protivnika,monety
    red[0].y += 10
    red[1].y += 10

    if protivnik.y > 825:
        red[0].x = random.randint(0, 650)
        red[0].y = -150
    if protivnik_2.y > 825:
        red[1].x = random.randint(0, 650)
        red[1].y = -150
    # Чтобы корабли не встречались
    lt = protivnik.colliderect(protivnik_2)
    if lt == 1:
        protivnik.left = protivnik_2.right

    for did in patroni:

        kl = protivnik.colliderect(did)

        if kl == 1:
            patroni.remove(did)
            protivnik.y = 3000
            monety+=1
        kf = protivnik_2.colliderect(did)

        if kf == 1:
            patroni.remove(did)
            protivnik_2.y = 3000
            monety+=1


def stolknovenie_protivnikov_and_platforme():
    global hp_platforme, hp, konez, konez_zezni
    io = protivnik.colliderect(platforma)
    o = protivnik_2.colliderect(platforma)
    if io == 1:
        protivnik.y = 900
    if o == 1:
        protivnik_2.y = 900

    if o == 1 or io == 1:
        hp -= 1


def upravlaem_patronom():
    for did in patroni:
        did.y -= 6

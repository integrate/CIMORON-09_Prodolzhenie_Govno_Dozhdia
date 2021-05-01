import pygame,random,time
from pygame import display, event

y = display.set_mode([750, 825])

platforma = pygame.Rect(200, 200, 100, 100)
protivnik = pygame.Rect(100, 100, 100, 100)
zhizn=pygame.Rect(0,0, 100, 100)
protivnik_2 = pygame.Rect(14, 140, 100, 100)
red = [protivnik, protivnik_2]
patroni = []
patron_spedy = 10

hp = 5






def slezhu_za_granicami():
    if platforma.bottom > 825:
        platforma.bottom = 825

    if platforma.y < 0:
        platforma.y = 0

    if platforma.right > 750:
        platforma.right = 750

    if platforma.x < 0:
        platforma.x = 0



def dvizhenie_protivnika():
    global korabl_protivnika
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

        kf = protivnik_2.colliderect(did)

        if kf == 1:
            patroni.remove(did)
            protivnik_2.y = 3000

def stolknovenie_protivnikov_and_platforme():
    global hp_platforme, hp,konez,konez_zezni
    io = protivnik.colliderect(platforma)
    o = protivnik_2.colliderect(platforma)
    if io == 1:
        protivnik.y = 900
    if o == 1:
        protivnik_2.y = 900

    if o == 1 or io == 1:
        hp -= 1
        # hp_platforme = shrift.render(str(hp), True, [255, 2, 10])

def upravlaem_patronom():
    for did in patroni:
        did.y -= 6

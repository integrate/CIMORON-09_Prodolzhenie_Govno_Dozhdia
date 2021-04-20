import pygame, time, random

pygame.init()
import help
from pygame import display, event

y = display.set_mode([750, 825])
platforma = pygame.Rect(200, 200, 100, 100)
protivnik = pygame.Rect(100, 100, 100, 100)
protivnik_2 = pygame.Rect(14, 140, 100, 100)
patroni = []
patron_spedy = 10
big_baby_type = False
karabl = pygame.image.load("risovanie_kartinak_dli_igr/karabl_dle_egr.png")
karabl = pygame.transform.scale(karabl, [100, 100])
red = [protivnik, protivnik_2]

kartnka_nebo = pygame.image.load("risovanie_kartinak_dli_igr/nebo.jpg")
kartnka_nebo=pygame.transform.scale(kartnka_nebo,[750,825])
korabl_protivnika = pygame.image.load("risovanie_kartinak_dli_igr/korabl_protivnika.png")
korabl_protivnika = pygame.transform.flip(korabl_protivnika, False, True)

korabl_protivnika = help.izmeni_kartinku(korabl_protivnika, 100, 100, [255, 255, 255], 130)

patron = pygame.image.load("risovanie_kartinak_dli_igr/patron_platforme.jpg")
patron = help.izmeni_kartinku(patron, 9, 50, [255, 255, 255], 15)


# def orabotka_sobity():]
def risovanie():
    rtyu = [200, 120, 10]  # pygame.draw.rect(y,rtyu,platforma)
    y.blit(kartnka_nebo,[0,0])
    y.blit(karabl, platforma)
    y.blit(korabl_protivnika, red[0])
    y.blit(korabl_protivnika, red[1])
    for did in patroni:
        y.blit(patron, did)

    # pygame.draw.rect(y,rtyu,platforma,1)
    # pygame.draw.rect(y,rtyu,patron_platforma,1)

    display.flip()  # Показывает окно пользователю


def upravlaem_patronom():
    for did in patroni:
        did.y -= 6


def obrabotka():
    lodka = pygame.event.get()
    global big_baby_type
    global y
    global patron_platforma_1
    for did in lodka:
        if did.type == pygame.QUIT:
            exit()
        if did.type == pygame.MOUSEBUTTONDOWN:

            if did.button == 1:
                a = pygame.Rect(300, 200, 9, 50)
                patroni.append(a)
                a.x = platforma.x
                a.y = platforma.y

            if did.button == 3:
                b = pygame.Rect(300, 200, 9, 50)
                patroni.append(b)
                b.right = platforma.right
                b.y = platforma.y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        platforma.x -= 6
        slezhu_za_granicami()

    if keys[pygame.K_d]:
        platforma.x += 6
        slezhu_za_granicami()

    if keys[pygame.K_w]:
        platforma.y -= 6
        slezhu_za_granicami()

    if keys[pygame.K_s]:
        platforma.y += 6
        slezhu_za_granicami()


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


def slezhu_za_granicami():
    if platforma.bottom > 825:
        platforma.bottom = 825

    if platforma.y < 0:
        platforma.y = 0

    if platforma.right > 750:
        platforma.right = 750

    if platforma.x < 0:
        platforma.x = 0


while 1 == 1:
    time.sleep(1 / 60)
    upravlaem_patronom()
    obrabotka()
    dvizhenie_protivnika()
    risovanie()

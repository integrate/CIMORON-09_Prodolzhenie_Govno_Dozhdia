import pygame, time, random

pygame.init()
import help
from pygame import display, event

y = display.set_mode([750, 825])

platforma = pygame.Rect(200, 200, 100, 100)
protivnik = pygame.Rect(100, 100, 100, 100)
protivnik_2 = pygame.Rect(14, 140, 100, 100)
patron_platforma = pygame.Rect(300,200, 20, 20)
patron_spedy = 10
big_baby_type=False
karabl = pygame.image.load("risovanie_kartinak_dli_igr/karabl_dle_egr.png")
karabl = pygame.transform.scale(karabl, [100, 100])
red = [protivnik, protivnik_2]

korabl_protivnika = pygame.image.load("risovanie_kartinak_dli_igr/korabl_protivnika.png")
korabl_protivnika = pygame.transform.flip(korabl_protivnika, False, True)

korabl_protivnika = help.izmeni_kartinku(korabl_protivnika, 100, 100, [255, 255, 255], 130)

patron = pygame.image.load("risovanie_kartinak_dli_igr/patron_platforme.jpg")
patron = help.izmeni_kartinku(patron, 9, 50, [255, 255, 255], 15)


# def orabotka_sobity():]
def risovanie():

    y.fill([0, 0, 0])
    rtyu = [200, 120, 10]  # pygame.draw.rect(y,rtyu,platforma)
    # pygame.draw.rect(y,rtyu,protivnik)

    y.blit(karabl, platforma)
    y.blit(korabl_protivnika, red[0])
    y.blit(korabl_protivnika, red[1])
    if big_baby_type ==True:
        y.blit(patron, patron_platforma)

    display.flip()  # Показывает окно пользователю




def upravlaem_patronom():
    global patron_spedy
    if big_baby_type == True:
        patron_platforma.y-= 10


def obrabotka():
    lodka = pygame.event.get()
    global big_baby_type
    global y
    global patron_platforma
    for did in lodka:
        if did.type == pygame.QUIT:
            exit()
        if did.type==pygame.MOUSEBUTTONDOWN:
            big_baby_type = True
            patron_platforma.y = platforma.y
            patron_platforma.x = platforma.x



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

    if protivnik.y > 725:
        korabl_protivnika = help.izmeni_kartinku(korabl_protivnika, 100, 100, [255, 255, 255], 150)
        red[0].x = random.randint(0, 650)
        red[0].y = 0
        red[1].x = random.randint(0, 650)
        red[1].y = 0


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

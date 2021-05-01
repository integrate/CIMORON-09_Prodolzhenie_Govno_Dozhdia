import pygame, random,time,model,help
from pygame import display, event

y = display.set_mode([750, 825])

platforma = pygame.Rect(200, 200, 100, 100)
protivnik = pygame.Rect(100, 100, 100, 100)
zhizn=pygame.Rect(0,0, 100, 100)
protivnik_2 = pygame.Rect(14, 140, 100, 100)

patron = pygame.image.load("risovanie_kartinak_dli_igr/patron_platforme.jpg")
patron = help.izmeni_kartinku(patron, 9, 50, [255, 255, 255], 15)

serdze = pygame.image.load("risovanie_kartinak_dli_igr/serdze.jpg")
serdze = help.izmeni_kartinku(serdze, 100, 100, [255, 255, 255], 10)
kartnka_nebo = pygame.image.load("risovanie_kartinak_dli_igr/nebo.jpg")
kartnka_nebo = pygame.transform.scale(kartnka_nebo, [750, 825])

korabl_protivnika = pygame.image.load("risovanie_kartinak_dli_igr/korabl_protivnika.png")
korabl_protivnika = pygame.transform.flip(korabl_protivnika, False, True)

korabl_protivnika = help.izmeni_kartinku(korabl_protivnika, 100, 100, [255, 255, 255], 130)
karabl = pygame.image.load("risovanie_kartinak_dli_igr/karabl_dle_egr.png")

karabl = pygame.transform.scale(karabl, [100, 100])
shrift = pygame.font.SysFont("arial", 50)
hp_platforme = shrift.render(str(model.hp), True, [255, 2, 10])
konez = "YOU DEAD"
konez_zezni = shrift.render(konez, True, [255, 2, 10])


def risovanie():
    y.blit(kartnka_nebo, [0, 0])
    y.blit(karabl, platforma)
    y.blit(serdze, zhizn)

    y.blit(korabl_protivnika, model.red[0])
    y.blit(korabl_protivnika, model.red[1])
    for did in model.patroni:
        y.blit(patron, did)
    y.blit(hp_platforme, [100, 0])
    if model.hp < 1:
        y.blit(konez_zezni, [413, 375])
        display.flip()  # Показывает окно пользователю
        time.sleep(4)
        exit()

    # def orabotka_sobity():]

    # pygame.draw.rect(y,rtyu,platforma,1)
    # pygame.draw.rect(y,rtyu,patron_platforma,1)

    display.flip()  # Показывает окно пользователю

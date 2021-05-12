import pygame, random, time, model, help
from pygame import display, event

y = display.set_mode([750, 825])

patron = pygame.image.load("risovanie_kartinak_dli_igr/patron_platforme.jpg")
patron = help.izmeni_kartinku(patron, 9, 50, [255, 255, 255], 15)

serdze = pygame.image.load("risovanie_kartinak_dli_igr/serdze.jpg")
serdze = help.izmeni_kartinku(serdze, 50, 50, [255, 255, 255], 10)

kartnka_nebo = pygame.image.load("risovanie_kartinak_dli_igr/nebo.jpg")
kartnka_nebo = pygame.transform.scale(kartnka_nebo, [750, 825])

korabl_protivnika = pygame.image.load("risovanie_kartinak_dli_igr/korabl_protivnika.png")
korabl_protivnika = pygame.transform.flip(korabl_protivnika, False, True)
korabl_protivnika = help.izmeni_kartinku(korabl_protivnika, 100, 100, [255, 255, 255], 130)

karabl = pygame.image.load("risovanie_kartinak_dli_igr/karabl_dle_egr.png")
karabl = pygame.transform.scale(karabl, [100, 100])

br_kubok= pygame.image.load("risovanie_kartinak_dli_igr/Bronzovei_Kubok.jpg")
br_kubok = help.izmeni_kartinku(br_kubok, 50, 50, [255, 255, 255], 5)

sr_kubok = pygame.image.load("risovanie_kartinak_dli_igr/serebrennie_kubk.jpg")
sr_kubok= help.izmeni_kartinku(sr_kubok, 50, 50, [255, 255, 255], 5)

zl_kubok= pygame.image.load("risovanie_kartinak_dli_igr/zolotoe_kubok .jpg")
zl_kubok= help.izmeni_kartinku(zl_kubok, 50, 50, [255, 255, 255], 5)

coin = pygame.image.load("risovanie_kartinak_dli_igr/coin.jpg")
coin = help.izmeni_kartinku(coin, 50, 50, [255, 255, 255], 5)

shrift = pygame.font.SysFont("arial", 50)
hp_platforme = shrift.render(str(model.hp), True, [255, 2, 10])
konez = "YOU DEAD"
konez_zezni = shrift.render(konez, True, [255, 2, 10])


def risovanie():
    y.blit(kartnka_nebo, [0, 0])

    y.blit(karabl, model.platforma)

    y.blit(serdze,[0,0])

    y.blit(coin, [650, 0])

    if model.monety>25:
        y.blit(br_kubok,[700,775])

    if model.monety>50:
        y.blit(sr_kubok, [650, 775])

    if model.monety>75:
        y.blit(zl_kubok, [600, 775])

    hp_platforme = shrift.render(str(model.hp), True, [255, 2, 10])
    y.blit(hp_platforme, [100, 0])

    monety_kartinka = shrift.render(str(model.monety), True, [255, 2, 10])
    y.blit(monety_kartinka, [590, 0])

    y.blit(korabl_protivnika, model.red[0])
    y.blit(korabl_protivnika, model.red[1])

    for did in model.patroni:
        y.blit(patron, did)

    if model.hp < 1:
        y.blit(konez_zezni, [350,400])
        display.flip()  # Показывает окно пользователю
        time.sleep(4)
        exit()

    display.flip()  # Показывает окно пользователю

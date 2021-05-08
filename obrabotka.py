import pygame, time, random, model



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
                model.sozdat_leviy_patron()
            if did.button == 3:
                model.sozdat_pravuy_patron()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        model.platforma.x -= 6
        model.slezhu_za_granicami()

    if keys[pygame.K_d]:
        model.platforma.x += 6
        model.slezhu_za_granicami()

    if keys[pygame.K_w]:
        model.platforma.y -= 6
        model.slezhu_za_granicami()

    if keys[pygame.K_s]:
        model.platforma.y += 6
        model.slezhu_za_granicami()

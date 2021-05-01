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
                a = pygame.Rect(300, 200, 9, 50)
                model.patroni.append(a)
                a.x = model.platforma.x
                a.y = model.platforma.y

            if did.button == 3:
                b = pygame.Rect(300, 200, 9, 50)
                model.patroni.append(b)
                b.right = model.platforma.right
                b.y = model.platforma.y

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

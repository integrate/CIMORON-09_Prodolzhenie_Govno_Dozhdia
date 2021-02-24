import pygame, time
from pygame import display, event

platforma = pygame.Rect(200, 200, 100, 100)


# def orabotka_sobity():]
def risovanie():
    y.fill([0, 0, 0])
    rtyu = [200, 120, 10]
    # pygame.draw.rect(y,rtyu,platforma)
    platforma = pygame.image.load("kartinki/karabl_dle_egr")
    platforma = pygame.transform.scale(platforma, [100, 100])


display.flip()  # Показывает окно пользователю


def obrabotka():
    lodka = pygame.event.get()
    for did in lodka:
        if did.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        platforma.x -= 10

    if keys[pygame.K_d]:
        platforma.x += 10

    if keys[pygame.K_w]:
        platforma.y -= 10

    if keys[pygame.K_s]:
        platforma.y += 10

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
    y = display.set_mode([750, 825])
    obrabotka()
    risovanie()

import pygame, time, random,model,risovanie,obrabotka
pygame.init()
big_baby_type = False
while 1 == 1:
    time.sleep(1 / 60)
    model.upravlaem_patronom()
    obrabotka.obrabotka()
    model.dvizhenie_protivnika()
    model.stolknovenie_protivnikov_and_platforme()
    risovanie.risovanie()

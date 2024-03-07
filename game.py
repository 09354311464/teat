import pygame
pygame.init()
screen=pygame.display.set_mode((800,400))#tuple
clock=pygame.time.Clock()
while True:#event loop -game loop-frame
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#constant-sadet
            pygame.quit()#-->delete from RAM
            exit()
    pygame.display.update()
    clock.tick(60)
    print(clock.get_fps())
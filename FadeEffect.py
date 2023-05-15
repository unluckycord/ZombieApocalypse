import time,Assets,pygame
def paintFade():
    currentTickCycleColor = pygame.time.get_ticks()
    nowCycleColor = 0
    duration = 0
    x = 255
    z = 0
    while x > 0: 
        print(z,x)
        nowCycleColor = pygame.time.get_ticks()
        fadeOut = x,0,0
        if nowCycleColor - currentTickCycleColor > 50:
            currentTickCycleColor = nowCycleColor
            x -= 3
        Assets.WIN.fill(fadeOut)
        pygame.display.update()
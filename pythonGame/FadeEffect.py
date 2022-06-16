import time,Assets,pygame

def paintFade():
    x = 255
    for i in range(85):    
        fadeOut = x,x,x
        x -= 3
        time.sleep(0.05)
        Assets.WIN.fill(fadeOut)
        pygame.display.update()
    z = 0 
    for i in range(85):
        fadeIn = z,z,z
        z += 3
        time.sleep(0.05)
        Assets.WIN.fill(fadeIn)
        pygame.display.update()
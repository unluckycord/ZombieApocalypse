import pygame,time,Assets,Game,FadeEffect,Main

def paintMenu():

    START_TEXT = Assets.START_FONT.render(" Click here to start",1,Assets.WHITE)
    Assets.WIN.fill(Assets.WHITE)
    Assets.WIN.blit(Assets.mainMenuBackground,(0,0))
    Assets.WIN.blit(Assets.blackBackground,((Assets.WIDTH//2- 135),((Assets.HEIGHT//2)-20)))
    Assets.WIN.blit(START_TEXT,((Assets.WIDTH//2- 115),(Assets.HEIGHT//2)))
    pygame.display.update()

def mainMenuUI():
    Assets.BACKGROUNDMAP1.stop()
    Assets.MAINMENUTHEME.play()
    clock = pygame.time.Clock()
    run = True
    while run:
        mousex,mousey = pygame.mouse.get_pos()
        clock.tick(Assets.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run == False
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if Assets.WIDTH//2 - 135 <= mousex <= 750 and Assets.HEIGHT//2-20<= mousey <= 450:
                    Assets.MENUCONFIRM.play()
                    Assets.MAINMENUTHEME.stop()
                    #Assets.FADESFX.play()
                    #FadeEffect.paintFade()
                    Game.start()
                else:
                    if Assets.WIDTH-70 <= mousex <= Assets.WIDTH - 20 and 20 <= mousey <= 70:
                        Main.musicIsOn = True
                        Assets.MAINMENUTHEME.play()
        paintMenu()
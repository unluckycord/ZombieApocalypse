import pygame,Assets,StartScreen,FadeEffect,Main

def endGameScreen(alive):
    run = True

    Assets.BACKGROUNDMAP1.stop()

    if alive:
        Assets.GAMEWON.play()
        
    else:
        Assets.GAMELOST.play()

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run == False

                pygame.quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    Assets.MENUCONFIRM.play()

                    Assets.FADESFX.play()

                    FadeEffect.paintFade()

                    StartScreen.startUI()

        if alive:
            Assets.WIN.fill(Assets.WHITE)
            FontColor = Assets.BLACK
            text = Assets.START_FONT.render(("YOU WON"),1,FontColor)
        else:
            FontColor = Assets.RED
            Assets.WIN.fill(Assets.BLACK)
            text = Assets.START_FONT.render(("YOU DIED"),1,FontColor)

        Assets.WIN.blit(text,((Assets.WIDTH//2-80),(Assets.HEIGHT//2)))

        goToMenu = Assets.START_FONT_SMALL.render(("PRESS ENTER TO GO TO MAIN MENU"),1,FontColor)

        Assets.WIN.blit(goToMenu,((Assets.WIDTH//2 - 135),(Assets.HEIGHT-(Assets.HEIGHT//4))))

        pygame.display.update()

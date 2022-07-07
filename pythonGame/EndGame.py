import pygame,Assets,StartScreen,FadeEffect,Main

def deathScreen():
    run = True
    Assets.BACKGROUNDMAP1.stop()
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
        Assets.WIN.fill(Assets.BLACK)
        dead = Assets.START_FONT.render(("YOU DIED"),1,Assets.RED)
        Assets.WIN.blit(dead,((Assets.WIDTH//2-60),(Assets.HEIGHT//2)))
        tryAgain = Assets.START_FONT_SMALL.render(("PRESS ENTER TO GO TO MAIN MENU"),1,Assets.RED)
        Assets.WIN.blit(tryAgain,((Assets.WIDTH//2 - 115),(Assets.HEIGHT-(Assets.HEIGHT//4))))

        pygame.display.update()
def WinnerScreen():
    run = True
    Assets.BACKGROUNDMAP1.stop()
    Assets.GAMEWON.play()
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
        Assets.WIN.fill(Assets.WHITE)
        dead = Assets.START_FONT.render(("YOU WON"),1,Assets.BLACK)
        Assets.WIN.blit(dead,((Assets.WIDTH//2-60),(Assets.HEIGHT//2)))
        tryAgain = Assets.START_FONT_SMALL.render(("PRESS ENTER TO GO TO MAIN MENU"),1,Assets.BLACK)
        Assets.WIN.blit(tryAgain,((Assets.WIDTH//2 - 115),(Assets.HEIGHT-(Assets.HEIGHT//4))))

        pygame.display.update()
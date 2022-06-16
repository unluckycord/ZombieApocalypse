import pygame,Assets,StartScreen,FadeEffect,Main

def paintDeath():
    Assets.WIN.fill(Assets.BLACK)
    dead = Assets.START_FONT.render(("YOU DIED"),1,Assets.RED)
    Assets.WIN.blit(dead,((Assets.WIDTH//2-60),(Assets.HEIGHT//2)))
    tryAgain = Assets.START_FONT_SMALL.render(("PRESS ENTER TO GO TO MAIN MENU"),1,Assets.RED)
    Assets.WIN.blit(tryAgain,((Assets.WIDTH//2 - 115),(Assets.HEIGHT-(Assets.HEIGHT//4))))

    pygame.display.update()

def deathScreen():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(Assets.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Assets.MENUCONFIRM.play()
                    Assets.FADESFX.play()
                    FadeEffect.paintFade()
                    StartScreen.mainMenuUI()
        paintDeath()
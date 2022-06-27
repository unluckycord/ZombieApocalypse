import pygame,time,Assets,Game,FadeEffect,Main
def startUI():
    Assets.BACKGROUNDMAP1.stop()
    Assets.MAINMENUTHEME.play()
    clock = pygame.time.Clock()
    run = True
    renderStart = True
    renderMenu = False
    renderGunShop = False
    renderLevelSelection = False
    renderBackButton = False
    while run:
        mousex,mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run == False
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(startButton, mouseRect) and renderStart:
                    Assets.MENUCONFIRM.play()
                    renderStart = False
                    renderMenu = True
        
        if renderBackButton:
            pass            
        
        Assets.WIN.fill(Assets.WHITE)
        Assets.WIN.blit(Assets.mainMenuBackground,(0,0))
        mouseRect = pygame.draw.rect(Assets.WIN, Assets.WHITE, (mousex-10, mousey-10, 20, 20))
        if renderStart:               
            TITLE = Assets.START_FONT.render("ZOMBIE APOCALYPSE", 1, Assets.BLACK)
            Assets.WIN.blit(TITLE, ((Assets.WIDTH//2 - 150), 50))
            
            START_TEXT = Assets.START_FONT.render("CLICK HERE TO START",1,Assets.WHITE)
            startButton = pygame.draw.rect(Assets.WIN, Assets.BLACK, ((Assets.WIDTH//2 - 170),(Assets.HEIGHT - 200), 340, 70))
            Assets.WIN.blit(START_TEXT,((Assets.WIDTH//2- 160),(Assets.HEIGHT - 180)))
            
        if renderMenu:
            #RENDERS GUN SHOP BUTTON
            heightOffset = 80
            gunShopButton = pygame.draw.rect(Assets.WIN, Assets.GREY, (40,heightOffset, 540, 430 + heightOffset//2))
            GUNSHOPTEXT = Assets.START_FONT.render("GUN SHOP",1,Assets.WHITE)
            pygame.draw.rect(Assets.WIN,Assets.BLACK, (60,370 + heightOffset, 500, 60))
            Assets.WIN.blit(GUNSHOPTEXT, (90, 390 + heightOffset))
            Assets.WIN.blit(Assets.gunShopBackground, (60, 20 + heightOffset))
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(gunShopButton, mouseRect) and renderMenu:
                Assets.GUNSHOPSOUND.play()
                renderGunShop = True
                renderMenu = False
            
            #RENDERS LEVEL SELECTION
            levelSelectionButton = pygame.draw.rect(Assets.WIN, Assets.GREY, (Assets.WIDTH-580,heightOffset, 540, 430 + heightOffset//2))
            LEVELTEXT = Assets.START_FONT.render("MISSIONS",1,Assets.WHITE)
            pygame.draw.rect(Assets.WIN,Assets.BLACK, (Assets.WIDTH-560,370 + heightOffset, 500, 60))
            Assets.WIN.blit(LEVELTEXT, (Assets.WIDTH-530, 390 + heightOffset))
            Assets.WIN.blit(Assets.levelSelectionBackground, (Assets.WIDTH - 560, 20 + heightOffset))
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(levelSelectionButton, mouseRect) and renderMenu:
                Assets.CONFIM.play()
                renderLevelSelection = True
                renderMenu = False
            
        if renderGunShop:
            backButton = pygame.draw.rect(Assets.WIN, Assets.BLACK, (20,20,50,50))
            Assets.WIN.blit(Assets.backArrow, (20, 20))
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(backButton, mouseRect) and renderGunShop:
                Assets.DECLINE.play()
                renderMenu = True
                renderGunShop = False
            
        if renderLevelSelection:
            backButton = pygame.draw.rect(Assets.WIN, Assets.BLACK, (20,20,50,50))
            Assets.WIN.blit(Assets.backArrow, (20, 20))
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(backButton, mouseRect) and renderLevelSelection:
                Assets.DECLINE.play()
                renderMenu = True
                renderLevelSelection = False
            #Assets.FADESFX.play()
            #Assets.MAINMENUTHEME.stop()
            #FadeEffect.paintFade()
            #Game.start()
        
            
        
        pygame.display.update()
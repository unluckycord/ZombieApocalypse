import pygame,time,Assets,Game,FadeEffect,Main
def startUI():
    Assets.BACKGROUNDMAP1.stop()
    Assets.MAINMENUTHEME.play()
    songLength = 200 * 1000
    clock = pygame.time.Clock()
    run = True
    renderStart = True
    renderMenu = False
    renderGunShop = False
    renderMissionType = False
    renderLevelSelection = False
    renderLevelSelectionCampaign = False
    renderBackButton = False
    currentTickClick, currentTickMusic = pygame.time.get_ticks(), pygame.time.get_ticks()
    nowClick, nowMusic = 0,0
    MINTIMEFORCLICK = 500
    while run:
        nowMusic, nowClick = pygame.time.get_ticks(), pygame.time.get_ticks()
        if nowMusic - currentTickMusic > songLength:
            currentTickMusic = nowMusic
            Assets.MAINMENUTHEME.play()
            
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
        
        backButton = pygame.draw.rect(Assets.WIN, Assets.BLACK, (40,20,50,50))
        
        Assets.WIN.fill(Assets.WHITE)
        mouseRect = pygame.draw.rect(Assets.WIN, Assets.WHITE, (mousex-10, mousey-10, 20, 20))
        Assets.WIN.blit(Assets.mainMenuBackground,(0,0))
        
        
        if renderStart:      
            renderBackButton = False         
            Assets.WIN.blit(Assets.START_FONT.render("ZOMBIE APOCALYPSE", 1, Assets.BLACK), ((Assets.WIDTH//2 - 150), 50))
        
            startButton = pygame.draw.rect(Assets.WIN, Assets.BLACK, ((Assets.WIDTH//2 - 170),(Assets.HEIGHT - 200), 340, 70))
            Assets.WIN.blit(Assets.START_FONT.render("CLICK HERE TO START",1,Assets.WHITE),((Assets.WIDTH//2- 160),(Assets.HEIGHT - 180)))
            
        if renderMenu:
            heightOffset = 80
            widthOffset = 40
            #RENDERS BACK BUTTON
            renderBackButton = True
            Assets.WIN.blit(Assets.backArrow, (widthOffset, heightOffset//4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(backButton, mouseRect) and renderMenu:
                currentTickClick = nowClick
                Assets.DECLINE.play()
                renderStart = True
                renderMenu = False
            
            #RENDERS GUN SHOP BUTTON
            gunShopButton = pygame.draw.rect(Assets.WIN, Assets.GREY, (widthOffset, heightOffset, 540, 430 + heightOffset//2))
            pygame.draw.rect(Assets.WIN,Assets.BLACK, (widthOffset + widthOffset//2,370 + heightOffset, 500, 60))
            Assets.WIN.blit(Assets.START_FONT.render("GUN SHOP",1,Assets.WHITE), (widthOffset + widthOffset//2, 390 + heightOffset))
            Assets.WIN.blit(Assets.gunShopBackground, (60, 20 + heightOffset))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(gunShopButton, mouseRect) and renderMenu:
                currentTickClick = nowClick
                Assets.GUNSHOPSOUND.play()
                renderGunShop = True
                renderMenu = False
            
            #RENDERS LEVELTYPE SELECTION
            levelSelectionButton = pygame.draw.rect(Assets.WIN, Assets.GREY, (Assets.WIDTH-580,heightOffset, 540, 430 + heightOffset//2))
            pygame.draw.rect(Assets.WIN,Assets.BLACK, (Assets.WIDTH-560,370 + heightOffset, 500, 60))
            Assets.WIN.blit(Assets.START_FONT.render("MISSIONS",1,Assets.WHITE), (Assets.WIDTH-560, 390 + heightOffset))
            Assets.WIN.blit(Assets.levelSelectionBackground, (Assets.WIDTH - 560, 20 + heightOffset))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(levelSelectionButton, mouseRect) and renderMenu:
                currentTickClick = nowClick
                Assets.CONFIM.play()
                renderMissionType = True
                renderMenu = False
            
        if renderGunShop:
            #BACK BUTTON
            Assets.WIN.blit(Assets.backArrow, (widthOffset, heightOffset//4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(backButton, mouseRect) and renderGunShop:
                currentTickClick = nowClick
                Assets.DECLINE.play()
                renderMenu = True
                renderGunShop = False
            
            
        if renderMissionType:
            #BACK BUTTON
            Assets.WIN.blit(Assets.backArrow, (widthOffset, heightOffset//4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(backButton, mouseRect) and renderMissionType:
                currentTickClick = nowClick
                Assets.DECLINE.play()
                renderMenu = True
                renderMissionType = False
                
            #LEVEL TYPES
            EndlessLevel = pygame.draw.rect(Assets.WIN, Assets.BLACK, (widthOffset, heightOffset, Assets.WIDTH//3 - 60 , Assets.HEIGHT - heightOffset - heightOffset//2))
            Assets.WIN.blit(Assets.EndlessMode, (widthOffset, heightOffset))
            Assets.WIN.blit(Assets.START_FONT.render("ENDLESS",1,Assets.RED), (widthOffset, Assets.HEIGHT - heightOffset + 4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(EndlessLevel, mouseRect) and renderMissionType:
                currentTickClick = nowClick
                Assets.CONFIM.play()
                renderLevelSelection = True
                renderMissionType = False                
            
            Campaign = pygame.draw.rect(Assets.WIN, Assets.BLACK, (widthOffset + (Assets.WIDTH//3 - 60) + widthOffset, heightOffset, Assets.WIDTH//3 - 60, Assets.HEIGHT - heightOffset - heightOffset//2))
            Assets.WIN.blit(Assets.CampaignMode, (widthOffset + (Assets.WIDTH//3 - 60) + widthOffset, heightOffset))
            Assets.WIN.blit(Assets.START_FONT.render("CAMPAIGN",1,Assets.RED), (widthOffset + (Assets.WIDTH//3 - 60) + widthOffset, Assets.HEIGHT - heightOffset + 4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(Campaign, mouseRect) and renderMissionType:
                currentTickClick = nowClick
                Assets.CONFIM.play()
                renderLevelSelectionCampaign = True
                renderMissionType = False
            
            SpecialTasks = pygame.draw.rect(Assets.WIN, Assets.BLACK, (widthOffset + ((Assets.WIDTH//3 - 60) + widthOffset)*2, heightOffset, Assets.WIDTH//3 - 60, Assets.HEIGHT - heightOffset - heightOffset//2))
            Assets.WIN.blit(Assets.placeHolder, (widthOffset + ((Assets.WIDTH//3 - 60) + widthOffset)*2, heightOffset))
        
        if renderLevelSelection:
            #BACK BUTTON
            Assets.WIN.blit(Assets.backArrow, (widthOffset, heightOffset//4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(backButton, mouseRect) and renderLevelSelection:
                currentTickClick = nowClick
                Assets.DECLINE.play()
                renderMissionType = True
                renderLevelSelection = False
            
            maxRoundCount = 100000000
            
            level1start = pygame.draw.rect(Assets.WIN, Assets.GREY, (widthOffset, heightOffset, 340, 300))
            pygame.draw.rect(Assets.WIN, Assets.BLACK,(widthOffset + widthOffset//2, heightOffset * 4, 300, 40))
            Assets.WIN.blit(Assets.START_FONT.render("FARM",1,Assets.WHITE), (70, 330))
            Assets.WIN.blit(Assets.level1, (widthOffset + widthOffset//2, heightOffset + heightOffset//4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(level1start, mouseRect) and renderLevelSelection:
                Assets.FADESFX.play()
                Assets.MAINMENUTHEME.stop()
                FadeEffect.paintFade()
                Game.start()
        
        if renderLevelSelectionCampaign:
            #BACK BUTTON
            Assets.WIN.blit(Assets.backArrow, (widthOffset, heightOffset//4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(backButton, mouseRect) and renderLevelSelectionCampaign:
                currentTickClick = nowClick
                Assets.DECLINE.play()
                renderMissionType = True
                renderLevelSelectionCampaign = False
                
            maxRoundCount = 1
            
            level1start = pygame.draw.rect(Assets.WIN, Assets.GREY, (widthOffset, heightOffset, 340, 300))
            pygame.draw.rect(Assets.WIN, Assets.BLACK,(widthOffset + widthOffset//2, heightOffset * 4, 300, 40))
            Assets.WIN.blit(Assets.START_FONT.render("FARM",1,Assets.WHITE), (70, 330))
            Assets.WIN.blit(Assets.level1, (widthOffset + widthOffset//2, heightOffset + heightOffset//4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(level1start, mouseRect) and renderLevelSelectionCampaign:
                Assets.FADESFX.play()
                Assets.MAINMENUTHEME.stop()
                FadeEffect.paintFade()
                Game.start(maxRoundCount)
            
        
        pygame.display.update()
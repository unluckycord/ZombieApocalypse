import pygame,time,Assets,Game,FadeEffect,Main
def startUI():
    Assets.BACKGROUNDMAP1.stop()
    Assets.MAINMENUTHEME.play()
    songLength = 200 * 1000
    clock = pygame.time.Clock()
    run = True
    renderStart = True
    renderSettings = False
    renderMenu = False
    renderShop = False
    renderMissionType = False
    renderLevelSelection = False
    renderLevelSelectionCampaign = False
    renderBackButton = False
    currentTickClick, currentTickMusic = pygame.time.get_ticks(), pygame.time.get_ticks()
    nowClick, nowMusic = 0,0
    MINTIMEFORCLICK = 500
    heightOffset = 80
    widthOffset = 40
    
    initialLocationForVolumeSlider = Assets.WIDTH - Assets.WIDTH//5 - 40
    
    textColor = Assets.WHITE
    
    while run:
        #print(Main.vol)
        mousex,mousey = pygame.mouse.get_pos()
        nowMusic, nowClick, nowColorCycle = pygame.time.get_ticks(), pygame.time.get_ticks(), pygame.time.get_ticks()
        
        #Mouse Collision Box
        mouseRect = pygame.draw.rect(Assets.WIN, Assets.WHITE, (mousex-10, mousey-10, 20, 20))
    
        #BackGround
        Assets.WIN.fill(Assets.BLACK)
        #Assets.WIN.blit(Assets.mainMenuBackground,(0,0))
        
        #Constant back button
        backButton = pygame.draw.rect(Assets.WIN, Assets.BLACK, (40,20,50,50))
        
        
        if nowMusic - currentTickMusic > songLength:
            currentTickMusic = nowMusic
            Assets.MAINMENUTHEME.play()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run == False
                    pygame.quit()
        
        if renderStart:      
            renderBackButton = False         
            Assets.WIN.blit(Assets.START_FONT.render("ZOMBIE APOCALYPSE", 1 ,textColor), ((Assets.WIDTH//2 - 150), 50))
        
            startButton = pygame.draw.rect(Assets.WIN, textColor, ((Assets.WIDTH//2 - 170),(Assets.HEIGHT - 300), 340, 70))
            Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render("START",1,Assets.BLACK),((Assets.WIDTH//2- 170),(Assets.HEIGHT - 280)))
            
            settingsButton = pygame.draw.rect(Assets.WIN, textColor, ((Assets.WIDTH//2 - 170),(Assets.HEIGHT - 200), 340, 70))
            Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render("SETTINGS",1,Assets.BLACK),((Assets.WIDTH//2- 170),(Assets.HEIGHT - 180)))
            
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(startButton, mouseRect) and renderStart:
                currentTickClick = nowClick
                Assets.MENUCONFIRM.play()
                renderMenu = True
                renderStart = False
                
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(settingsButton, mouseRect) and renderStart:
                currentTickClick = nowClick
                Assets.MENUCONFIRM.play()
                renderSettings = True
                renderStart = False
        
        if renderSettings:
            
            Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render("VOLUME", True, textColor), (Assets.WIDTH//5, Assets.HEIGHT//6))
            volumeSliderRail = pygame.draw.rect(Assets.WIN, textColor, (Assets.WIDTH//5, Assets.HEIGHT//4, Assets.WIDTH - 2*(Assets.WIDTH//5),20))
            volumeSlider = pygame.draw.rect(Assets.WIN, Assets.RED, (initialLocationForVolumeSlider, Assets.HEIGHT//4 - 10, 40,40))
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(mouseRect, volumeSliderRail):
                initialLocationForVolumeSlider = mouseRect.x
            
            Assets.WIN.blit(Assets.backArrow, (widthOffset, heightOffset//4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(backButton, mouseRect) and renderSettings:
                currentTickClick = nowClick
                Assets.DECLINE.play()
                renderStart = True
                renderSettings = False
            
            
        if renderMenu:
            Assets.WIN.blit(Assets.backArrow, (widthOffset, heightOffset//4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(backButton, mouseRect) and renderMenu:
                currentTickClick = nowClick
                Assets.DECLINE.play()
                renderStart = True
                renderMenu = False
            
            #RENDERS GUN SHOP BUTTON
            shopButton = pygame.draw.rect(Assets.WIN, Assets.GREY, (widthOffset, heightOffset, 540, 430 + heightOffset//2))
            pygame.draw.rect(Assets.WIN,Assets.BLACK, (widthOffset + widthOffset//2,370 + heightOffset, 500, 60))
            Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render("SHOP",1,textColor), (widthOffset + widthOffset//2, 390 + heightOffset))
            Assets.WIN.blit(Assets.gunShopBackground, (60, 20 + heightOffset))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(shopButton, mouseRect) and renderMenu:
                currentTickClick = nowClick
                Assets.GUNSHOPSOUND.play()
                renderShop = True
                renderMenu = False
            
            #RENDERS LEVELTYPE SELECTION
            levelSelectionButton = pygame.draw.rect(Assets.WIN, Assets.GREY, (Assets.WIDTH-580,heightOffset, 540, 430 + heightOffset//2))
            pygame.draw.rect(Assets.WIN,Assets.BLACK, (Assets.WIDTH-560,370 + heightOffset, 500, 60))
            Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render("MISSIONS",1,textColor), (Assets.WIDTH-560, 390 + heightOffset))
            Assets.WIN.blit(Assets.levelSelectionBackground, (Assets.WIDTH - 560, 20 + heightOffset))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(levelSelectionButton, mouseRect) and renderMenu:
                currentTickClick = nowClick
                Assets.CONFIM.play()
                renderMissionType = True
                renderMenu = False
            
        if renderShop:
            #BACK BUTTON
            Assets.WIN.blit(Assets.backArrow, (widthOffset, heightOffset//4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(backButton, mouseRect) and renderShop:
                currentTickClick = nowClick
                Assets.DECLINE.play()
                renderMenu = True
                renderShop = False
            
            
        if renderMissionType:
            #BACK BUTTON
            Assets.WIN.blit(Assets.backArrow, (widthOffset, heightOffset//4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(backButton, mouseRect) and renderMissionType:
                currentTickClick = nowClick
                Assets.DECLINE.play()
                renderMenu = True
                renderMissionType = False
                
            #LEVEL TYPES
            EndlessLevel = pygame.draw.rect(Assets.WIN, Assets.GREY, (widthOffset, heightOffset, Assets.WIDTH//3 - 60 , Assets.HEIGHT - heightOffset - heightOffset//2))
            Assets.WIN.blit(Assets.EndlessMode, (widthOffset, heightOffset))
            Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render("ENDLESS",1,textColor), (widthOffset, Assets.HEIGHT - heightOffset + 4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(EndlessLevel, mouseRect) and renderMissionType:
                currentTickClick = nowClick
                Assets.CONFIM.play()
                renderLevelSelection = True
                renderMissionType = False                
            
            Campaign = pygame.draw.rect(Assets.WIN, Assets.GREY, (widthOffset + (Assets.WIDTH//3 - 60) + widthOffset, heightOffset, Assets.WIDTH//3 - 60, Assets.HEIGHT - heightOffset - heightOffset//2))
            Assets.WIN.blit(Assets.CampaignMode, (widthOffset + (Assets.WIDTH//3 - 60) + widthOffset, heightOffset))
            Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render("CAMPAIGN",1,textColor), (widthOffset + (Assets.WIDTH//3 - 60) + widthOffset, Assets.HEIGHT - heightOffset + 4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(Campaign, mouseRect) and renderMissionType:
                currentTickClick = nowClick
                Assets.CONFIM.play()
                renderLevelSelectionCampaign = True
                renderMissionType = False
            
            SpecialTasks = pygame.draw.rect(Assets.WIN, Assets.GREY, (widthOffset + ((Assets.WIDTH//3 - 60) + widthOffset)*2, heightOffset, Assets.WIDTH//3 - 60, Assets.HEIGHT - heightOffset - heightOffset//2))
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
            Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render("FARM",1,textColor), (widthOffset + widthOffset//2, 330))
            Assets.WIN.blit(Assets.level1, (widthOffset + widthOffset//2, heightOffset + heightOffset//4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(level1start, mouseRect) and renderLevelSelection:
                Assets.FADESFX.play()
                Assets.MAINMENUTHEME.stop()
                FadeEffect.paintFade()
                Game.start(maxRoundCount)
        
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
            Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render("FARM",1,textColor), (widthOffset + widthOffset//2, 330))
            Assets.WIN.blit(Assets.level1, (widthOffset + widthOffset//2, heightOffset + heightOffset//4))
            if nowClick - currentTickClick > MINTIMEFORCLICK and event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.colliderect(level1start, mouseRect) and renderLevelSelectionCampaign:
                Assets.FADESFX.play()
                Assets.MAINMENUTHEME.stop()
                FadeEffect.paintFade()
                Game.start(maxRoundCount)
            
        
        pygame.display.update()
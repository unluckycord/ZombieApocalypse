import pygame,Assets,Zombie,Game,random
def drawWindow(player, zombies, objects, gameConfig, angle,zombieHurtSounds,currentTickZombieTakeDamage, nowZombieTakeDamage):
    randomSound = random.randint(0, 2)
    nowZombieTakeDamage = pygame.time.get_ticks()
    
    
    Assets.WIN.fill(Assets.BLACK)
    for i in range(len(objects)):
        Assets.WIN.blit(objects[i].getSprite(), (objects[i].getPosX(), objects[i].getPosY()))
    for zombie in zombies:
        if zombie.getZombieHealth()  < 1:
            Assets.WIN.blit(Assets.zombieSpriteCorpse, (zombie.getZombiex(), zombie.getZombiey()))
        else:
            Assets.WIN.blit(zombie.getSprite(), (zombie.getZombiex(), zombie.getZombiey()))
    Assets.WIN.blit(player.getSprite(), (player.getPlayerx(), player.getPlayery()))
    
    
    if gameConfig.getHUD():
        #draws HUD
        Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render(str(player.getPlayerGun().getCurrentAmmo()),1, Assets.RED),((20),(20)))
        if player.getPlayerGun().getCurrentAmmo() < 10:
            Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render("/" + str(player.getPlayerGun().getMaxAmmo()),1, Assets.RED),((40),(20)))
        else:
            Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render("/" + str(player.getPlayerGun().getMaxAmmo()),1, Assets.RED),((55),(20)))
        #draws health bar  
        if gameConfig.getBoarderAroundHealth():
            pygame.draw.rect(Assets.WIN, Assets.WHITE, (Assets.WIDTH - player.getMaxhealth()//2 - 50 - 3,7, player.getMaxhealth()//2 + 6,26))
        pygame.draw.rect(Assets.WIN, Assets.BLACK, (Assets.WIDTH - player.getMaxhealth()//2 - 50,10, player.getMaxhealth()//2 ,20))  
        pygame.draw.rect(Assets.WIN, Assets.RED, (Assets.WIDTH - player.getPlayerHealth()//2 - 50,10, player.getPlayerHealth()//2 ,20))
        Assets.WIN.blit(Assets.playerHealthSprite, (1120, -15))
        Assets.WIN.blit(Assets.playerStimPackSprite, (1120, 70))
        Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render(str(player.getHealablesOwned()),1,Assets.RED), (1080, 85))
        Assets.WIN.blit(Assets.playerGrenade, (1000, 70))
        Assets.WIN.blit(Assets.START_FONT_BOLD_ITALIC.render(str(player.getGrenadeCount()),1,Assets.RED), (960, 85))

def paintRoundTransition():
    pass
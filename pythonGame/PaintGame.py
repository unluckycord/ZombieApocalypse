import pygame,Assets,Zombie,Player,Game
def drawWindow(player, zombies, objects, gun, gameConfig, bullets):
    playerHitBox = pygame.draw.rect(Assets.WIN, Assets.BLACK, (player.getPlayerx(), player.getPlayery(), player.getPlayerh(), player.getPlayerw()))
    for i in range(len(zombies)):
        if zombies[i].getZombieHealth() > 0:
            zombies[i].canBeHit = True
            currentZombieHitBox = pygame.draw.rect(Assets.WIN, Assets.WHITE, (zombies[i].getZombiex(), zombies[i].getZombiey(), zombies[i].getZombieh(), zombies[i].getZombiew()))
            for bullet in bullets:
                currentBullet = pygame.draw.rect(Assets.WIN, Assets.WHITE, (bullet.bulletHitbox(player)))
                Assets.WIN.blit(bullet.getSprite(),(bullet.getBulletx(), bullet.getBullety()))
                if bullet.getBulletx() > 5000 or bullet.getBullety() > 5000 or bullet.getBulletx() < -5000 or bullet.getBullety() < -5000:
                    bullets.remove(bullet)
                if pygame.Rect.colliderect(currentBullet, currentZombieHitBox) and zombies[i].getCanBeHit():
                    bullets.remove(bullet)
                    #print(gun[player.getPlayerGun()].getGunDamage(player.getPlayerx(), player.getPlayery(), zombie.getZombiex(), zombie.getZombiey()))
                    zombies[i].zombieHealth -= gun[player.getPlayerGun()].getGunDamage(player.getPlayerx(), player.getPlayery(), zombies[i].getZombiex(), zombies[i].getZombiey())
                    
            if pygame.Rect.colliderect(currentZombieHitBox , playerHitBox) and zombies[i].getZombieHealth() > 0:
                player.playerTakingDamage = True
            else:
                player.playerTakingDamage = False
    Assets.WIN.fill(Assets.BLACK)
    for i in range(len(objects)):
        Assets.WIN.blit(objects[i].getSprite(), (objects[i].getPosX(), objects[i].getPosY()))
    for zombie in zombies:
        if zombie.getZombieHealth() > 0:
            Assets.WIN.blit(zombie.getSprite(), (zombie.getZombiex(), zombie.getZombiey()))
        else:
            Assets.WIN.blit(Assets.zombieSpriteCorpse, (zombie.getZombiex(), zombie.getZombiey()))
    #Assets.WIN.blit(Assets.playerBullet, (player.getPlayerx(), player.getPlayery()))
    Assets.WIN.blit(player.getSprite(), (player.getPlayerx(), player.getPlayery()))
    if gameConfig.getHUD():
        #draws HUD
        Assets.WIN.blit(Assets.START_FONT.render(str(gun[player.getPlayerGun()].getCurrentAmmo()),1, Assets.RED),((20),(20)))
        if gun[player.getPlayerGun()].getCurrentAmmo() < 10:
            Assets.WIN.blit(Assets.START_FONT.render("/" + str(gun[player.getPlayerGun()].getMaxAmmo()),1, Assets.RED),((40),(20)))
        else:
            Assets.WIN.blit(Assets.START_FONT.render("/" + str(gun[player.getPlayerGun()].getMaxAmmo()),1, Assets.RED),((55),(20)))
        #draws health bar  
        if gameConfig.getBoarderAroundHealth():
            pygame.draw.rect(Assets.WIN, Assets.WHITE, (Assets.WIDTH - player.getMaxhealth()//2 - 50 - 3,7, player.getMaxhealth()//2 + 6,26))
        pygame.draw.rect(Assets.WIN, Assets.BLACK, (Assets.WIDTH - player.getMaxhealth()//2 - 50,10, player.getMaxhealth()//2 ,20))  
        pygame.draw.rect(Assets.WIN, Assets.RED, (Assets.WIDTH - player.getPlayerHealth()//2 - 50,10, player.getPlayerHealth()//2 ,20))
        Assets.WIN.blit(Assets.playerHealthSprite, (1120, -15))

def paintRoundTransition():
    pass
import pygame,PaintGame,Assets,Player,Zombie,random,math,Objects,Guns
def playersVariables(player, gun, zombies, objects, worldDistanceX, worldDistanceY):
    player.regenHealth()
    mouseInput = pygame.mouse.get_pressed()
    keysPressed = pygame.key.get_pressed()
    mousex, mousey = pygame.mouse.get_pos()
    angle = math.degrees(math.atan2(Assets.CENTERX-mousex+20,Assets.CENTERY-mousey+20))-270
    currentSprite = gun[player.getPlayerGun()].getCurrentSprite()
    player.sprite = pygame.transform.rotate(currentSprite.copy(),angle)
    player.playerMovement(keysPressed, zombies, objects, worldDistanceX, worldDistanceY, gun)

def start():
    clock = pygame.time.Clock()
    run = True
    player = Player.Player(1000, 1000, False, 0, False, Assets.playerSpriteIdelHandgun, Assets.WIDTH // 2, Assets.HEIGHT // 2, Assets.PLAYERW, Assets.PLAYERH,3, True, False)
    zombies = []
    zombieDamageToPlayerSounds = [Assets.ZOMBIEATTACK1,Assets.ZOMBIEATTACK2,Assets.ZOMBIEATTACK3,Assets.ZOMBIEATTACK4,Assets.ZOMBIEATTACK5,Assets.ZOMBIEATTACK6,Assets.ZOMBIEATTACK7,Assets.ZOMBIEATTACK8,Assets.ZOMBIEATTACK9]
    zombieHurtSounds = []
    #upper limit is 200 zombies loaded on screen
    #DO NOT EXCEED 200 ZOMBIES
    for i in range(100):
        zombies.append(Zombie.Zombie(i, 100, 100, False, 1, False, Assets.zombieSpriteIdel, random.randint(0,1200), random.randint(0,1200), Assets.PLAYERW, Assets.PLAYERH,zombieDamageToPlayerSounds,zombieHurtSounds))
    objects = []
    objects.append(Objects.Objects(1, Assets.CENTERX-1530, Assets.CENTERY - 1010, Assets.GROUND))
    gun = []
    gun.append(Guns.Guns(Assets.playerSpriteIdelHandgun, Assets.playerSpriteHandgunMuzzle, Assets.playerSpriteIdelHandgun, 0, Assets.HANDGUNSOUNDEFFECT, Assets.RELOADHANDGUN, 10, 10, 300, 1900))
    gun.append(Guns.Guns(Assets.playerSpriteIdelShotgun, Assets.playerSpriteShotgunMuzzle, Assets.playerSpriteIdelShotgun, 1, Assets.SHOTGUNSOUNDEFFECT, Assets.RELOADSHOTGUN, 8 , 8, 600, 3300))
    gun.append(Guns.Guns(Assets.playerSpriteIdelAK47, Assets.playerSpriteAK47Muzzle, Assets.playerSpriteIdelAK47, 2, Assets.AK47SOUNDEFFECT, Assets.RELOADAK47, 30, 30, 100, 2300))
    
    worldDistanceX, worldDistanceY = 0,0
    currentTick, currentTickWalking, currentTickZombieDamage = pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks()
    now, nowZombieDamage, nowWalking = 0,0,0
    while run:
        playersVariables(player,gun, zombies, objects, worldDistanceX, worldDistanceY)
        for i in range(len(zombies)):
            if zombies[i].getZombieHealth() > 0:
                angleRelToPlayer = math.degrees(math.atan2(zombies[i].getZombiex() - player.getPlayerx(),zombies[i].getZombiey() - player.getPlayery()))-270
                zombies[i].sprite = pygame.transform.rotate(Assets.zombieSpriteIdel.copy(), angleRelToPlayer)
                zombies[i].zombieMovement(player)
                zombies[i].zombieDamage(player)
        clock.tick(Assets.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                now = pygame.time.get_ticks()
                #checks if player can shoot based on trigger pull
                if now - currentTick >= gun[player.getPlayerGun()].getCooldown():
                    player.canShoot = True
                else:
                    player.canShoot = False
                #checks if player can shoot based on reloading
                if now - currentTick >= gun[player.getPlayerGun()].getCooldownReloading():
                    player.isReloading = False
                #if checks pass, player can shoot
                if player.canShoot and player.isReloading != True:
                    currentTick = now
                    if gun[player.getPlayerGun()].currentAmmo != 0:
                        gun[player.getPlayerGun()].getGunSound()
                        gun[player.getPlayerGun()].currentSprite = gun[player.getPlayerGun()].getSpriteShooting()
                        gun[player.getPlayerGun()].currentAmmo -= 1
                    if player.getPlayerGun() == 1:
                        Assets.SHOTGUNCOCK.play()
                    else:
                        Assets.EMPTYGUN.play()
            else:
                gun[player.getPlayerGun()].currentSprite = gun[player.getPlayerGun()].getIdelSprite()
        #walking sounds based on ticks
        nowWalking = pygame.time.get_ticks()
        if nowWalking - currentTickWalking >= 500 and player.getIsWalking():
            currentTickWalking = nowWalking
            Assets.WALKINGCONCRETE.play()
        elif player.isWalking == False:
            Assets.WALKINGCONCRETE.stop()
        #zombies hurting player sounds
        for i in range(len(zombies)):
            nowZombieDamage = pygame.time.get_ticks()
            if nowZombieDamage - currentTickZombieDamage >= 3000 and player.playerTakingDamage:
                currentTickZombieDamage = nowZombieDamage
                zombieDamageToPlayerSounds[random.randint(0,len(zombieDamageToPlayerSounds)-1)].play()
                
        PaintGame.drawWindow(player, zombies, objects, gun)
        
    pygame.quit()
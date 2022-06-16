from random import choice
import pygame,PaintGame,Assets,Player,Zombie,random,math,Objects,Guns,GameConfig,Bullet,Death
def playersVariables(player, gun, zombies, objects, currentTickHeal, nowHealing, angle, bullets, mousex, mousey):
    #player.regenHealth()
    mouseInput = pygame.mouse.get_pressed()
    keysPressed = pygame.key.get_pressed()
    angle = math.degrees(math.atan2(Assets.CENTERX-mousex+20,Assets.CENTERY-mousey+20))-270
    currentSprite = gun[player.getPlayerGun()].getCurrentSprite()
    player.sprite = pygame.transform.rotate(currentSprite.copy(),angle)
    player.playerMovement(keysPressed, zombies, objects, gun, currentTickHeal, nowHealing, bullets)

def roundCount(Round):
    if Round <= 10:
        return random.randint(20,40)
    elif 10 < Round <= 20:
        return random.randint(40, 60)
    else:
        return random.randint(60,100)
def randomZombiePosx(exclusion, rangeLower, rangeUpper):
    return choice([i for i in range(rangeLower, rangeUpper) if i not in exclusion])
def randomZombiePosy(exclusion, rangeLower, rangeUpper):
    return choice([i for i in range(rangeLower, rangeUpper) if i not in exclusion])
def roundTransition():
    pass

def start():
    Round = 1
    gameConfig = GameConfig.GameConfig(False, True, True, True)
    clock = pygame.time.Clock()
    run = True
    exclusion = []
    for i in range(1000):
        exclusion.append(i)
    player = Player.Player(1000, 1000, False, 0, False, Assets.playerSpriteIdelHandgun, Assets.CENTERX, Assets.CENTERY, Assets.PLAYERW, Assets.PLAYERH, 3, True, False, 0, False)
    zombies = []
    zombieDamageToPlayerSounds = [Assets.ZOMBIEATTACK1,Assets.ZOMBIEATTACK2,Assets.ZOMBIEATTACK3,Assets.ZOMBIEATTACK4,Assets.ZOMBIEATTACK5,Assets.ZOMBIEATTACK6,Assets.ZOMBIEATTACK7,Assets.ZOMBIEATTACK8,Assets.ZOMBIEATTACK9]
    zombieHurtSounds = []
    #upper limit is 200 zombies loaded on screen
    #DO NOT EXCEED 200 ZOMBIES
    maxZombieCount = roundCount(Round)
    for i in range(maxZombieCount):
        zombies.append(Zombie.Zombie(i, 100, 20, False, 15, False, Assets.zombieSpriteIdel, randomZombiePosx(exclusion, -3060, 3060), randomZombiePosy(exclusion, -2020, 2020), Assets.PLAYERW-10, Assets.PLAYERH-10,zombieDamageToPlayerSounds,zombieHurtSounds, True))
    objects = []
    objects.append(Objects.Objects(0, Assets.CENTERX-1530, Assets.CENTERY - 1010, Assets.GROUND))
    gun = []
    gun.append(Guns.Guns(Assets.playerSpriteIdelHandgun, Assets.playerSpriteHandgunMuzzle, Assets.playerSpriteIdelHandgun, 0, Assets.HANDGUNSOUNDEFFECT, Assets.RELOADHANDGUN, 10, 10, 300, 1900, 15, 5))
    gun.append(Guns.Guns(Assets.playerSpriteIdelShotgun, Assets.playerSpriteShotgunMuzzle, Assets.playerSpriteIdelShotgun, 1, Assets.SHOTGUNSOUNDEFFECT, Assets.RELOADSHOTGUN, 8 , 8, 600, 3300, 7, 40))
    gun.append(Guns.Guns(Assets.playerSpriteIdelAK47, Assets.playerSpriteAK47Muzzle, Assets.playerSpriteIdelAK47, 2, Assets.AK47SOUNDEFFECT, Assets.RELOADAK47, 30, 30, 100, 2300, 30, 20))
    bullets = []
    worldDistanceX, worldDistanceY = 0,0
    currentTickShooting, currentTickWalking, currentTickZombieDamage, currentTickHeal = pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks()
    nowShooting, nowZombieDamage, nowWalking, nowHealing = 0,0,0,0
    angle = 0
    
    
    while run:
        HealthPool = 0
        mousex, mousey = pygame.mouse.get_pos()
        playersVariables(player,gun, zombies, objects, currentTickHeal, nowHealing, angle, bullets, mousex, mousey)
        if len(zombies) < maxZombieCount:
            zombies.append(Zombie.Zombie(i, 100, 100, False, 15, False, Assets.zombieSpriteIdel, randomZombiePosx(exclusion, -3060, 3060), randomZombiePosy(exclusion, -2020, 2020), Assets.PLAYERW-10, Assets.PLAYERH-10,zombieDamageToPlayerSounds,zombieHurtSounds, True))
        for i in range(len(zombies)):
            if zombies[i].getZombieHealth() > 0:
                angleRelToPlayer = math.degrees(math.atan2(zombies[i].getZombiex() - player.getPlayerx(),zombies[i].getZombiey() - player.getPlayery()))-270
                zombies[i].sprite = pygame.transform.rotate(Assets.zombieSpriteIdel.copy(), angleRelToPlayer)
                zombies[i].zombieMovement(player)
                HealthPool += zombies[i].getZombieHealth()
        clock.tick(Assets.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                nowShooting = pygame.time.get_ticks()
                #checks if player can shoot based on trigger pull
                if nowShooting - currentTickShooting >= gun[player.getPlayerGun()].getCooldown():
                    player.canShoot = True
                else:
                    player.canShoot = False
                #checks if player can shoot based on reloading
                if nowShooting - currentTickShooting >= gun[player.getPlayerGun()].getCooldownReloading():
                    player.isReloading = False
                #if checks pass, player can shoot
                if player.canShoot and player.isReloading != True:
                    nowBullet = pygame.time.get_ticks()
                    currentTickShooting = nowShooting
                    if gun[player.getPlayerGun()].currentAmmo > 0:
                        bullets.append(Bullet.Bullet(gun[player.getPlayerGun()],player.getPlayerx() + (player.getPlayerw()//2), player.getPlayery() + (player.getPlayerh()//2), gun[player.getPlayerGun()].getVel(), mousex, mousey,True, Assets.playerBullet))
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
        nowZombieDamage = pygame.time.get_ticks()
        if nowZombieDamage - currentTickZombieDamage >= random.randint(1000,5000) and player.playerTakingDamage:
            currentTickZombieDamage = nowZombieDamage
            zombieDamageToPlayerSounds[random.randint(0,len(zombieDamageToPlayerSounds)-1)].play()
            for i in range(len(zombies)):
                zombies[i].zombieDamage(player)
        if player.getPlayerHealth() < 0:
            pass
            #Death.deathScreen()
        if HealthPool <= 0:
            
            zombies.clear()
            Round += 1
            roundCount(Round)
            player.playerHealth = player.MAXHEALTH
                
        PaintGame.drawWindow(player, zombies, objects, gun, gameConfig, bullets)
        pygame.display.update()
        
    pygame.quit()
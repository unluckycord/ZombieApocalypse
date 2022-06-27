from array import *
from random import choice
import pygame,PaintGame,Assets,Player,Zombie,random,math,Objects,Guns,GameConfig,Bullet,Death, time
def playersVariables(player, gun, zombies, objects, currentTickHeal, nowHealing, angle, bullets, mousex, mousey, grenades, grenadeVel, currentTickTossGrenade, nowTossGrenade):
    #player.regenHealth()
    mouseInput = pygame.mouse.get_pressed()
    keysPressed = pygame.key.get_pressed()
    currentSprite = gun[player.getPlayerGun()].getCurrentSprite()
    player.sprite = pygame.transform.rotate(currentSprite.copy(),angle)
    player.playerMovement(keysPressed, zombies, objects, gun, currentTickHeal, nowHealing, bullets, grenades, grenadeVel, currentTickTossGrenade, nowTossGrenade)

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
    PlayerVel = 3
    zombieVel = 1
    pistolVel = 4
    shotgunVel = 2
    akVel = 9
    grenadeVel = 3
    
    Round = 1
    prevTime = time.time()
    dt = 0
    gameConfig = GameConfig.GameConfig(False, True, True, True)
    clock = pygame.time.Clock()
    run = True
    player = Player.Player(1000, 1000, False, 0, False, Assets.playerSpriteIdelHandgun, Assets.CENTERX, Assets.CENTERY, Assets.PLAYERW, Assets.PLAYERH, PlayerVel, True, False, 2, False, 2)
    
    exclusion = []
    for i in range(500):
        exclusion.append(i)
    zombies = []
    zombieLocationsX = []
    zombieLocationsY = []
    zombieDamageToPlayerSounds = [Assets.ZOMBIEATTACK1,Assets.ZOMBIEATTACK2,Assets.ZOMBIEATTACK3,Assets.ZOMBIEATTACK4,Assets.ZOMBIEATTACK5,Assets.ZOMBIEATTACK6,Assets.ZOMBIEATTACK7,Assets.ZOMBIEATTACK8,Assets.ZOMBIEATTACK9]
    zombieHurtSounds = [Assets.ZOMBIEHURT1,Assets.ZOMBIEHURT2,Assets.ZOMBIEHURT3]
    #upper limit is 200 zombies loaded on screen
    #DO NOT EXCEED 200 ZOMBIES
    maxZombieCount = 20
    #maxZombieCount = roundCount(Round)
    for i in range(maxZombieCount):
        x = randomZombiePosx(exclusion, -3075, 3075)
        y = randomZombiePosy(exclusion, -2020, 2020)
        zombieLocationsX.append(x)
        zombieLocationsY.append(y)
        zombies.append(Zombie.Zombie(i, 100, 20, False, 15, False, Assets.zombieSpriteIdel, x, y, Assets.PLAYERW-10, Assets.PLAYERH-10,zombieDamageToPlayerSounds,zombieHurtSounds, True, zombieVel, True))
    
    objects = []
    objects.append(Objects.Objects(0, Assets.CENTERX-1530, Assets.CENTERY - 1010, Assets.GROUND))
    #objects.append(Objects.Objects(1, Assets.CENTERX, Assets.CENTERY,Assets.BUILDING))
    
    gun = []
    gun.append(Guns.Guns(Assets.playerSpriteIdelHandgun, Assets.playerSpriteHandgunMuzzle, Assets.playerSpriteIdelHandgun, 0, Assets.HANDGUNSOUNDEFFECT, Assets.RELOADHANDGUN, 10, 10, 300, 1900, pistolVel, 5))
    gun.append(Guns.Guns(Assets.playerSpriteIdelShotgun, Assets.playerSpriteShotgunMuzzle, Assets.playerSpriteIdelShotgun, 1, Assets.SHOTGUNSOUNDEFFECT, Assets.RELOADSHOTGUN, 8 , 8, 600, 3300, shotgunVel, 40))
    gun.append(Guns.Guns(Assets.playerSpriteIdelAK47, Assets.playerSpriteAK47Muzzle, Assets.playerSpriteIdelAK47, 2, Assets.AK47SOUNDEFFECT, Assets.RELOADAK47, 30, 30, 100, 2300, akVel, 20))
    bullets = []
    worldDistanceX, worldDistanceY = 0,0
    grenades = []
    
    currentTickShooting, currentTickWalking, currentTickZombieDamage, currentTickTossGrenade, currentTickHeal, currentTickZombieTakeDamage = pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks()
    nowShooting, nowZombieDamage, nowWalking, nowHealing, nowTossGrenade, nowZombieTakeDamage = 0,0,0,0,0,0
    
    angle = 0
    
    Assets.BACKGROUNDMAP1.play()
    while run:
        currentTime = time.time()
        dt = currentTime - prevTime
        prevTime = currentTime
        
        player.VEL = PlayerVel * dt * Assets.TARGETFPS
        if gun[player.getPlayerGun()].gun == 0:
            gun[player.getPlayerGun()].vel = pistolVel * dt * Assets.TARGETFPS
        if gun[player.getPlayerGun()].gun == 1:
            gun[player.getPlayerGun()].vel = shotgunVel * dt * Assets.TARGETFPS
        if gun[player.getPlayerGun()].gun == 2:
            gun[player.getPlayerGun()].vel = akVel * dt * Assets.TARGETFPS
        
        
        for i in range(len(grenades)):
            grenades[i].grenadeVel = grenadeVel * dt * Assets.TARGETFPS
        
        print(len(grenades))
        
        HealthPool = 0
        mousex, mousey = pygame.mouse.get_pos()
        angle = math.degrees(math.atan2(Assets.CENTERX-mousex+20,Assets.CENTERY-mousey+20))-270
        playersVariables(player,gun, zombies, objects, currentTickHeal, nowHealing, angle, bullets, mousex, mousey, grenades, grenadeVel, currentTickTossGrenade, nowTossGrenade)
        
        if len(zombies) < maxZombieCount:
            zombies.append(Zombie.Zombie(i, 100, 100, False, 15, False, Assets.zombieSpriteIdel, randomZombiePosx(exclusion, -3060, 3060), randomZombiePosy(exclusion, -2020, 2020), Assets.PLAYERW-10, Assets.PLAYERH-10,zombieDamageToPlayerSounds,zombieHurtSounds, True, zombieVel, True))
        for i in range(len(zombies)):
            zombieLocationsX.insert(i, round(zombies[i].getZombiex()))
            zombieLocationsY.insert(i, round(zombies[i].getZombiey()))
            zombies[i].Vel = dt * Assets.TARGETFPS * zombieVel
            if zombies[i].getZombieHealth() > 0:
                angleRelToPlayer = math.degrees(math.atan2(zombies[i].getZombiex() - player.getPlayerx(),zombies[i].getZombiey() - player.getPlayery()))-270
                zombies[i].sprite = pygame.transform.rotate(Assets.zombieSpriteIdel.copy(), angleRelToPlayer)
                zombies[i].zombieMovement(player, zombieLocationsX, zombieLocationsY, zombies)
                HealthPool += zombies[i].getZombieHealth()
                nowZombieTakeDamage = pygame.time.get_ticks()
                if zombies[i].zombieTakingDamage and nowZombieTakeDamage - currentTickZombieTakeDamage >= 2000:
                    currentTickZombieTakeDamage = nowZombieTakeDamage
                    zombieHurtSounds[random.randint(0, 2)].play()
                nowZombieDamage = pygame.time.get_ticks()
                if nowZombieDamage - currentTickZombieDamage >= random.randint(1000,10000) and zombies[i].canBeHit and abs(zombies[i].getZombiex() - player.getPlayerx()) < 100 and abs(zombies[i].getZombiey()-player.getPlayery()) < 100:
                    currentTickZombieDamage = nowZombieDamage
                    zombieDamageToPlayerSounds[random.randint(0,len(zombieDamageToPlayerSounds)-1)].play()
                    zombies[i].zombieDamage(player)
        
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
                        if(player.getPlayerGun())==1:
                            bullets.append(Bullet.Bullet(gun[player.getPlayerGun()],player.getPlayerx() + (player.getPlayerw()//2), player.getPlayery() + (player.getPlayerh()//2), gun[player.getPlayerGun()].getVel(), mousex, mousey,True, pygame.transform.rotate(Assets.playerSlug,angle)))
                        else:
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
        
        if player.getPlayerHealth() < 0:
            pass
            #Death.deathScreen()
        if HealthPool <= 0:
            
            zombies.clear()
            Round += 1
            roundCount(Round)
            player.playerHealth = player.MAXHEALTH
                
        PaintGame.drawWindow(player, zombies, objects, gun, gameConfig, bullets, angle,zombieHurtSounds, currentTickZombieTakeDamage, nowZombieTakeDamage)
        pygame.display.update()
        
    pygame.quit()
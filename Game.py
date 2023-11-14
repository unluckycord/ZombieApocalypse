from array import *
from random import choice
import pygame,PaintGame,Assets,Player,Zombie,random,math,Objects,Guns,GameConfig,Bullet,EndGame,time,roundSystem

def playersVariables(keysPressed, player, gun, zombies, objects, currentTickHeal, nowHealing, angle, bullets, mousex, mousey, grenades, grenadeVel, currentTickTossGrenade, nowTossGrenade):
    #player.regenHealth()
    currentSprite = gun[player.getPlayerGun()].getCurrentSprite()
    player.sprite = pygame.transform.rotate(currentSprite.copy(),angle)
    player.playerMovement(keysPressed, zombies, objects, gun, currentTickHeal, nowHealing, bullets, grenades, grenadeVel, currentTickTossGrenade, nowTossGrenade, mousex,mousey)


def start(maxRoundCount):
    PlayerVel = 3
    zombieVel = 1
    pistolVel = 4
    shotgunVel = 2
    akVel = 9
    grenadeVel = 3
    Round = 1
    prevTime = time.time()
    deltaTime = 0
    gameConfig = GameConfig.GameConfig(False, True, True, True)
    clock = pygame.time.Clock()
    run = True
    player = Player.Player(1000, 1000, False, 0, False, Assets.playerSpriteIdelHandgun, Assets.CENTERX, Assets.CENTERY, Assets.PLAYERW, Assets.PLAYERH, PlayerVel, True, False, 2, False, 2)
    zombieDamageToPlayerSounds = [Assets.ZOMBIEATTACK1,Assets.ZOMBIEATTACK2,Assets.ZOMBIEATTACK3,Assets.ZOMBIEATTACK4,Assets.ZOMBIEATTACK5,Assets.ZOMBIEATTACK6,Assets.ZOMBIEATTACK7,Assets.ZOMBIEATTACK8,Assets.ZOMBIEATTACK9]
    zombieHurtSounds = [Assets.ZOMBIEHURT1,Assets.ZOMBIEHURT2,Assets.ZOMBIEHURT3]
    
    Round = roundSystem.Round()
    Round.NewRound(1,maxRoundCount, zombieVel,zombieDamageToPlayerSounds,zombieHurtSounds)
    
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
    HealthPool = 0
    #game loop everything above is intialized once
    while run:
        keysPressed = pygame.key.get_pressed()
        currentTime = time.time()
        deltaTime = currentTime - prevTime
        prevTime = currentTime
        player.VEL = PlayerVel * deltaTime * Assets.TARGETFPS
        if gun[player.getPlayerGun()].gun == 0:
            gun[player.getPlayerGun()].vel = pistolVel * deltaTime * Assets.TARGETFPS
        if gun[player.getPlayerGun()].gun == 1:
            gun[player.getPlayerGun()].vel = shotgunVel * deltaTime * Assets.TARGETFPS
        if gun[player.getPlayerGun()].gun == 2:
            gun[player.getPlayerGun()].vel = akVel * deltaTime * Assets.TARGETFPS
        
        
        for i in range(len(grenades)):
            grenades[i].grenadeVel = grenadeVel * deltaTime * Assets.TARGETFPS
        
        
        mousex, mousey = pygame.mouse.get_pos()
        angle = math.degrees(math.atan2(Assets.CENTERX-mousex+20,Assets.CENTERY-mousey+20))-270
        playersVariables(keysPressed,player,gun, Round.zombies, objects ,currentTickHeal, nowHealing, angle, bullets, mousex, mousey, grenades, grenadeVel, currentTickTossGrenade, nowTossGrenade)
        
        Round.zombieCheck(player,deltaTime,zombieVel,zombieHurtSounds,zombieDamageToPlayerSounds,HealthPool,currentTickZombieDamage)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        mouseInput = pygame.mouse.get_pressed()
        if mouseInput == (1, 0, 0):
            #checks if player can shoot based on trigger pull
            nowShooting = pygame.time.get_ticks()
            print(nowShooting, currentTickShooting)
            if nowShooting - currentTickShooting >= gun[player.getPlayerGun()].getCooldown():
                player.canShoot = True
            else:
                player.canShoot = False
            #checks if player can shoot based on reloading
            if nowShooting - currentTickShooting >= gun[player.getPlayerGun()].getCooldownReloading():
                player.isReloading = False
            #if checks pass, player can shoot
            if player.canShoot and player.isReloading != True:
                currentTickShooting = nowShooting
                nowBullet = pygame.time.get_ticks()
                if gun[player.getPlayerGun()].currentAmmo > 0:
                    if(player.getPlayerGun())==1:
                        bullets.append(Bullet.Bullet(gun[player.getPlayerGun()],player.getPlayerx() + (player.getPlayerw()//2), player.getPlayery() + (player.getPlayerh()//2), gun[player.getPlayerGun()].getVel(), mousex, mousey,True, pygame.transform.rotate(Assets.playerSlug, angleRelToPlayer)))
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
            EndGame.endGameScreen(False)
        print(HealthPool)
        HealthPool = 100000
        if HealthPool <= 0:
            Round.zombies.clear()
            player.playerHealth = player.MAXHEALTH
            HealthPool = Round.NewRound(Round.roundCount+1,maxRoundCount, zombieVel,zombieDamageToPlayerSounds,zombieHurtSounds)
        #print(Round.zombieLocationsX ,Round.zombieLocationsY)
        PaintGame.drawWindow(player, Round.zombies, objects, gun, gameConfig, bullets, angle,zombieHurtSounds, currentTickZombieTakeDamage, nowZombieTakeDamage)
        pygame.display.update()
        
    pygame.quit()
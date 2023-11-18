from array import *
from random import choice, randint
import pygame,PaintGame,Assets,Player,math,Objects,Guns,GameConfig,Bullet,EndGame,time,roundSystem

def playersVariables(keysPressed, player, zombies, objects, currentTickHeal, nowHealing, angle, mousex, mousey, grenades, grenadeVel, currentTickTossGrenade, nowTossGrenade):
    #player.regenHealth()
    currentSprite = player.getPlayerGun().getCurrentSprite()
    player.sprite = pygame.transform.rotate(currentSprite.copy(),angle)
    player.playerMovement(keysPressed, zombies, objects, currentTickHeal, nowHealing, grenades, grenadeVel, currentTickTossGrenade, nowTossGrenade, mousex,mousey)


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
    Pistol = Guns.Guns(Assets.playerSpriteIdelHandgun, Assets.playerSpriteHandgunMuzzle, Assets.playerSpriteIdelHandgun, 0, Assets.HANDGUNSOUNDEFFECT, Assets.RELOADHANDGUN, 10, 10, 300, 1900, pistolVel, 5)
    AK47 = Guns.Guns(Assets.playerSpriteIdelShotgun, Assets.playerSpriteShotgunMuzzle, Assets.playerSpriteIdelShotgun, 1, Assets.SHOTGUNSOUNDEFFECT, Assets.RELOADSHOTGUN, 8 , 8, 600, 3300, shotgunVel, 40)
    Shotgun = Guns.Guns(Assets.playerSpriteIdelAK47, Assets.playerSpriteAK47Muzzle, Assets.playerSpriteIdelAK47, 2, Assets.AK47SOUNDEFFECT, Assets.RELOADAK47, 30, 30, 100, 2300, akVel, 20)
    player = Player.Player(PlayerVel, 2, 2,Pistol, AK47, Shotgun)
    zombieHurtSounds = [Assets.ZOMBIEHURT1,Assets.ZOMBIEHURT2,Assets.ZOMBIEHURT3]
    
    Round = roundSystem.Round()
    Round.NewRound(1,maxRoundCount, zombieVel)
    
    objects = []
    objects.append(Objects.Objects(0, Assets.CENTERX-1530, Assets.CENTERY - 1010, Assets.GROUND))
    #objects.append(Objects.Objects(1, Assets.CENTERX, Assets.CENTERY,Assets.BUILDING))

    
    worldDistanceX, worldDistanceY = 0,0
    grenades = []
    
    currentTickShooting, currentTickWalking, currentTickZombieDamage, currentTickTossGrenade, currentTickHeal, currentTickZombieTakeDamage = pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks()
    nowShooting, nowZombieDamage, nowWalking, nowHealing, nowTossGrenade, nowZombieTakeDamage = 0,0,0,0,0,0
    
    angle = 0
    
    Assets.BACKGROUNDMAP1.play()
    #game loop everything above is intialized once
    while run:
        keysPressed = pygame.key.get_pressed()
        currentTime = time.time()
        deltaTime = currentTime - prevTime
        prevTime = currentTime
        player.VEL = PlayerVel * deltaTime * Assets.TARGETFPS

        for i in range(len(grenades)):
            grenades[i].grenadeVel = grenadeVel * deltaTime * Assets.TARGETFPS
        
        mousex, mousey = pygame.mouse.get_pos()
        angle = math.degrees(math.atan2(Assets.CENTERX-mousex+20,Assets.CENTERY-mousey+20))-270
        playersVariables(keysPressed,player, Round.zombies, objects ,currentTickHeal, nowHealing, angle, mousex, mousey, grenades, grenadeVel, currentTickTossGrenade, nowTossGrenade)
        Round.roundCheck(player,maxRoundCount,zombieVel,deltaTime,currentTickZombieDamage)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        mouseInput = pygame.mouse.get_pressed()
        if mouseInput == (1, 0, 0):
            #checks if player can shoot based on trigger pull
            nowShooting = pygame.time.get_ticks()
            if nowShooting - currentTickShooting >= player.getPlayerGun().getCooldown():
                player.canShoot = True
            else:
                player.canShoot = False
            #checks if player can shoot based on reloading
            if nowShooting - currentTickShooting >= player.getPlayerGun().getCooldownReloading():
                player.isReloading = False
            #if checks pass, player can shoot
            if player.canShoot and player.isReloading != True:
                currentTickShooting = nowShooting
                nowBullet = pygame.time.get_ticks()
                player.getPlayerGun().createBullet(player, pistolVel, shotgunVel, deltaTime, mousex, mousey)
                
        else:
            player.getPlayerGun().currentSprite = player.getPlayerGun().getIdelSprite()
        
        #walking sounds based on ticks
        nowWalking = pygame.time.get_ticks()
        if nowWalking - currentTickWalking >= 500 and player.getIsWalking():
            currentTickWalking = nowWalking
            Assets.WALKINGCONCRETE.play()
        elif player.isWalking == False:
            Assets.WALKINGCONCRETE.stop()

        if player.getPlayerHealth() < 0:
            EndGame.endGameScreen(False)
        #FIX THIS IMMEDITLY
        PaintGame.drawWindow(player, Round.zombies, objects, gameConfig, angle,zombieHurtSounds, currentTickZombieTakeDamage, nowZombieTakeDamage)
        pygame.display.update()
        
    pygame.quit()
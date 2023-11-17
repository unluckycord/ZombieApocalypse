import math
from random import choice, randint
import random

import pygame, Assets
class Zombie:
    def __init__(self,zombieCount, Vel, x , y):
        self.zombieCount = zombieCount
        self.MAXHEALTH = 100
        self.zombieHealth = 100
        self.zombieTakingDamage = False
        self.damageAmount = 15
        self.dealingDamage = True
        self.zombieDamageToPlayerSounds = [Assets.ZOMBIEATTACK1,Assets.ZOMBIEATTACK2,Assets.ZOMBIEATTACK3,Assets.ZOMBIEATTACK4,Assets.ZOMBIEATTACK5,Assets.ZOMBIEATTACK6,Assets.ZOMBIEATTACK7,Assets.ZOMBIEATTACK8,Assets.ZOMBIEATTACK9]
        self.zombieHurtSounds = [Assets.ZOMBIEHURT1,Assets.ZOMBIEHURT2,Assets.ZOMBIEHURT3]
        self.sprite = Assets.zombieSpriteCorpse
        self.zombieX = x
        self.zombieY = y
        self.zombiew = Assets.PLAYERW-10
        self.zombieh = Assets.PLAYERH-10
        self.zombieHitBox = pygame.draw.rect(Assets.WIN, Assets.WHITE, (self.zombieX, self.zombieY, self.zombieh, self.zombiew))
        self.zombieCollsionHitbox = pygame.draw.rect(Assets.WIN, Assets.BLACK, (self.zombieX, self.zombieY, self.zombieh/2, self.zombiew/2)).clamp(self.zombieHitBox)
        self.canBeHit = True
        self.canWalk = True
        self.isAlive = True
        self.Vel = Vel
        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.postion = pygame.math.Vector2([self.zombieX, self.zombieY])
        
    def getZombieCount(self):
        return self.zombieCount
    def getMaxhealth(self):
        return self.MAXHEALTH
    def getZombieHealth(self):
        return self.zombieHealth
    def getZombieTakingDamage(self):
        return self.zombieTakingDamage
    def getDamageAmount(self):
        return self.damageAmount
    def getDealingDamage(self):
        return self.dealingDamage
    def getSprite(self):
        if self.isAlive:
            self.sprite = Assets.zombieSpriteIdel
        return self.sprite
    def getZombiex(self):
        return self.zombieX
    def getZombiey(self):
        return self.zombieY
    def getZombiew(self):
        return self.zombiew
    def getZombieh(self):
        return self.zombieh
    def getRandomZombieDamageSounds(self):
        return self.zombieDamageToPlayerSounds
    def getRandomZombieHurtSounds(self):
        return self.zombieHurtSounds
    def getCanBeHit(self):
        return self.canBeHit
    
    def randomZombiePosx(self, exclusion, rangeLower, rangeUpper):
        return choice([i for i in range(rangeLower, rangeUpper) if i not in exclusion])
    def randomZombiePosy(self, exclusion, rangeLower, rangeUpper):
        return choice([i for i in range(rangeLower, rangeUpper) if i not in exclusion])
    
    def zombieMovement(self, player):
        #tempArrX = [round(self.getZombiex())]
        #tempArrY = [round(self.getZombiey())]
        #for i in range(len(zombies)):
            #if i == self.zombieCount:
            #    break
            #else:
                #need to redo collison#
                #if zombies[i].getZombieHealth() > 0:
                #    if 0 <= abs(tempArrY[0] - zombieLocationsY[i]) < 50 and 0 <= abs(tempArrX[0] - zombieLocationsX[i]) < 50:
                #        self.canWalk = False
                #    else:
                #        self.canWalk = True
        playerVector = pygame.math.Vector2(player.getPlayerx(), player.getPlayery())
        zombieVector = pygame.math.Vector2(self.zombieX, self.zombieY)
        distance = (playerVector - zombieVector).magnitude()
        
        if distance > 0:
            self.direction = (playerVector - zombieVector).normalize()
        else:
            self.direction = pygame.math.Vector2()

        self.velocity = self.direction * self.Vel
        self.zombieX += self.velocity.x
        self.zombieY += self.velocity.y
            
    def zombieDamageToPlayer(self, player):
        if player.playerTakingDamage == True:
            player.playerHealth -= self.damageAmount

    def randomZombieAttackSound(self,player,currentTickZombieDamage):
        nowZombieDamage = pygame.time.get_ticks()
        if nowZombieDamage - currentTickZombieDamage >= random.randint(1000,10000) and self.canBeHit and abs(self.getZombiex() - player.getPlayerx()) < 100 and abs(self.getZombiey()-player.getPlayery()) < 100:
            currentTickZombieDamage = nowZombieDamage
            self.zombieDamageToPlayerSounds[randint(0,len(self.zombieDamageToPlayerSounds))]
            self.zombieDamageToPlayer(player)

    def rotateZombie(self, player):
        angleRelToPlayer = math.degrees(math.atan2(self.getZombiex() - player.getPlayerx(),self.getZombiey() - player.getPlayery()))-270
        self.sprite = pygame.transform.rotate(Assets.zombieSpriteIdel.copy(), angleRelToPlayer)

    def zombieDeathCheck(self):
        if self.getZombieHealth == 0:
            self.isAlive = False

    def zombieBrain(self,player,deltaTime,zombieVel,currentTickZombieDamage):
            self.Vel = deltaTime * Assets.TARGETFPS * zombieVel
            if self.isAlive:
                self.zombieMovement(player)
                self.rotateZombie(player)
                self.zombieMovement(player)
                self.randomZombieAttackSound(player,currentTickZombieDamage)
                self.zombieDeathCheck()
    
import math
from random import choice
import random

import pygame, Assets
class Zombie:
    def __init__(self,zombieCount, zombieTakingDamage, dealingDamage, canBeHit, Vel, canWalk, x , y):
        self.zombieCount = zombieCount
        self.MAXHEALTH = 100
        self.zombieHealth = 100
        self.zombieTakingDamage = zombieTakingDamage
        self.damageAmount = 15
        self.dealingDamage = dealingDamage
        self.zombieDamageToPlayerSounds = [Assets.ZOMBIEATTACK1,Assets.ZOMBIEATTACK2,Assets.ZOMBIEATTACK3,Assets.ZOMBIEATTACK4,Assets.ZOMBIEATTACK5,Assets.ZOMBIEATTACK6,Assets.ZOMBIEATTACK7,Assets.ZOMBIEATTACK8,Assets.ZOMBIEATTACK9]
        self.zombieHurtSounds = [Assets.ZOMBIEHURT1,Assets.ZOMBIEHURT2,Assets.ZOMBIEHURT3]
        self.sprite = Assets.zombieSpriteIdel
        self.zombieX = x
        self.zombieY = y
        self.zombiew = Assets.PLAYERW-10
        self.zombieh = Assets.PLAYERH-10
        self.canBeHit = canBeHit
        self.isAlive = True
        self.Vel = Vel
        self.canWalk = canWalk
        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.postion = pygame.math.Vector2([self.zombieLocation[0], self.zombieLocation[1]])
        
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
        return self.sprite
    def getZombiex(self):
        return self.zombieLocation[0]
    def getZombiey(self):
        return self.zombieLocation[1]
    def getZombieLocation(self):
        return self.zombieLocation
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
    
    def zombieMovement(self, player, zombieLocationsX, zombieLocationsY, zombies):
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
        if self.canWalk: 
            playerVector = pygame.math.Vector2(player.getPlayerx(), player.getPlayery())
            zombieVector = pygame.math.Vector2(self.zombiex, self.zombiey)
            distance = (playerVector - zombieVector).magnitude()
            
            if distance > 0:
                self.direction = (playerVector - zombieVector).normalize()
            else:
                self.direction = pygame.math.Vector2()

            self.velocity = self.direction * self.Vel
            self.zombiex += self.velocity.x
            self.zombiey += self.velocity.y
            
    def zombieDamageToPlayer(self, player):
        if player.playerTakingDamage == True:
            player.playerHealth -= self.damageAmount

    def randomZombieAttackSound(self, i, player):
        nowZombieDamage = pygame.time.get_ticks()
        if nowZombieDamage - currentTickZombieDamage >= random.randint(1000,10000) and self.zombies[i].canBeHit and abs(self.zombies[i].getZombiex() - player.getPlayerx()) < 100 and abs(self.zombies[i].getZombiey()-player.getPlayery()) < 100:
            currentTickZombieDamage = nowZombieDamage
            self.zombieDamageToPlayerSounds[random.randint(0,len(self.zombieDamageToPlayerSounds)-1)].play()
            self.zombies[i].zombieDamageToPlayer(player)

    def randomZombieTakingDamageSound():
        pass

    def rotateZombie(self, i, player):
        angleRelToPlayer = math.degrees(math.atan2(self.zombies[i].getZombiex() - player.getPlayerx(),self.zombies[i].getZombiey() - player.getPlayery()))-270
        self.zombies[i].sprite = pygame.transform.rotate(Assets.zombieSpriteIdel.copy(), angleRelToPlayer)

    def zombieBrain(self,player,deltaTime,zombieVel,zombieHurtSounds,zombieDamageToPlayerSounds,currentTickZombieDamage):
        for i in range(len(self.zombies)):
            self.zombies[i].Vel = deltaTime * Assets.TARGETFPS * zombieVel
            if self.zombies[i].isAlive:
                self.rotateZombie(i)
                self.zombies[i].zombieMovement(player, self.zombieLocationsX, self.zombieLocationsY, self.zombies)
                self.HealthPool = math.sum(self.zombies[i].getZombieHealth())
                self.randomZombieAttackSound(i, player)
    
from random import choice

import pygame
class Zombie:
    def __init__(self,zombieCount,MAXHEALTH, zombieHealth, zombieTakingDamage, damageAmount, dealingDamage, sprite, zombiex, zombiey, zombiew, zombieh, randomZombieDamageSounds, randomZombieHurtSounds, canBeHit, Vel, canWalk):
        self.zombieCount = zombieCount
        self.MAXHEALTH = MAXHEALTH
        self.zombieHealth = zombieHealth
        self.zombieTakingDamage = zombieTakingDamage
        self.damageAmount = damageAmount
        self.dealingDamage = dealingDamage
        self.sprite = sprite
        self.zombiex = zombiex
        self.zombiey = zombiey
        self.zombiew = zombiew
        self.zombieh = zombieh
        self.randomZombieDamageSounds = randomZombieDamageSounds
        self.randomZombieHurtSounds = randomZombieHurtSounds
        self.canBeHit = canBeHit
        self.Vel = Vel
        self.canWalk = canWalk
        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.postion = pygame.math.Vector2([self.zombiex, self.zombiey])
        
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
        return self.zombiex
    def getZombiey(self):
        return self.zombiey
    def getZombiew(self):
        return self.zombiew
    def getZombieh(self):
        return self.zombieh
    def getRandomZombieDamageSounds(self):
        return self.randomZombieDamageSounds
    def getRandomZombieHurtSounds(self):
        return self.randomZombieHurtSounds
    def getCanBeHit(self):
        return self.canBeHit    
    
    def zombieMovement(self, player, zombieLocationsX, zombieLocationsY, zombies):
        tempArrX = [round(self.getZombiex())]
        tempArrY = [round(self.getZombiey())]
        for i in range(len(zombies)):
            if i == self.zombieCount:
                break
            else:
                if zombies[i].getZombieHealth() > 0:
                    if 0 <= abs(tempArrY[0] - zombieLocationsY[i]) < 50 and 0 <= abs(tempArrX[0] - zombieLocationsX[i]) < 50:
                        self.canWalk = False
                    else:
                        self.canWalk = True
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
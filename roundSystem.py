import math
from random import choice
import random, EndGame, Assets, Zombie

import pygame


class Round():
    def __init__(self):
        self.zombies = []
        self.roundCount = 0
        self.maxZombieCount = 0
        self.exclusion = []
        self.zombieLocationsX = []
        self.zombieLocationsY = []
        
    def increaseRoundCount(self, Round, maxRoundCount):
        if Round <= maxRoundCount:
            if Round <= 10:
                return random.randint(20,40)
            elif 10 < Round <= 20:
                return random.randint(40, 60)
            else:
                return random.randint(60,100)
        else:
            EndGame.endGameScreen(True)

    def randomZombiePosx(self, exclusion, rangeLower, rangeUpper):
        return choice([i for i in range(rangeLower, rangeUpper) if i not in exclusion])
    def randomZombiePosy(self, exclusion, rangeLower, rangeUpper):
        return choice([i for i in range(rangeLower, rangeUpper) if i not in exclusion])
    def roundTransition(self):
        pass

    def NewRound(self, round,maxRoundCount, zombieVel,zombieDamageToPlayerSounds,zombieHurtSounds):
        self.roundCount = round
        for i in range(500):
            self.exclusion.append(i)
        #upper limit is 200 zombies loaded on screen
        #DO NOT EXCEED 200 ZOMBIES
        self.maxZombieCount = 20
        #self.maxZombieCount = self.increaseRoundCount(round, maxRoundCount)
        for i in range(self.maxZombieCount):
            x = self.randomZombiePosx(self.exclusion, -3075, 3075)
            y = self.randomZombiePosy(self.exclusion, -2020, 2020)
            self.zombieLocationsX.append(x)
            self.zombieLocationsY.append(y)
            self.zombies.append(Zombie.Zombie(i, 100, 20, False, 15, False, Assets.zombieSpriteIdel, x, y, Assets.PLAYERW-10, Assets.PLAYERH-10,zombieDamageToPlayerSounds,zombieHurtSounds, True, zombieVel, True))

    def zombieCheck(self,player,deltaTime,zombieVel,zombieHurtSounds,zombieDamageToPlayerSounds,HealthPool,currentTickZombieDamage):
        if len(self.zombies) < self.maxZombieCount:
            self.zombies.append(Zombie.Zombie(i, 100, 100, False, 15, False, Assets.zombieSpriteIdel, self.randomZombiePosx(self.exclusion, -3060, 3060), self.randomZombiePosy(self.exclusion, -2020, 2020), Assets.PLAYERW-10, Assets.PLAYERH-10,zombieDamageToPlayerSounds,zombieHurtSounds, True, zombieVel, True))
        for i in range(len(self.zombies)):
            self.zombieLocationsX.insert(i, round(self.zombies[i].getZombiex()))
            self.zombieLocationsY.insert(i, round(self.zombies[i].getZombiey()))
            self.zombies[i].Vel = deltaTime * Assets.TARGETFPS * zombieVel
            if self.zombies[i].getZombieHealth() > 0:
                angleRelToPlayer = math.degrees(math.atan2(self.zombies[i].getZombiex() - player.getPlayerx(),self.zombies[i].getZombiey() - player.getPlayery()))-270
                self.zombies[i].sprite = pygame.transform.rotate(Assets.zombieSpriteIdel.copy(), angleRelToPlayer)
                self.zombies[i].zombieMovement(player, self.zombieLocationsX, self.zombieLocationsY, self.zombies)
                HealthPool += self.zombies[i].getZombieHealth()
                nowZombieTakeDamage = pygame.time.get_ticks()
                if self.zombies[i].zombieTakingDamage and nowZombieTakeDamage - currentTickZombieTakeDamage >= 2000:
                    currentTickZombieTakeDamage = nowZombieTakeDamage
                    zombieHurtSounds[random.randint(0, 2)].play()
                nowZombieDamage = pygame.time.get_ticks()
                if nowZombieDamage - currentTickZombieDamage >= random.randint(1000,10000) and self.zombies[i].canBeHit and abs(self.zombies[i].getZombiex() - player.getPlayerx()) < 100 and abs(self.zombies[i].getZombiey()-player.getPlayery()) < 100:
                    currentTickZombieDamage = nowZombieDamage
                    zombieDamageToPlayerSounds[random.randint(0,len(zombieDamageToPlayerSounds)-1)].play()
                    self.zombies[i].zombieDamageToPlayer(player)
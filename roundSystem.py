import math
from random import choice
import random, EndGame, Assets, Zombie

import pygame


class Round():
    def __init__(self):
        self.HealthPool = 0
        self.roundCount = 0
        #self.maxEnemyCount = 0
        self.zombies = []
        
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

    def NewRound(self, round,maxRoundCount, zombieVel):
        self.roundCount = round
        #upper limit is 200 zombies loaded on screen
        #DO NOT EXCEED 200 ZOMBIES
        #opptiomization is needed to retest this above note
        
        #safe gaurd
        self.maxZombieCount = 5
        #self.maxZombieCount = self.increaseRoundCount(round, maxRoundCount)

        exclusion = []
        for i in range(500):
            exclusion.insert(0, -i)
            exclusion.append(i)
        rangeLower = -1000
        rangeUpper = 1000
        for i in range(self.maxZombieCount):
            x = choice([i for i in range(rangeLower, rangeUpper) if i not in exclusion])
            y = choice([i for i in range(rangeLower, rangeUpper) if i not in exclusion])
            self.zombies.append(Zombie.Zombie(i, zombieVel, x, y ))
        for i in range(self.maxZombieCount):
            self.HealthPool = 1
            print(self.zombies) 
            #self.HealthPool = sum(self.zombies[i].getZombieHealth())
        
    def roundCheck(self, player,maxRoundCount,zombieVel,deltaTime,currentTickZombieDamage):
        if self.HealthPool <= 0:
            self.zombies.clear()
            player.playerHealth = player.MAXHEALTH
            self.NewRound(self.roundCount+1,maxRoundCount, zombieVel)
        else:
            for i in range(len(self.zombies)):
                self.zombies[i].zombieBrain(player,deltaTime,zombieVel,currentTickZombieDamage)


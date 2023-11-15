import math
from random import choice
import random, EndGame, Assets, Zombie

import pygame


class Round():
    def __init__(self):
        self.HealthPool = 0
        self.roundCount = 0
        self.maxEnemyCount = 0
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

    def setZombieSpawn(self, exclusion, rangeLower, rangeUpper):
        self.zombieX = choice([i for i in range(rangeLower, rangeUpper) if i not in exclusion])
        self.zombieY = choice([i for i in range(rangeLower, rangeUpper) if i not in exclusion])

    def NewRound(self, round,maxRoundCount, zombieVel):
        self.roundCount = round
        #upper limit is 200 zombies loaded on screen
        #DO NOT EXCEED 200 ZOMBIES
        #opptiomization is needed to retest this above note
        
        #safe gaurd
        self.maxZombieCount = 20
        #self.maxZombieCount = self.increaseRoundCount(round, maxRoundCount)

        exclusion = []
        for i in range(500):
            exclusion.insert(0, -i)
            exclusion.append(i)
        rangeLower = -1000
        rangeUpper = 1000
        for i in range(self.maxEnemyCount):
            x = self.zombieX = choice([i for i in range(rangeLower, rangeUpper) if i not in exclusion])
            y = self.zombieY = choice([i for i in range(rangeLower, rangeUpper) if i not in exclusion])
            self.zombies.append(Zombie.Zombie(i, False, False, True, zombieVel, True, 0, 0 ))

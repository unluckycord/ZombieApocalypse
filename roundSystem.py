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

    def NewRound(self, round,maxRoundCount, zombieVel):
        self.roundCount = round
        for i in range(500):
            self.exclusion.append(i)
        #upper limit is 200 zombies loaded on screen
        #DO NOT EXCEED 200 ZOMBIES
        self.maxEnemyCount = 20
        #self.maxZombieCount = self.increaseRoundCount(round, maxRoundCount)
        for i in range(self.maxEnemyCount):
            x = self.randomZombiePosx(self.exclusion, -3075, 3075)
            y = self.randomZombiePosy(self.exclusion, -2020, 2020)
            self.zombieLocationsX.append(x)
            self.zombieLocationsY.append(y)
            self.zombies.append(Zombie.Zombie(i, False, False, True, zombieVel, True))
from random import choice
import random, EndGame, Assets, Zombie


class Round():
    def __init__(self):
        self.zombies = []
        self.roundCount = 0
        
    def roundCount(self, Round, maxRoundCount):
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

    def NewRound(self, Round,maxRoundCount, zombieVel,zombieDamageToPlayerSounds,zombieHurtSounds):
        self.roundCount = Round
        exclusion = []
        for i in range(500):
            exclusion.append(i)
        zombieLocationsX = []
        zombieLocationsY = []
        #upper limit is 200 zombies loaded on screen
        #DO NOT EXCEED 200 ZOMBIES
        #maxZombieCount = 20
        maxZombieCount = self.roundCount(Round, maxRoundCount)
        for i in range(maxZombieCount):
            x = self.randomZombiePosx(exclusion, -3075, 3075)
            y = self.randomZombiePosy(exclusion, -2020, 2020)
            zombieLocationsX.append(x)
            zombieLocationsY.append(y)
            self.zombies.append(Zombie.Zombie(i, 100, 20, False, 15, False, Assets.zombieSpriteIdel, x, y, Assets.PLAYERW-10, Assets.PLAYERH-10,zombieDamageToPlayerSounds,zombieHurtSounds, True, zombieVel, True))


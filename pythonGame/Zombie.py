class Zombie:
    def __init__(self,zombieCount,MAXHEALTH, zombieHealth, zombieTakingDamage, damageAmount, dealingDamage, sprite, zombiex, zombiey, zombiew, zombieh, randomZombieDamageSounds, randomZombieHurtSounds):
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
    
    def zombieMovement(self, player):
        if self.zombiex >= player.getPlayerx():
            self.zombiex -= 1
        if self.zombiex <= player.getPlayerx():
            self.zombiex += 1
        if self.zombiey >= player.getPlayery():
            self.zombiey -= 1
        if self.zombiey < player.getPlayery():
            self.zombiey += 1
    def zombieDamage(self, player):
        ##print(self.zombiex-player.getPlayerx(), self.zombiey-player.getPlayery())
        if self.zombieHealth > 0 and -20 < self.zombiex - player.getPlayerx() < 30 and -20 < self.zombiey - player.getPlayery() < 30:
            player.playerTakingDamage = True
            player.playerHealth -= 0.005
            
        else:
            player.playerTakingDamage = False
class Grenade:
    def __init__(self, grenadeVel, damageAmount):
        self.grenadeVel = grenadeVel
        self.damageAmount = damageAmount
        
    def getGrenadeVel(self):
        return self.grenadeVel
    def getDamageAmount(self):
        return self.damageAmount
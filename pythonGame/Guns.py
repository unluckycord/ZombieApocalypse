class Guns:
    def __init__(self, currentSprite, spriteShooting, idelSprite, gun, gunSound, gunReloading, MAXAMMO, currentAmmo, cooldown, cooldownReloading):
        self.currentSprite = currentSprite
        self.spriteShooting = spriteShooting
        self.idelSprite = idelSprite
        self.gun = gun
        self.gunSound = gunSound
        self.gunReloading = gunReloading
        self.MAXAMMO = MAXAMMO
        self.currentAmmo = currentAmmo
        self.cooldown = cooldown
        self.cooldownReloading = cooldownReloading
        
    def getCurrentSprite(self):
        return self.currentSprite
    def getSpriteShooting(self):
        return self.spriteShooting
    def getIdelSprite(self):
        return self.idelSprite
    def getGun(self):
        return self.gun
    def getGunSound(self):
        return self.gunSound.play()
    def getGunReloading(self):
        return self.gunReloading.play()
    def getCurrentAmmo(self):
        return self.currentAmmo
    def getMaxAmmo(self):
        return self.MAXAMMO
    def getCooldown(self):
        return self.cooldown
    def getCooldownReloading(self):
        return self.cooldownReloading
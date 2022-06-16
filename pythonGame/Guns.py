class Guns:
    def __init__(self, currentSprite, spriteShooting, idelSprite, gun, gunSound, gunReloading, MAXAMMO, currentAmmo, cooldown, cooldownReloading, vel, gunDamage):
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
        self.vel = vel
        self.gunDamage = gunDamage
        
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
    def getVel(self):
        return self.vel
    def getGunDamage(self, playerx, playery, zombiex, zombiey):
        if self.gun ==1:
            print(playerx - zombiex, playery - zombiey)
            if playerx - zombiex < 40 and playery - zombiey < 40:
                return self.gunDamage
            if 40 < playerx - zombiex < 50 or 40 < playery - zombiey < 50:
                return self.gunDamage * 0.9
            if 50 < playerx - zombiex < 80 or 50 < playery - zombiey < 80:
                return self.gunDamage * 0.8
            if 80 < playerx - zombiex < 110 or 80 < playery - zombiey < 110:
                return self.gunDamage * 0.6
            if 110 < playerx - zombiex < 140 or 110 < playery - zombiey < 140:
                return self.gunDamage * 0.4
            if 140 < playerx - zombiex < 170 or 140 < playery - zombiey < 170:
                return self.gunDamage * 0.1
            else:
                return self.gunDamage * 0.00001
        else:
            return self.gunDamage 
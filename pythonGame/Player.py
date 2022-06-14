import pygame
class Player:
    def __init__(self,MAXHEALTH, playerHealth, playerTakingDamage, playerGun, isWalking, sprite ,playerx, playery, playerw , playerh, VEL, canShoot, isReloading):
        self.MAXHEALTH = MAXHEALTH
        self.playerHealth = playerHealth
        self.playerTakingDamage = playerTakingDamage
        #its a number instead, 0 is handgun, 1 is shotgun and 2 is AK
        self.playerGun = playerGun
        self.isWalking = isWalking
        self.sprite = sprite
        self.playerx = playerx
        self.playery = playery
        self.playerw = playerw
        self.playerh = playerh
        self.VEL = VEL
        self.canShoot = canShoot
        self.isReloading = isReloading
    
    def getMaxhealth(self):
        return self.MAXHEALTH
    def getPlayerHealth(self):
        return self.playerHealth
    def getPlayerTakingDamage(self):
        return self.playerTakingDamage
    def getPlayerGun(self):
        return self.playerGun
    def getIsWalking(self):
        return self.isWalking
    def getSprite(self):
        return self.sprite
    def getPlayerx(self):
        return self.playerx
    def getPlayery(self):
        return self.playery
    def getPlayerw(self):
        return self.playerw
    def getPlayerh(self):
        return self.playerh
    def getVel(self):
        return self.VEL
    def getCanShoot(self):
        return self.canShoot
    def getIsReloading(self):
        return self.isReloading
    
    def regenHealth(self):
        if self.playerTakingDamage == False and self.playerHealth <= self.MAXHEALTH:
            self.playerHealth += 0.3
    
    def playerMovement(self,keysPressed, zombies, objects,worldDistanceX, worldDistanceY, gun):
        if self.playerHealth > 0:
            if keysPressed[pygame.K_r] and gun[self.playerGun].currentAmmo != gun[self.playerGun].MAXAMMO:
                self.isReloading = True
                gun[self.playerGun].getGunReloading()
                gun[self.playerGun].currentAmmo = gun[self.playerGun].MAXAMMO
            if keysPressed[pygame.K_1]:
                self.playerGun = 0
            if keysPressed[pygame.K_2]:
                self.playerGun = 1
            if keysPressed[pygame.K_3]:
                self.playerGun = 2
            if keysPressed[pygame.K_a] or keysPressed[pygame.K_d] or keysPressed[pygame.K_s] or keysPressed[pygame.K_w] and worldDistanceX > -750 and worldDistanceX < 750 and worldDistanceY > -750 and worldDistanceY < 750:
                self.isWalking = True
            else:
                self.isWalking = False
            for i in range(len(objects)):
                if keysPressed[pygame.K_a]and worldDistanceX > -750:
                    objects[i].posx += self.VEL
                elif keysPressed[pygame.K_d]and worldDistanceX < 750:
                    objects[i].posx -= self.VEL
                if keysPressed[pygame.K_w]and worldDistanceY > -750:
                    objects[i].posy += self.VEL
                elif keysPressed[pygame.K_s]and worldDistanceY < 750:
                    objects[i].posy -= self.VEL
            for i in range(len(zombies)):
                if keysPressed[pygame.K_a]and worldDistanceX > -750:
                    zombies[i].zombiex += self.VEL
                elif keysPressed[pygame.K_d]and worldDistanceX < 750:
                    zombies[i].zombiex -= self.VEL
                if keysPressed[pygame.K_w]and worldDistanceY > -750:
                    zombies[i].zombiey += self.VEL
                elif keysPressed[pygame.K_s]and worldDistanceY < 750:
                    zombies[i].zombiey -= self.VEL
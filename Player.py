import pygame, Grenade, Assets, Bullet, Game
class Player:
    def __init__(self,MAXHEALTH, playerHealth, playerTakingDamage, playerGun, isWalking, sprite ,playerx, playery, playerw , playerh, VEL, canShoot, isReloading, healablesOwned, isShooting, grenadeCount):
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
        self.healablesOwned = healablesOwned
        self.isShooting = isShooting
        self.grenadeCount = grenadeCount

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
    def getHealablesOwned(self):
        return self.healablesOwned
    def getIsShooting(self):
        return self.isShooting
    
    def playerMovement(self,keysPressed, zombies, objects, gun, currentTickHeal, nowHealing, bullets, grenades, grenadeVel, currentTickTossGrenade, nowTossGrenade, mousex,mousey):
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
            
            #grenade is 4
            nowTossGrenade = pygame.time.get_ticks()
            if nowTossGrenade - currentTickTossGrenade >= 3000 and self.grenadeCount > 0 and keysPressed[pygame.K_4]:
                currentTickTossGrenade = nowTossGrenade
                self.grenadeCount -= 1   
                grenades.append(Grenade.Grenade(3, 50))
                currentTickTossGrenade = nowTossGrenade
        
            #health shot is 5
            nowHealing = pygame.time.get_ticks()
            if self.playerHealth < self.MAXHEALTH and nowHealing - currentTickHeal >= 3000 and self.healablesOwned > 0 and keysPressed[pygame.K_5]:
                Assets.HEALTHSHOT.play()
                self.healablesOwned -= 1
                currentTickHeal = nowHealing
                self.playerHealth = self.MAXHEALTH
                
            if keysPressed[pygame.K_a] or keysPressed[pygame.K_d] or keysPressed[pygame.K_s] or keysPressed[pygame.K_w]:
                self.isWalking = True
            else:
                self.isWalking = False
            for i in range(len(bullets)):
                if keysPressed[pygame.K_a]:
                    bullets[i].bulletx += self.VEL
                elif keysPressed[pygame.K_d]:
                    bullets[i].bulletx -= self.VEL
                if keysPressed[pygame.K_w]:
                    bullets[i].bullety += self.VEL
                elif keysPressed[pygame.K_s]:
                    bullets[i].bullety -= self.VEL
            for i in range(len(objects)):
                if keysPressed[pygame.K_a]:
                    objects[i].posx += self.VEL
                elif keysPressed[pygame.K_d]:
                    objects[i].posx -= self.VEL
                if keysPressed[pygame.K_w]:
                    objects[i].posy += self.VEL
                elif keysPressed[pygame.K_s]:
                    objects[i].posy -= self.VEL
            for i in range(len(zombies)):
                if keysPressed[pygame.K_a]:
                    zombies[i].zombieX += self.VEL
                elif keysPressed[pygame.K_d]:
                    zombies[i].zombieX -= self.VEL
                if keysPressed[pygame.K_w]:
                    zombies[i].zombieY += self.VEL
                elif keysPressed[pygame.K_s]:
                    zombies[i].zombieY -= self.VEL
        
import pygame, Grenade, Assets, Bullet, Game
class Player:
    def __init__(self, VEL, healablesOwned, grenadeCount, Pistol, Shotgun, AK47):
        self.MAXHEALTH = 1000
        self.playerHealth = 1000
        self.isAlive = True
        self.playerTakingDamage = False
        #its a number instead, 0 is handgun, 1 is shotgun and 2 is AK
        self.playerGun = Pistol
        self.platerInventoryGuns = [Pistol, Shotgun, AK47]
        self.isWalking = False
        self.sprite = Assets.playerSpriteIdelHandgun
        self.playerx = Assets.CENTERX
        self.playery = Assets.CENTERY
        self.playerw = Assets.PLAYERW
        self.playerh = Assets.PLAYERH
        self.VEL = VEL
        self.canShoot = True
        self.isReloading = False
        self.healablesOwned = healablesOwned
        self.isShooting = False
        self.grenadeCount = grenadeCount
        self.walkingSound = Assets.WALKINGCONCRETE
        self.playerHitBox = pygame.draw.rect(Assets.WIN, Assets.BLACK, (self.getPlayerx(), self.getPlayery(), self.getPlayerh(), self.getPlayerw()))

    def getMaxhealth(self):
        return self.MAXHEALTH
    def getPlayerHealth(self):
        return self.playerHealth
    def getPlayerTakingDamage(self):
        return self.playerTakingDamage
    def getPlayerGun(self):
        return self.playerGun
    def gerPlayerGunInventory(self):
        return self.platerInventoryGuns
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
    def getGrenadeCount(self):
        return self.grenadeCount
    def getIsShooting(self):
        return self.isShooting
    
    def playerMovementSound(self, currentTickWalking):
        #walking sounds based on ticks
        nowWalking = pygame.time.get_ticks()
        if nowWalking - currentTickWalking >= 500 and self.getIsWalking():
            currentTickWalking = nowWalking
            self.walkingSound.play()
        elif self.isWalking == False:
            self.walkingSound.stop()
    
    def playerMovement(self,keysPressed, zombies, objects, currentTickHeal, nowHealing, grenades, grenadeVel, currentTickTossGrenade, nowTossGrenade, mousex,mousey):
        if self.playerHealth > 0:
            
            if keysPressed[pygame.K_r] and self.getPlayerGun().getCurrentAmmo() != self.getPlayerGun().MAXAMMO:
                self.isReloading = True
                self.playerGun.getGunReloading()
                self.getPlayerGun().currentAmmo = self.getPlayerGun().MAXAMMO
            if keysPressed[pygame.K_1]:
                self.playerGun = self.platerInventoryGuns[0]
            if keysPressed[pygame.K_2]:
                self.playerGun = self.platerInventoryGuns[1]
            if keysPressed[pygame.K_3]:
                self.playerGun = self.platerInventoryGuns[2]
            
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

            #for i in range(len(bullets)):
            #    if keysPressed[pygame.K_a]:
            #        bullets[i].bulletx += self.VEL
            #    elif keysPressed[pygame.K_d]:
            #        bullets[i].bulletx -= self.VEL
            #    if keysPressed[pygame.K_w]:
            #        bullets[i].bullety += self.VEL
            #    elif keysPressed[pygame.K_s]:
            #        bullets[i].bullety -= self.VEL
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
        
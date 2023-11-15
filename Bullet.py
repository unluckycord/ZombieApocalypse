import math, Assets, pygame
from random import randint
class Bullet:
    def __init__(self, gun, bulletx, bullety, vel, mousex, mousey):
        # 0 is hand gun
        # 1 is shotgun
        # 2 is AK
        #3 is RPG
        self.gun = gun
        self.bulletx = bulletx
        self.bullety = bullety
        self.mousex = mousex
        self.mousey = mousey
        self.vel = vel

        self.bulletHead = pygame.draw.circle(Assets.WIN, Assets.RED, (self.bulletx, self.bullety), 2)
        self.casing = Assets.playerBullet
        
        self.angle = math.atan2(bullety-mousey, bulletx - mousex)
        self.sprite = pygame.transform.rotate(Assets.playerSlug, randint(0, 360))
        self.xvel = math.cos(self.angle)*self.vel
        self.yvel = math.sin(self.angle)*self.vel
        
    def getGun(self):
        return self.gun
    def getBulletx(self):
        return self.bulletx
    def getBullety(self):
        return self.bullety
    def getVel(self):
        return self.vel
    def getRenderBullet(self):
        return self.renderBullet
    def getAngle(self):
        return self.angle
    def getSprite(self):
        return self.sprite
    def bulletHitbox(self, player):
        self.bulletx -= int(self.xvel)
        self.bullety -= int(self.yvel)
        if player.getPlayerGun() == 1:
            return self.bulletx, self.bullety, 30,30
        return self.bulletx, self.bullety, 10, 10
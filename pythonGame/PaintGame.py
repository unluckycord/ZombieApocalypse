import pygame,Assets,Zombie,Player,Game
def drawWindow(player, zombies, objects, gun):
    #Assets.WIN.fill(Assets.WHITE);
    for i in range(len(objects)):
        Assets.WIN.blit(objects[i].getSprite(), (objects[i].getPosX(), objects[i].getPosY()))
    for i in range(len(zombies)):
        Assets.WIN.blit(zombies[i].getSprite(), (zombies[i].getZombiex(), zombies[i].getZombiey()))

    Assets.WIN.blit(Assets.START_FONT.render(str(gun[player.getPlayerGun()].getCurrentAmmo()),1, Assets.RED),((20),(20)))
    if gun[player.getPlayerGun()].getCurrentAmmo() < 10:
        Assets.WIN.blit(Assets.START_FONT.render("/" + str(gun[player.getPlayerGun()].getMaxAmmo()),1, Assets.RED),((40),(20)))
    else:
        Assets.WIN.blit(Assets.START_FONT.render("/" + str(gun[player.getPlayerGun()].getMaxAmmo()),1, Assets.RED),((55),(20)))
        
    pygame.draw.rect(Assets.WIN, Assets.BLACK, (Assets.WIDTH - player.getMaxhealth()//2 - 50,10, player.getMaxhealth()//2 ,20))  
    pygame.draw.rect(Assets.WIN, Assets.RED, (Assets.WIDTH - player.getPlayerHealth()//2 - 50,10, player.getPlayerHealth()//2 ,20))
    
    Assets.WIN.blit(player.getSprite(), (Assets.CENTERX, Assets.CENTERY))
    pygame.display.update()
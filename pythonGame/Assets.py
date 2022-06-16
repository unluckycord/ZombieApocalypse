import pygame
pygame.mixer.init()
pygame.font.init()
clock = pygame.time.Clock()
run = True
START_FONT = pygame.font.SysFont("Horror Poster Trajan Pro",40)
START_FONT_SMALL = pygame.font.SysFont("Horror Poster Trajan Pro",20)
WIDTH, HEIGHT = 1200, 800
CENTERX, CENTERY = WIDTH//2-50, HEIGHT//2-50
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
FPS = 120
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
PLAYERW, PLAYERH = 75,75

zombieSpriteIdel = pygame.transform.scale(pygame.image.load(
    "Assets/sprites/zombieIdel.png"), (PLAYERW, PLAYERH))
zombieSpriteCorpse = pygame.transform.scale(pygame.image.load(
    "Assets/sprites/zombieCorpse.png"), (PLAYERW, PLAYERH))

#gun sprites
playerSpriteIdelAK47 = pygame.transform.scale(pygame.image.load(
    "Assets/sprites/playerSprites/rifle/idle/playerIdelAK47.png"), (PLAYERW, PLAYERH))
playerSpriteIdelShotgun = pygame.transform.scale(pygame.image.load(
    "Assets/sprites/playerSprites/shotgun/idle/playerIdelShotgun.png"), (PLAYERW, PLAYERH))
playerSpriteIdelHandgun = pygame.transform.scale(pygame.image.load(
    "Assets/sprites/playerSprites/handgun/idle/playerIdelHandgun.png"), (PLAYERW, PLAYERH))
playerHealthSprite = pygame.transform.scale(pygame.image.load("Assets/sprites/playerSprites/heart.png"), (70,70))

playerSpriteAK47Muzzle = pygame.transform.scale(pygame.image.load(
    "Assets/sprites/playerSprites/rifle/shoot/playerShootingAK47.png"), (PLAYERW, PLAYERH))
playerSpriteShotgunMuzzle = pygame.transform.scale(pygame.image.load(
    "Assets/sprites/playerSprites/shotgun/shoot/playerShootingShotgun.png"), (PLAYERW, PLAYERH))
playerSpriteHandgunMuzzle = pygame.transform.scale(pygame.image.load(
    "Assets/sprites/playerSprites/handgun/shoot/playerShootingHandgun.png"), (PLAYERW, PLAYERH))
playerBullet = pygame.transform.scale(pygame.image.load(
    "/Users/unluckycord/python_projects/pythonGame/Assets/sprites/bullet.png"), (20,20))

#audio for player
WALKINGCONCRETE = pygame.mixer.Sound("Assets/sounds/playerSounds/walkingConcrete.wav")

#audio for guns
HANDGUNSOUNDEFFECT = pygame.mixer.Sound("Assets/sounds/gunSounds/handgunShooting.wav")
AK47SOUNDEFFECT = pygame.mixer.Sound("Assets/sounds/gunSounds/ak47.wav")
SHOTGUNSOUNDEFFECT = pygame.mixer.Sound("Assets/sounds/gunSounds/shotgunSoundEffect.wav")
EMPTYGUN = pygame.mixer.Sound("Assets/sounds/gunSounds/emptyGun.wav")
RELOADHANDGUN =  pygame.mixer.Sound("Assets/sounds/gunSounds/reload_pistol_fast.wav")
RELOADSHOTGUN =  pygame.mixer.Sound("Assets/sounds/gunSounds/reload_shotgun_fast.wav")
RELOADAK47 =  pygame.mixer.Sound("Assets/sounds/gunSounds/reload_ar_fast.wav")
SHOTGUNCOCK = pygame.mixer.Sound("Assets/sounds/gunSounds/shotgunClick.wav")

#audio for zombies
ZOMBIEATTACK1 = pygame.mixer.Sound("Assets/sounds/enemySounds/Zombie-Aggressive-Attack-A1.mp3")
ZOMBIEATTACK2 = pygame.mixer.Sound("Assets/sounds/enemySounds/Zombie-Aggressive-Attack-A2.mp3")
ZOMBIEATTACK3 = pygame.mixer.Sound("Assets/sounds/enemySounds/Zombie-Aggressive-Attack-A3.mp3")
ZOMBIEATTACK4 = pygame.mixer.Sound("Assets/sounds/enemySounds/Zombie-Aggressive-Attack-A4.mp3")
ZOMBIEATTACK5 = pygame.mixer.Sound("Assets/sounds/enemySounds/Zombie-Aggressive-Attack-A5.mp3")
ZOMBIEATTACK6 = pygame.mixer.Sound("Assets/sounds/enemySounds/Zombie-Aggressive-Attack-A6.mp3")
ZOMBIEATTACK7 = pygame.mixer.Sound("Assets/sounds/enemySounds/Zombie-Aggressive-Attack-A7.mp3")
ZOMBIEATTACK8 = pygame.mixer.Sound("Assets/sounds/enemySounds/Zombie-Aggressive-Attack-A8.mp3")
ZOMBIEATTACK9 = pygame.mixer.Sound("Assets/sounds/enemySounds/Zombie-Aggressive-Attack-A9.mp3")


#Backgrounds
mainMenuBackground = pygame.transform.scale(pygame.image.load("Assets/backgrounds/menu.png"), (WIDTH, HEIGHT))
blackBackground = pygame.transform.scale(pygame.image.load("Assets/backgrounds/blackButton.png"), (300, 70))
REF = pygame.image.load("Assets/backgrounds/re.png")
MUSICON = pygame.transform.scale(pygame.image.load("Assets/backgrounds/musicOn.png"),(PLAYERW,PLAYERH))
MUSICOFF = pygame.transform.scale(pygame.image.load("Assets/backgrounds/musicOff.png"),(PLAYERW,PLAYERH))
BUILDING = pygame.transform.scale(pygame.image.load("Assets/sprites/house.png"),(550,500))
GROUND = pygame.transform.scale(pygame.image.load("Assets/backgrounds/ground.png"),(6120,4040))
#Sounds
BACKGROUNDMAP1 = pygame.mixer.Sound("Assets/sounds/music/VOICES.wav")
MAINMENUTHEME = pygame.mixer.Sound("Assets/sounds/music/HorrorSoundscape.wav")
FADESFX = pygame.mixer.Sound("Assets/sounds/fade.wav")
GAMELOST = pygame.mixer.Sound("Assets/sounds/game_lose.wav")
GAMEWON = pygame.mixer.Sound("Assets/sounds/game_win.wav")
MENUCONFIRM = pygame.mixer.Sound("Assets/sounds/menuConfirm.wav")
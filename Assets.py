import pygame,pygame,Main
pygame.mixer.init()
pygame.font.init()
clock = pygame.time.Clock()

pygame.mixer.music.set_volume(Main.vol)

run = True
START_FONT = pygame.font.SysFont("Horror Poster Trajan Pro", 40)
START_FONT_ITALIC = pygame.font.SysFont("Horror Poster Trajan Pro", 40, italic=True)
START_FONT_BOLD = pygame.font.SysFont("Horror Poster Trajan Pro", 40, bold=True)
START_FONT_BOLD_ITALIC = pygame.font.SysFont("Horror Poster Trajan Pro", 40, bold=True, italic=True)
START_FONT_SMALL = pygame.font.SysFont("Horror Poster Trajan Pro", 20)
WIDTH, HEIGHT = 1200, 800
CENTERX, CENTERY = WIDTH//2-50, HEIGHT//2-50
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
GREY = (169,169,169)
TARGETFPS = 120
textcolor = WHITE
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
    "Assets/sprites/bullet.png"), (20,20))
playerSlug = pygame.transform.scale(pygame.image.load(
    "Assets/sprites/slug.png"), (20,20))

#audio for player
WALKINGCONCRETE = pygame.mixer.Sound("Assets/sounds/playerSounds/walkingConcrete.wav")
HEALTHSHOT = pygame.mixer.Sound("Assets/sounds/playerSounds/healthsound.wav")

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
ZOMBIEHURT1 = pygame.mixer.Sound("Assets/sounds/enemySounds/zombie_hit1.wav")
ZOMBIEHURT2 = pygame.mixer.Sound("Assets/sounds/enemySounds/zombie_hit2.wav")
ZOMBIEHURT3 = pygame.mixer.Sound("Assets/sounds/enemySounds/zombie_hit3.wav")


#Backgrounds
mainMenuBackground = pygame.transform.scale(pygame.image.load("Assets/backgrounds/menu.jpeg"), (WIDTH, HEIGHT))
gunShopBackground = pygame.transform.scale(pygame.image.load("Assets/backgrounds/gunShop.png"),(500,320))
EndlessMode = pygame.transform.scale(pygame.image.load("Assets/backgrounds/EndlessMode.jpeg"), (WIDTH//3 - 60, HEIGHT - 160))
CampaignMode = pygame.transform.scale(pygame.image.load("Assets/backgrounds/CampaignMode.jpeg"), (WIDTH//3 - 60, HEIGHT - 160))
placeHolder = pygame.transform.scale(pygame.image.load("Assets/backgrounds/placeHolder.png"),(WIDTH//3 - 60, HEIGHT - 160))
levelSelectionBackground = pygame.transform.scale(pygame.image.load("Assets/backgrounds/levelSelection.jpeg"), (500,320))
level1 = pygame.transform.scale(pygame.image.load("Assets/backgrounds/level1.jpeg"), (300, 200))

backArrow = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Assets/backgrounds/backArrow.png"), (50,50)), 180)
REF = pygame.image.load("Assets/backgrounds/re.png")
MUSICON = pygame.transform.scale(pygame.image.load("Assets/backgrounds/musicOn.png"),(PLAYERW,PLAYERH))
MUSICONOFF = pygame.transform.scale(pygame.image.load("Assets/backgrounds/musicOff.png"),(PLAYERW,PLAYERH))
BUILDING = pygame.transform.scale(pygame.image.load("Assets/sprites/house.png"),(550,500))
GROUND = pygame.transform.scale(pygame.image.load("Assets/backgrounds/map.png"),(6000,4050))
#Sounds
GUNSHOPSOUND = pygame.mixer.Sound("Assets/sounds/gunSounds/gunShopSound.wav")
CONFIM = pygame.mixer.Sound("Assets/sounds/confirm.wav")
DECLINE = pygame.mixer.Sound("Assets/sounds/decline.mp3")
BACKGROUNDMAP1 = pygame.mixer.Sound("Assets/sounds/music/VOICES.wav")
MAINMENUTHEME = pygame.mixer.Sound("Assets/sounds/music/HorrorSoundscape.wav")
FADESFX = pygame.mixer.Sound("Assets/sounds/fade.wav")
GAMELOST = pygame.mixer.Sound("Assets/sounds/game_lose.wav")
GAMEWON = pygame.mixer.Sound("Assets/sounds/game_win.wav")
MENUCONFIRM = pygame.mixer.Sound("Assets/sounds/menuConfirm.wav")

testSound = pygame.mixer.Sound("Assets/test.wav")
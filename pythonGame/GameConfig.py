class GameConfig:
    def __init__(self, boarderAroundHealth, music, HUD, sounds):
        self.boarderAroundHealth = boarderAroundHealth
        self.music = music
        self.HUD = HUD
        self.sounds = sounds
    
    def getBoarderAroundHealth(self):
        return self.boarderAroundHealth
    def getMusic(self):
        return self.music
    def getHUD(self):
        return self.HUD
    def getSounds(self):
        return self.sounds
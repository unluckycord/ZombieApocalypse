import pygame,StartScreen,Game, os

pygame.display.set_caption("Zombie Apocalypse")

vol = 1.0

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #Game.start()
    StartScreen.startUI()

if __name__ == "__main__":
    main()
    
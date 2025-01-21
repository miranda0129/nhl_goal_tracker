import pygame
from NextGame import NextGame
from time import sleep
from Display import Display
import TimeDateHelpers

pygame.init()

TEAM_ABBREV = 'DET'
nextGame = NextGame(TEAM_ABBREV)
nextGame.getNextGame()

isGameToday = nextGame.isNextGameToday()
gameTime = nextGame.nextGameTime
gameId = nextGame.nextGameId

print("The wings are playing next at...", gameTime)
print("Game Id: ", gameId)

display = Display() 
counter = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    display.screen.fill((255, 255, 255))  # white background
    
    print("doing other work")
    counter += 1
    sleep(1)

    if (counter > 3):
        #display.displayGoal()
        if ((counter%5) == 0):
            display.displayGoal()
        else:
          display.displayScore([counter, counter], ["DET", "OTH"])
    else:
        display.displayNextGame(TimeDateHelpers.toTwelveHourTime(nextGame.nextGameTime))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
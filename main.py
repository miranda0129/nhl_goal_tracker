from time import sleep
from pprint import pprint
import LiveGame
from NextGame import NextGame
import TimeDateHelpers
import pygame
from Display import Display

TEAM_ABBREV = 'DET'
TIME_ZONE = 'US/Eastern'


def runLoop():
    nextGame = NextGame(TEAM_ABBREV)
    nextGame.getNextGame()
    isGameToday = nextGame.isNextGameToday()
    gameTime = nextGame.getTime()
    gameId = nextGame.nextGameId

    print("The wings are playing next at...", gameTime)
    print("Game Id: ", gameId)
    display.displayNextGame(gameTime)
    pygame.display.flip()

    if (isGameToday):
        #wait until game goes live
        timeDela = TimeDateHelpers.getTimeUntilGame(gameTime)
        totalSeconds = TimeDateHelpers.getSecondsToTime(timeDela)
        TimeDateHelpers.sleepUntilGame(totalSeconds)
        
        liveGame = LiveGame.LiveGame(nextGame.nextGameId)
        while True:
            if(liveGame.getIsLive()):
                break
            sleep(1)

        #track score while game is live
        while(liveGame.getIsLive()):
            if (liveGame.home_or_away == ''):
             liveGame.getTeamSide()
        score = liveGame.getScore()
        display.displayScore(score)
        pygame.display.flip()

        if (liveGame.hasScoreIncreased(score[0])):
                display.displayGoal()
                pygame.display.flip()

        pprint('~~~~~~~~~~~~~~~~~~~')
        sleep(1)

        runLoop()


    else:
        #check for game again tomorrow
        timeTomorrow = TimeDateHelpers.getTimeForTomorrowMorning()
        secondsToSleep = TimeDateHelpers.getSecondsUntilTomorrowCheck(timeTomorrow)
        print("Sleeping for ", secondsToSleep, " seconds until ", timeTomorrow)
        sleep(secondsToSleep)
        runLoop()

if __name__ == "__main__":
    display = Display() 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
        display.screen.fill((255, 255, 255))
        runLoop()
        pygame.display.flip()
    pygame.quit()





 
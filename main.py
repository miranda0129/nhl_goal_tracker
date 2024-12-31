from time import sleep
from pprint import pprint
import LiveGame
from NextGame import NextGame
import TimeDateHelpers
import pygame
from Display import Display
import threading

TEAM_ABBREV = 'DET'
TIME_ZONE = 'US/Eastern'

checkForNextGame = True
gameOn = False
nextGame = NextGame(TEAM_ABBREV)

def sleepUntilTomorrow():
        global checkForNextGame
        #check for game again tomorrow
        timeTomorrow = TimeDateHelpers.getTimeForTomorrowMorning()
        secondsToSleep = TimeDateHelpers.getSecondsUntilTomorrowCheck(timeTomorrow)
        print("Sleeping for ", secondsToSleep, " seconds until ", timeTomorrow)
        sleep(secondsToSleep)
        checkForNextGame = True

def sleepUntilGame(gameTime):
    global gameOn
    timeDela = TimeDateHelpers.getTimeUntilGame(gameTime)
    totalSeconds = TimeDateHelpers.getSecondsToTime(timeDela)
    print("Sleeping for ", totalSeconds, " seconds until ", gameTime)
    TimeDateHelpers.sleepUntilGame(totalSeconds)
    gameOn = True


def runLoop():
    global checkForNextGame
    global nextGame
    global gameOn
    isGameToday = False
    
    if (checkForNextGame):
        nextGame.getNextGame()
        isGameToday = nextGame.isNextGameToday()
        gameTime = nextGame.nextGameTime
        gameId = nextGame.nextGameId

        print("The wings are playing next at...", gameTime)
        print("Game Id: ", gameId)
        pygame.display.flip()

        if (not isGameToday):
            print("threading for sleep")
            checkForNextGame = False
            worker = threading.Thread(target=sleepUntilTomorrow, daemon=True)
            print(type(worker))
            worker.start()
            print(worker.is_alive)

    display.displayNextGame(TimeDateHelpers.toTwelveHourTime(nextGame.nextGameTime))

    if (isGameToday):
        checkForNextGame = False

        sleepThread = threading.Thread(target=sleepUntilGame, daemon=True, args=(gameTime,))
        if (not sleepThread.is_alive()):
            sleepThread.start()

        if (gameOn):
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





 
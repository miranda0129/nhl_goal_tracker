from time import sleep
from pprint import pprint
from LiveGame import LiveGame
from NextGame import NextGame
import TimeDateHelpers
import pygame
from Display import Display
import threading

TEAM_ABBREV = 'DET'
TIME_ZONE = 'US/Eastern'

checkForNextGame = True
sleepForGame = True
isGameToday = False
gameOn = False

nextGame = NextGame(TEAM_ABBREV)
liveGame = None


def sleepUntilTomorrow():
    global checkForNextGame
    timeTomorrow = TimeDateHelpers.getTimeForTomorrowMorning()
    secondsToSleep = TimeDateHelpers.getSecondsUntilTomorrowCheck(timeTomorrow)
    print("Sleeping for ", secondsToSleep, " seconds until ", timeTomorrow)
    sleep(secondsToSleep)
    checkForNextGame = True

def sleepUntilGame(gameTime):
    global gameOn
    timeDela = TimeDateHelpers.getTimeUntilGame(gameTime)
    totalSeconds = TimeDateHelpers.getSecondsToTime(timeDela)

    if (totalSeconds > 0):
        print("Sleeping for ", totalSeconds, " seconds until ", gameTime)
        sleep(totalSeconds)
    gameOn = True


def runLoop():
    global checkForNextGame
    global isGameToday
    global sleepForGame
    global gameOn

    global nextGame
    global liveGame
    
    if (checkForNextGame):
        nextGame.getNextGame()
        isGameToday = nextGame.isNextGameToday()
        gameTime = nextGame.nextGameTime
        gameId = nextGame.nextGameId

        print("The wings are playing next at...", gameTime)
        print("Game Id: ", gameId)

        if (not isGameToday):
            checkForNextGame = False
            sleepThread = threading.Thread(target=sleepUntilTomorrow, daemon=True)
            sleepThread.start()

    if (isGameToday):
        checkForNextGame = False

        if (liveGame == None):
            liveGame = LiveGame(nextGame.nextGameId)

        if (not gameOn):
            display.displayTodayGame(TimeDateHelpers.toTwelveHourTime(nextGame.nextGameTime))

            if (sleepForGame):
                sleepForGame = False
                sleepThread = threading.Thread(target=sleepUntilGame, daemon=True, args=(nextGame.nextGameTime,))
                sleepThread.start()

        if (gameOn):
            liveGame.update()

            #track score while game is live
            if (liveGame.getIsLive()):
                if (liveGame.home_or_away == ''):
                    liveGame.getTeamSide()
                score = liveGame.getScore()

                #[DET, other]
                display.displayScore(score, [liveGame.team_abbrev, liveGame.vs_team_abbrev])

                if (liveGame.hasScoreIncreased(score[0])):
                    display.displayGoal()

                pprint('~~~~~~~~~~~~~~~~~~~')

            #reset once game is finished
            elif (liveGame.isGameFinished()):
                checkForNextGame = True
                sleepForGame = True
                gameOn = False
                isGameToday = False
                liveGame = None
                print(checkForNextGame, sleepForGame, gameOn, isGameToday)

            #wait for game to start
            else:
                display.displayTodayGame(TimeDateHelpers.toTwelveHourTime(nextGame.nextGameTime))

    else:
         display.displayNextGame(TimeDateHelpers.toTwelveHourTime(nextGame.nextGameTime))

    sleep(1)



if __name__ == "__main__":
    pygame.init()
    pygame.mouse.set_visible(False)
    display = Display() 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or  (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                running = False
        display.screen.fill((255, 255, 255))
        runLoop()
        pygame.display.flip()
    pygame.quit()





 
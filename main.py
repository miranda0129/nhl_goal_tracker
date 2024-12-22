import requests
from time import sleep
from pprint import pprint
from datetime import datetime, timedelta
import pytz
import LiveGame
from NextGame import NextGame
import TimeDateHelpers

TEAM_ABBREV = 'DET'
TIME_ZONE = 'US/Eastern'

def watchLiveGame():
    currentGame = LiveGame('2024020412')

    # currentGame.getIsLive()
    # currentGame.getScore()

    while (currentGame.getIsLive() == True):
        if (currentGame.home_or_away == ''):
            currentGame.getTeamSide()
        score = currentGame.getScore()
        currentGame.hasScoreIncreased(score)
        pprint('~~~~~~~~~~~~~~~~~~~')
        sleep(1)


def main():
    nextGame = NextGame('DET')
    nextGame.getNextGame()

    isGameToday = nextGame.isNextGameToday()
    gameTime = nextGame.getTime()
    gameId = nextGame.nextGameId

    if (isGameToday):
        print("The wings are playing today at...", gameTime)
        print("Game Id: ", gameId)

        timeDela = TimeDateHelpers.getTimeUntilGame(gameTime)
        totalSeconds = TimeDateHelpers.getSecondsToTime(timeDela)
        TimeDateHelpers.sleepUntilGame(totalSeconds)
        
        liveGame = LiveGame.LiveGame(nextGame.nextGameId)
        while True:
            if(liveGame.getIsLive()):
                break
            sleep(1)

        while(liveGame.getIsLive()):
         liveGame.getScore()
         sleep(1)


    else:
        print("The wings will be playing next at ", gameTime)
        print("Game Id: ", gameId)

        timeTomorrow = TimeDateHelpers.getTimeForTomorrowMorning()
        secondsToSleep = TimeDateHelpers.getSecondsUntilTomorrowCheck(timeTomorrow)
        print("Sleeping for ", secondsToSleep, " seconds until ", timeTomorrow)
        sleep(secondsToSleep)

if __name__ == "__main__":
    main()




 
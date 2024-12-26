import requests
from time import sleep
from pprint import pprint
from datetime import datetime, timedelta, timezone
import pytz

def getTimeUntilGame(time):
    eastern_tz = pytz.timezone('US/Eastern')
    timeDelta = time - datetime.now(eastern_tz)
    return timeDelta

def getSecondsToTime(timeDelta):
    print("Time to sleep before game start", timeDelta)
    total_seconds = timeDelta.total_seconds()
    return total_seconds

def sleepUntilGame(secondsUntilGame):
    sleep(secondsUntilGame)

def getTimeForTomorrowMorning():
    eastern_tz = pytz.timezone('US/Eastern')
    tomorrow = datetime.now(eastern_tz) + timedelta(days = 1)
    tomorrowMorning = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 7, 00, tzinfo=eastern_tz)
    return tomorrowMorning

def getSecondsUntilTomorrowCheck(time):
    eastern_tz = pytz.timezone('US/Eastern')
    timeDelta = time - datetime.now(eastern_tz)
    return timeDelta.total_seconds()



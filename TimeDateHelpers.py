from time import sleep
from datetime import datetime, timedelta
import pytz

def getTimeUntilGame(time):
    eastern_tz = pytz.timezone('US/Eastern')
    timeDelta = time - datetime.now(eastern_tz)
    return timeDelta

def getSecondsToTime(timeDelta):
    total_seconds = timeDelta.total_seconds()
    return total_seconds

def getTimeForTomorrowMorning():
    eastern_tz = pytz.timezone('US/Eastern')
    tomorrow = datetime.now(eastern_tz) + timedelta(days = 1)
    tomorrowMorning = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 7, 00, tzinfo=eastern_tz)
    return tomorrowMorning

def getSecondsUntilTomorrowCheck(time):
    eastern_tz = pytz.timezone('US/Eastern')
    timeDelta = time - datetime.now(eastern_tz)
    return timeDelta.total_seconds()

def toTwelveHourTime(time_24):
    return time_24.strftime("%B %d, %I:%M %p")



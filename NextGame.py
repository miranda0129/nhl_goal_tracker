import requests
from datetime import datetime
import pytz

class NextGame:
    def __init__(self, teamAbbrev) -> None:
        self.teamAbbrev = teamAbbrev
        self.nextGameDay = None
        self.nextGameTime = None
        self.nextGameId = None

    def getNextGame(self):
        season_schedule_url = f'https://api-web.nhle.com/v1/club-schedule-season/{self.teamAbbrev}/now'
        season_schedule_response = requests.get(season_schedule_url)
        season_schedule_dict = season_schedule_response.json()

        #Get next game wings are playing
        for item in season_schedule_dict['games']:
            gameState = item['gameState']
            if (gameState == 'FUT' or gameState == 'PRE' or gameState == 'LIVE' or gameState == 'CRIT'):
                self.nextGameId = item['id']

                gameDayJson = item['startTimeUTC']
                self.nextGameDay = datetime.strptime(item['gameDate'], "%Y-%m-%d").date()

                utcTime = datetime.strptime(gameDayJson, "%Y-%m-%dT%H:%M:%SZ")
                utcTime = pytz.utc.localize(utcTime)
                eastern_tz = pytz.timezone('US/Eastern')
                local_time = utcTime.astimezone(eastern_tz)
                self.nextGameTime = local_time
                break

    def isNextGameToday(self):
        self.getNextGame()
        today_date = datetime.today().date()
        if (today_date == self.nextGameDay):
            return True
        return False

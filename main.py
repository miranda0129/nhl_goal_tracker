import requests
from time import sleep
from pprint import pprint
from datetime import datetime
import pytz

class LiveGame:
    def __init__(self, gameId) -> None:
        self.gameId = gameId
        print('Wings Game Today: ', gameId)
        game_details_url = 'https://api-web.nhle.com/v1/gamecenter/{current_game_id}/boxscore'.format(current_game_id=self.gameId)
        game_details_response = requests.get(game_details_url)
        self.game_details_dict = game_details_response.json()
        self.team_goals = 0
        self.team_abbrev = 'DET'
        self.team_side = ''

    def getIsLive(self):
        isLive = self.game_details_dict['gameState'] == 'LIVE'
        print('Is game: ', self.gameId, ' live? ', isLive)
        return isLive

    def getScore(self):
        home_team = self.game_details_dict['homeTeam']
        away_team = self.game_details_dict['awayTeam']

        pprint(home_team['abbrev'] + ': ' + str(home_team['score']))
        pprint(away_team['abbrev'] + ': ' + str(away_team['score']))
        
        self.hasScoreChanged(int(home_team['score']), int(away_team['score']))

    def getTeamSide(self):
        home_team = self.game_details_dict['homeTeam']['abbrev']
        away_team = self.game_details_dict['awayTeam']['abbrev']

        if (home_team == self.team_abbrev):
            self.team_side = 'homeTeam'
        if (away_team == self.team_abbrev):
            self.team_side = 'awayTeam'

    def hasScoreChanged(self, home_score, away_score):
        if (self.getTeamSide == 'homeTeam' and home_score > self.team_goals):
            print('WINGS SCORED!')
            return True
        if (self.getTeamSide == 'awayTeam' and away_score > self.team_goals):
            print('WINGS SCORED!')
            return True
        print('Waiting for another goal ... ')
        return False

        
    

currentGame = LiveGame('2024020412')

# currentGame.getIsLive()
# currentGame.getScore()

while (currentGame.getIsLive() == True):
    currentGame.getScore()
    pprint('~~~~~~~~~~~~~~~~~~~')
    sleep(1)

import requests
from time import sleep
from pprint import pprint
from datetime import datetime

class LiveGame:
    def __init__(self, gameId) -> None:
        self.gameId = gameId
        self.game_details_url = 'https://api-web.nhle.com/v1/gamecenter/{current_game_id}/boxscore'.format(current_game_id=self.gameId)
        self.game_details_response = requests.get(self.game_details_url)
        self.game_details_dict = self.game_details_response.json()
        
        self.team_goals = 0
        self.team_abbrev = 'DET'
        self.home_or_away = ''

    def getIsLive(self):
        gameState = self.game_details_dict['gameState']
        isLive = gameState == 'LIVE'
        print('GameId: ', self.gameId, ' GameState: ', gameState)
        return isLive

    #return both scores as dict
    def getScore(self):
        game_details_response = requests.get(self.game_details_url)
        self.game_details_dict = game_details_response.json()

        home_team = self.game_details_dict['homeTeam']
        away_team = self.game_details_dict['awayTeam']

        pprint(home_team['abbrev'] + ': ' + str(home_team['score']))
        pprint(away_team['abbrev'] + ': ' + str(away_team['score']))
        
        if self.home_or_away == 'homeTeam':
            return home_team['score']
        if self.home_or_away == 'awayTeam':
            return away_team['score']

    def getTeamSide(self):
        home_team = self.game_details_dict['homeTeam']['abbrev']
        away_team = self.game_details_dict['awayTeam']['abbrev']

        if (home_team == self.team_abbrev):
            print('your team is home')
            self.home_or_away = 'homeTeam'
        if (away_team == self.team_abbrev):
            print('your team is away')
            self.home_or_away = 'awayTeam'

    #need to account for protested goals, score may go down
    def hasScoreIncreased(self, score):
        if (score > self.team_goals):
            pprint('WINGSS SCORED!!!!!')
            self.team_goals += 1
            return True
        print('Waiting for another goal ... ')
        return False  
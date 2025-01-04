import requests
from pprint import pprint

class LiveGame:
    def __init__(self, gameId) -> None:
        self.gameId = gameId
        self.game_details_url = 'https://api-web.nhle.com/v1/gamecenter/{current_game_id}/boxscore'.format(current_game_id=self.gameId)
        self.game_details_response = requests.get(self.game_details_url)
        self.game_details_dict = self.game_details_response.json()
        
        self.team_goals = 0
        self.team_abbrev = 'DET'
        self.vs_team_abbrev = self.game_details_dict['awayTeam']['abbrev']
        self.home_or_away = ''

    def getIsLive(self):
        gameState = self.game_details_dict['gameState']
        isLive = (gameState == 'LIVE') or (gameState == 'CRIT') 
        print('GameId: ', self.gameId, ' GameState: ', gameState)
        return isLive
    
    def isGameFinished(self):
        gameState = self.game_details_dict['gameState']
        isFinished = (gameState == 'FINAL') 
        return isFinished

    def getScore(self):
        game_details_response = requests.get(self.game_details_url)
        self.game_details_dict = game_details_response.json()

        home_team = self.game_details_dict['homeTeam']
        away_team = self.game_details_dict['awayTeam']

        pprint(home_team['abbrev'] + ': ' + str(home_team['score']))
        pprint(away_team['abbrev'] + ': ' + str(away_team['score']))
        
        if self.home_or_away == 'homeTeam':
            return [home_team['score'], away_team['score']]
        if self.home_or_away == 'awayTeam':
            return [away_team['score'], home_team['score']]

    def getTeamSide(self):
        home_team = self.game_details_dict['homeTeam']['abbrev']
        away_team = self.game_details_dict['awayTeam']['abbrev']

        if (home_team == self.team_abbrev):
            print('your team is home')
            self.home_or_away = 'homeTeam'
            self.vs_team_abbrev = away_team
        if (away_team == self.team_abbrev):
            print('your team is away')
            self.home_or_away = 'awayTeam'
            self.vs_team_abbrev = home_team

    def hasScoreIncreased(self, score):
        if (score > self.team_goals):
            print('team goals = ', self.team_goals)
            print('score = ', score)
            pprint('---> SCORE!!! <---')
            self.team_goals = score
            print('team goals = ', self.team_goals)
            print('score = ', score)
            return True
        return False  
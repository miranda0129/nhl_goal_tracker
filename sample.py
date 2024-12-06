import requests
from pprint import pprint
from datetime import datetime
import pytz

season_schedule_url = 'https://api-web.nhle.com/v1/club-schedule-season/DET/now'
season_schedule_response = requests.get(season_schedule_url)
season_schedule_dict = season_schedule_response.json()
pprint('~~~~~~~~~~~~~~~~~~')

#Get next game wings are playing
for item in season_schedule_dict['games']:
    gameState = item['gameState']
    if (gameState == 'FUT'):
        print('The next Red Wings game is at: ')
        print('Game Date: ', item['gameDate'])

        gameDayJson = item['startTimeUTC']
        utcTime = datetime.strptime(gameDayJson, "%Y-%m-%dT%H:%M:%SZ")
        utcTime = pytz.utc.localize(utcTime)
        eastern_tz = pytz.timezone('US/Eastern')
        local_time = utcTime.astimezone(eastern_tz)

        print('Game Time: ')
        print(local_time)
        print('GameId: ', item['id'])
        print('~~~~~~~~~~~~~~~~~~')
        break


#Get today's schedule and check if Wings are playing
daily_schedule_url = 'https://api-web.nhle.com/v1/schedule/now'
daily_schedule_response = requests.get(daily_schedule_url)
daily_schedule_dict = daily_schedule_response.json()

weekly_schedule_games_dict = daily_schedule_dict['gameWeek']
for weekly_game in weekly_schedule_games_dict:
    game_day_json = weekly_game['date']
    game_day = datetime.strptime(game_day_json, "%Y-%m-%d").date()
    today_date = datetime.today().date()

    if (game_day != today_date):
        continue

    pprint(weekly_game.keys())
    for game in weekly_game['games']:
        home_team_abbr = game['homeTeam']['abbrev']
        away_team_abbr = game['awayTeam']['abbrev']
        if (home_team_abbr == 'DET' or away_team_abbr == 'DET'):
            print('Wings are playing today!')


#There's a game today, let's check if it's live
#And if so what is the score
print('Wings Game Today: 2024020412')
game_details_url = 'https://api-web.nhle.com/v1/gamecenter/{current_game_id}/boxscore'.format(current_game_id=2024020412)
game_details_response = requests.get(game_details_url)
game_details_dict = game_details_response.json()

#pprint(game_details_dict)
pprint('~~~~~~~~~~~~~~~~~~~')

if (game_details_dict['gameState'] == 'LIVE'):
    pprint('Game is LIVE!')

    home_team_score = game_details_dict['homeTeam']['score']
    home_team_abbr = game_details_dict['homeTeam']['abbrev']
    away_team_score = game_details_dict['awayTeam']['score']
    away_team_abbr = game_details_dict['awayTeam']['abbrev']

    pprint(home_team_abbr)
    pprint(home_team_score)
    pprint(away_team_abbr)
    pprint(away_team_score)
else:
    pprint('Game is not live...yet')
    
    

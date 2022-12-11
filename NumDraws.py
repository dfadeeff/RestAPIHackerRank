import json

import requests


def getNumDraws(year):
    url = ("https://jsonmock.hackerrank.com/api/football_matches?&year={}".format(year))
    response = requests.get(url).json()
    print(response)
    print(response['data'])
    draws = 0
    total_pages = response['total_pages']
    for i in range(1, total_pages + 1):
        url = (
            "https://jsonmock.hackerrank.com/api/football_matches?&year={}&page={}".format(
                year, i))
        response = requests.get(url).json()
        for j in range(0, len(response['data'])):
            if (response['data'][j]['team1goals'] == response['data'][j]['team2goals']):
                draws += 1
    return draws

if __name__ == '__main__':
    year = '2011'

    print(getNumDraws(year))

'''
{'page': 1, 'per_page': 10, 'total': 6, 'total_pages': 1,
'data': 
[{'name': 'UEFA Champions League', 'country': '', 'year': 2014, 'winner': 'Barcelona', 'runnerup': 'Juventus'}, 
{'name': 'English Premier League', 'country': 'England', 'year': 2014, 'winner': 'Chelsea', 'runnerup': 'Manchester City'},
{'name': 'La Liga', 'country': 'Spain', 'year': 2014, 'winner': 'FC Barcelona', 'runnerup': 'Real Madrid'},
{'name': 'League 1', 'country': 'France', 'year': 2014, 'winner': 'Paris Saint-Germain', 'runnerup': 'Olympique Lyon'},
{'name': 'Serie A', 'country': 'Italy', 'year': 2014, 'winner': 'Juventus', 'runnerup': 'AS Roma'},
{'name': 'Bundesliga', 'country': 'Germany', 'year': 2014, 'winner': 'Bayern Munchen', 'runnerup': 'VfL Wolfsburg'}]}

Matches
'data': 
[{'competition': 'UEFA Champions League', 'year': 2011, 'round': 'GroupH', 'team1': 'Barcelona', 'team2': 'AC Milan', 'team1goals': '2', 'team2goals': '2'}, 
{'competition': 'UEFA Champions League', 'year': 2011, 'round': 'GroupG', 'team1': 'APOEL Nikosia', 'team2': 'Zenit St. Petersburg', 'team1goals': '2', 'team2goals': '1'},
 {'competition': 'UEFA Champions League', 'year': 2011, 'round': 'GroupF', 'team1': 'Borussia Dortmund', 'team2': 'Arsenal', 'team1goals': '1', 'team2goals': '1'}, 
 {'competition': 'UEFA Champions League', 'year': 2011, 'round': 'GroupH', 'team1': 'Viktoria Plzen', 'team2': 'BATE Borisov', 'team1goals': '1', 'team2goals': '1'}, 
 {'competition': 'UEFA Champions League', 'year': 2011, 'round': 'GroupE', 'team1': 'Chelsea', 'team2': 'Bayer Leverkusen', 'team1goals': '2', 'team2goals': '0'}, 
 {'competition': 'UEFA Champions League', 'year': 2011, 'round': 'GroupG', 'team1': 'FC Porto', 'team2': 'Shakhtar Donetsk', 'team1goals': '2', 'team2goals': '1'}, 
 {'competition': 'UEFA Champions League', 'year': 2011, 'round': 'GroupE', 'team1': 'KRC Genk', 'team2': 'Valencia CF', 'team1goals': '0', 'team2goals': '0'}, 
 {'competition': 'UEFA Champions League', 'year': 2011, 'round': 'GroupF', 'team1': 'Olympiacos', 'team2': 'Olympique Marseille', 'team1goals': '0', 'team2goals': '1'}, 
 {'competition': 'UEFA Champions League', 'year': 2011, 'round': 'GroupD', 'team1': 'AFC Ajax', 'team2': 'Olympique Lyon', 'team1goals': '0', 'team2goals': '0'}, 
 {'competition': 'UEFA Champions League', 'year': 2011, 'round': 'GroupC', 'team1': 'Basel', 'team2': 'Otelul Galati', 'team1goals': '2', 'team2goals': '1'}]}





'''

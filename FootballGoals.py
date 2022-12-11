import requests


def getTotalGoals(team, year):
    urlTeam1 = ("https://jsonmock.hackerrank.com/api/football_matches?year={}&team1={}&page=1".format(year, team))
    responseTeam1 = requests.get(urlTeam1).json()
    print("response from team 1 ")
    print(responseTeam1)

    sumGoalsTeam1 = 0
    for i in range(0, responseTeam1['total']):
        goals = int(responseTeam1['data'][i]['team1goals'])
        sumGoalsTeam1 += goals

    urlTeam2 = ("https://jsonmock.hackerrank.com/api/football_matches?year={}&team2={}&page=1".format(year, team))
    responseTeam2 = requests.get(urlTeam2).json()
    sumGoalsTeam2 = 0
    print("response from team 2 ")
    print(responseTeam2)
    for i in range(0, responseTeam2['total']):
        goals = int(responseTeam2['data'][i]['team2goals'])
        sumGoalsTeam2 += goals

    return sumGoalsTeam1 + sumGoalsTeam2


if __name__ == '__main__':
    team = 'Barcelona'
    year = '2011'
    print(getTotalGoals(team, year))

"""
{'page': 1,
 'per_page': 10,
 'total': 6,
 'total_pages': 1,
 'data': [{'competition': 'UEFA Champions League', 'year': 2011, 'round': 'GroupH', 'team1': 'Barcelona',
           'team2': 'AC Milan', 'team1goals': '2', 'team2goals': '2'},
          {'competition': 'UEFA Champions League', 'year': 2011, 'round': 'GroupH', 'team1': 'Barcelona',
           'team2': 'Viktoria Plzen', 'team1goals': '2', 'team2goals': '0'},
          {'competition': 'UEFA Champions League', 'year': 2011, 'round': 'GroupH', 'team1': 'Barcelona',
           'team2': 'BATE Borisov', 'team1goals': '4', 'team2goals': '0'},
          {'competition': 'UEFA Champions League', 'year': 2011, 'round': 'R16', 'team1': 'Barcelona',
           'team2': 'Bayer Leverkusen', 'team1goals': '7', 'team2goals': '1'},
          {'competition': 'UEFA Champions League', 'year': 2011, 'round': 'QF', 'team1': 'Barcelona',
           'team2': 'AC Milan', 'team1goals': '3', 'team2goals': '1'},
          {'competition': 'UEFA Champions League', 'year': 2011, 'round': 'SF', 'team1': 'Barcelona',
           'team2': 'Chelsea', 'team1goals': '2', 'team2goals': '2'}]}
"""

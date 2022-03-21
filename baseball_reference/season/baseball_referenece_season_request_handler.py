def get_baseball_reference_season_data(baseball_reference_params):

    print('in get_baseball_reference_season_data')



'''
import requests
from bs4 import BeautifulSoup
import pandas as pd


Team Table Names

https://www.baseball-reference.com/teams/DET/2004.shtml
1. team_batting (Team batting)
2. team_pitching (Team Pitching)


https://www.baseball-reference.com/teams/DET/2004-roster.shtml
3. appearances (Full Season Roster & Games by Position)
4. coaches (Coaching Staff)


https://www.baseball-reference.com/teams/DET/2004-fielding.shtml
5. standard_fielding (Team Fielding Totals) ERROR



6. players_value_batting (Team Player Value--Batters) ERROR
7. players_value_pitching (Team Player Value--Pitchers)


TEAM = 'DET'
YEAR = '1972'
# URL = 'https://www.baseball-reference.com/teams/OAK/1992.shtml'

URL = "".join(['https://www.baseball-reference.com/teams/', TEAM, '/', YEAR, '.shtml'])
TABLE_NAME = 'team_batting'

r = requests.get(URL, headers = {
    'accept-language':'en-US,en;q=0.8',
})

soup = BeautifulSoup(r.content, 'html5lib')

team_table = soup.find('table', {'id': TABLE_NAME})

df = pd.read_html(str(team_table))[0]

# Remove rows where Rk is Rk
df = df.drop(df[df['Rk'] == 'Rk'].index)

# Remove rows where Rk is NaN (should make this optional in config)
df = df.drop(df[pd.isna(df['Rk'])].index)

# Remove name for roster tables
# df = df.drop(df[df['Name'] == 'Name'].index)

print(df)

'''
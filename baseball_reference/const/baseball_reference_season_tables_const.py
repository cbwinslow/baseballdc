BASEBALL_REFERENCE_SEASON_URL_PREFIX = 'https://www.baseball-reference.com/leagues'

BASEBALL_REFERENCE_LEAUGE_TABLE_CONFIGS = [
    {
        'table': 'Team Wins',
        'table_identifier': 'teams_team_wins3000',
        'url_prefix': BASEBALL_REFERENCE_SEASON_URL_PREFIX,
        'table_commented': False,
        'league_required': True,
        'year_required': False,
        'url_postfix': '',
        'shtml_postfix_required': False,
        'remove_rows_on': []     
    }
]

BASEBALL_REFERENCE_SEASON_TABLE_CONFIGS = [
    *BASEBALL_REFERENCE_LEAUGE_TABLE_CONFIGS
]
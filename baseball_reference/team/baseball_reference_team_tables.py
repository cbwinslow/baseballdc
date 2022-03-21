BASEBALL_REFERENCE_TEAMS_URL_PREFIX = 'https://www.baseball-reference.com/teams'

baseball_reference_team_table_configs = [
    {
        'table': 'Active Franchises',
        'table_identifier': 'teams_active',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': False,
        'team_required': False,
        'year_required': False,
        'shtml_postfix_required': False,
        'remove_rows_on': ['rk:rk', 'rk:Nan']     
    },
    {
        'table': 'Inactive Franchises',
        'table_identifier': 'teams_defunct',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': False,
        'year_required': False,
        'shtml_postfix_required': False,   
        'remove_rows_on': ['rk:rk', 'rk:Nan']            
    },
    {
        'table': 'National Association Franchises',
        'table_identifier': 'teams_na',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': False,
        'year_required': False,
        'shtml_postfix_required': False,   
        'remove_rows_on': ['rk:Nan']            
    },
    {
        'table': 'Franchise History',
        'table_identifier': 'franchise_years',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': False,
        'team_required': True,
        'year_required': False,
        'shtml_postfix_required': False,   
        'remove_rows_on': ['Year:Year']            
    },
    {
        'table': 'Team Batting',
        'table_identifier': 'team_batting',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': False,
        'team_required': True,
        'year_required': True,
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Pitching',
        'table_identifier': 'team_pitching',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': False,
        'team_required': True,
        'year_required': True,
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Full-Season Roster & Games by Position',
        'table_identifier': 'appearances',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Coaching Staff',
        'table_identifier': 'coaches',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Fielding Totals',
        'table_identifier': 'standard_fielding',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },    
    {
        'table': 'Team Player Value--Batters',
        'table_identifier': 'players_value_batting',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Player Value--Pitchers',
        'table_identifier': 'players_value_pitching',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
]
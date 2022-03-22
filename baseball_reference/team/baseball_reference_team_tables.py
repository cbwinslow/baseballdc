BASEBALL_REFERENCE_TEAMS_URL_PREFIX = 'https://www.baseball-reference.com/teams'

'''
All Franchise Tables
'''
baseball_reference_all_franchise_table_configs = [
    {
        'table': 'Active Franchises',
        'table_identifier': 'teams_active',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': False,
        'team_required': False,
        'year_required': False,
        'url_postfix': '',
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
        'url_postfix': '',
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
        'url_postfix': '',
        'shtml_postfix_required': False,   
        'remove_rows_on': ['rk:Nan']            
    }
]

'''
Single Franchise History Tables
'''
baseball_reference_franchise_table_configs = [
    {
        'table': 'Franchise History',
        'table_identifier': 'franchise_years',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': False,
        'team_required': True,
        'year_required': False,
        'url_postfix': '',
        'shtml_postfix_required': False,   
        'remove_rows_on': ['Year:Year']            
    }
]

'''
Single Franchise w/ Year Tables
'''
baseball_reference_team_year_table_configs = [
    {
        'table': 'Team Batting',
        'table_identifier': 'team_batting',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': False,
        'team_required': True,
        'year_required': True,
        'url_postfix': '',
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
        'url_postfix': '',
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
        'url_postfix': '',
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
        'url_postfix': '',
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
        'url_postfix': '',
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
        'url_postfix': '',
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
        'url_postfix': '',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    }
]

'''
Single Franchise w/ Year Batting Tables
'''
baseball_reference_team_year_batting_table_configs = [
    {
        'table': 'Team Advanced Batting',
        'table_identifier': 'players_advanced_batting',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-batting',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Sabermetric Batting',
        'table_identifier': 'players_sabermetric_batting',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-batting',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Batting Ratios*',
        'table_identifier': 'players_ratio_batting',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-batting',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Win Probability*',
        'table_identifier': 'players_win_probability_batting',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-batting',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    }, 
    {
        'table': 'Team Baserunning/Misc*',
        'table_identifier': 'players_baserunning_batting',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-batting',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    }, 
    {
        'table': 'Team PH/HR/Situ Hitting*',
        'table_identifier': 'players_situational_batting',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-batting',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    }, 
    {
        'table': 'Team Pitches Batting*',
        'table_identifier': 'players_pitches_batting',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-batting',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Neutralized Batting',
        'table_identifier': 'players_neutral_batting',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-batting',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Cumulative Batting',
        'table_identifier': 'players_cumulative_batting',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-batting',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    }    
]

'''
Single Franchise w/ Year Pitching Tables
'''
baseball_reference_team_year_pitching_table_configs = [
    {
        'table': 'Team Advanced Pitching',
        'table_identifier': 'players_pitching_advanced',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-pitching',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Pitching Ratios*',
        'table_identifier': 'players_ratio_pitching',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-pitching',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Batting Against*',
        'table_identifier': 'players_batting_pitching',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-pitching',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Win Probability*',
        'table_identifier': 'players_win_probability_pitching',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-pitching',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Starting Pitching*',
        'table_identifier': 'players_starter_pitching',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-pitching',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Relief Pitching*',
        'table_identifier': 'players_reliever_pitching',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-pitching',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Baserunning/Situ*',
        'table_identifier': 'players_basesituation_pitching',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-pitching',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Pitching Pitches*',
        'table_identifier': 'players_pitches_pitching',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-pitching',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Team Neutralized Pitching',
        'table_identifier': 'players_neutral_pitching',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-pitching',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },    
    {
        'table': 'Team Cumulative Pitching',
        'table_identifier': 'players_cumulative_pitching',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-pitching',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },   
]

'''
Single Franchise w/ Year Fielding Tables
'''
baseball_reference_team_year_fielding_table_configs = [
    {
        'table': 'Player Standard Fielding--C',
        'table_identifier': 'players_standard_fielding_c',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Standard Fielding--1B',
        'table_identifier': 'players_standard_fielding_1b',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Standard Fielding--2B',
        'table_identifier': 'players_standard_fielding_2b',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },    
    {
        'table': 'Player Standard Fielding--3B',
        'table_identifier': 'players_standard_fielding_3b',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Standard Fielding--SS',
        'table_identifier': 'players_standard_fielding_ss',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Standard Fielding--LF',
        'table_identifier': 'players_standard_fielding_lf',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Standard Fielding--CF',
        'table_identifier': 'players_standard_fielding_cf',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Standard Fielding--RF',
        'table_identifier': 'players_standard_fielding_rf',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Standard Fielding--OF',
        'table_identifier': 'players_standard_fielding_of',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Standard Fielding--P',
        'table_identifier': 'players_standard_fielding_p',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player DH Games',
        'table_identifier': 'players_DH_games',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Advanced Fielding -- C',
        'table_identifier': 'players_advanced_fielding_c',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Advanced Fielding -- C Baserunning',
        'table_identifier': 'players_advanced_fielding_c_baserunning',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Advanced Fielding -- 1B',
        'table_identifier': 'players_advanced_fielding_1b',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Advanced Fielding -- 2B',
        'table_identifier': 'players_advanced_fielding_2b',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Advanced Fielding -- 3B',
        'table_identifier': 'players_advanced_fielding_3b',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Advanced Fielding -- SS',
        'table_identifier': 'players_advanced_fielding_ss',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Advanced Fielding -- LF',
        'table_identifier': 'players_advanced_fielding_lf',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Advanced Fielding -- CF',
        'table_identifier': 'players_advanced_fielding_cf',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Advanced Fielding -- RF',
        'table_identifier': 'players_advanced_fielding_rf',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Player Advanced Fielding -- P',
        'table_identifier': 'players_advanced_fielding_p',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': True,
        'url_postfix': '-fielding',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
]

'''
Single Franchise w/ Year Fielding Tables
'''
baseball_reference_franchise_batting_history_table_configs = [
    {
        'table': 'Year-by-Year Team Batting',
        'table_identifier': 'yby_team_bat',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': False,
        'team_required': True,
        'year_required': False,
        'url_postfix': '/batteam',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Year-by-Year Team Batting per Game',
        'table_identifier': 'yby_team_bat_per_game',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': False,
        'url_postfix': '/batteam',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Year-by-Year Team Batting Ranks',
        'table_identifier': 'yby_team_bat_ranks',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': False,
        'url_postfix': '/batteam',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
]

baseball_reference_franchise_pitching_history_table_configs = [
    {
        'table': 'Year-by-Year Team Pitching',
        'table_identifier': 'yby_team_pitch',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': False,
        'team_required': True,
        'year_required': False,
        'url_postfix': '/pitchteam',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Year-by-Year Team Pitching per Game',
        'table_identifier': 'yby_team_pitch_per_game',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': False,
        'url_postfix': '/pitchteam',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
    {
        'table': 'Year-by-Year Team Pitching Ranks',
        'table_identifier': 'yby_team_pitch_ranks',
        'url_prefix': BASEBALL_REFERENCE_TEAMS_URL_PREFIX,
        'table_commented': True,
        'team_required': True,
        'year_required': False,
        'url_postfix': '/pitchteam',
        'shtml_postfix_required': True,   
        'remove_rows_on': []            
    },
]

baseball_reference_team_table_configs = [
    *baseball_reference_all_franchise_table_configs, 
    *baseball_reference_franchise_table_configs, 
    *baseball_reference_team_year_table_configs,
    *baseball_reference_team_year_batting_table_configs,
    *baseball_reference_team_year_pitching_table_configs,
    *baseball_reference_team_year_fielding_table_configs,
    *baseball_reference_franchise_batting_history_table_configs,
    *baseball_reference_franchise_pitching_history_table_configs
]
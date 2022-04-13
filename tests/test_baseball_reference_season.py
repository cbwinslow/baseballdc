import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import baseballdc
import unittest

class TestBaseballReferenceIndividualPlayer(unittest.TestCase):

    def test_team_wins(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'SEASON',
                'table': 'Team Wins',
                'league': 'NL',
            }
        }

        df = baseballdc.get_data(baseballdc_request)
        df_columns = list(df.columns.values)

        expected_columns = ['Year', 'G', 'ARI', 'ATL', 'CHC', 'CIN', 'COL', 'HOU', 'LAD', 'MIA', 'MIL', 'NYM', 
                            'PHI', 'PIT', 'SDP', 'SFG', 'STL', 'WSN']
        self.assertEqual(df_columns, expected_columns)

    def test_east_division(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'SEASON',
                'table': 'East Division',
                'league': 'NL',
                'year': '2021'
            }
        }

        df = baseballdc.get_data(baseballdc_request)
        df_columns = list(df.columns.values)

        expected_columns = ['Tm', 'W', 'L', 'W-L%', 'GB']
        self.assertEqual(df_columns, expected_columns)        

    def test_central_division(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'SEASON',
                'table': 'Central Division',
                'league': 'NL',
                'year': '2021'
            }
        }

        df = baseballdc.get_data(baseballdc_request)
        df_columns = list(df.columns.values)

        expected_columns = ['Tm', 'W', 'L', 'W-L%', 'GB']
        self.assertEqual(df_columns, expected_columns)  

    def test_west_division(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'SEASON',
                'table': 'West Division',
                'league': 'NL',
                'year': '2021'
            }
        }

        df = baseballdc.get_data(baseballdc_request)
        df_columns = list(df.columns.values)

        expected_columns = ['Tm', 'W', 'L', 'W-L%', 'GB']
        self.assertEqual(df_columns, expected_columns)  


    def test_postseason(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'SEASON',
                'table': 'Postseason',
                'league': 'NL',
                'year': '2021'
            }
        }

        df = baseballdc.get_data(baseballdc_request)
        df_columns = list(df.columns.values)

        expected_columns = [0, 1, 2]
        self.assertEqual(df_columns, expected_columns)  

    def test_team_standard_batting(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'SEASON',
                'table': 'Team Standard Batting',
                'league': 'NL',
                'year': '2021'
            }
        }

        df = baseballdc.get_data(baseballdc_request)
        df_columns = list(df.columns.values)

        expected_columns = ['Tm', '#Bat', 'BatAge', 'R/G', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 
                            'SB', 'CS', 'BB', 'SO', 'BA', 'OBP', 'SLG', 'OPS', 'OPS+', 'TB', 'GDP', 'HBP', 'SH', 
                            'SF', 'IBB', 'LOB']
        self.assertEqual(df_columns, expected_columns)  

    def test_team_standard_batting(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'SEASON',
                'table': 'Team Standard Pitching',
                'league': 'NL',
                'year': '2021'
            }
        }

        df = baseballdc.get_data(baseballdc_request)
        df_columns = list(df.columns.values)

        expected_columns = ['Tm', '#P', 'PAge', 'RA/G', 'W', 'L', 'W-L%', 'ERA', 'G', 'GS', 'GF', 'CG', 'tSho', 'cSho', 'SV', 
                            'IP', 'H', 'R', 'ER', 'HR', 'BB', 'IBB', 'SO', 'HBP', 'BK', 'WP', 'BF', 'ERA+', 'FIP', 'WHIP', 'H9', 
                            'HR9', 'BB9', 'SO9', 'SO/W', 'LOB']
        self.assertEqual(df_columns, expected_columns)  

    def test_american_league_wins_above_average_by_position(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'SEASON',
                'table': 'American League Wins Above Average By Position',
                'league': 'NL',
                'year': '2021'
            }
        }

        df = baseballdc.get_data(baseballdc_request)
        df_columns = list(df.columns.values)

        expected_columns = ['Rk', 'Total', 'All P', 'SP', 'RP', 'Non-P', 'C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 
                            'OF (All)', 'DH', 'PH']
        self.assertEqual(df_columns, expected_columns)  

    def test_national_league_wins_above_average_by_position(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'SEASON',
                'table': 'National League Wins Above Average By Position',
                'league': 'NL',
                'year': '2021'
            }
        }

        df = baseballdc.get_data(baseballdc_request)
        df_columns = list(df.columns.values)

        expected_columns = ['Rk', 'Total', 'All P', 'SP', 'RP', 'Non-P', 'C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 
                            'OF (All)', 'DH', 'PH']
        self.assertEqual(df_columns, expected_columns)  

    def test_team_fielding(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'SEASON',
                'table': 'Team Fielding',
                'league': 'NL',
                'year': '2021'
            }
        }

        df = baseballdc.get_data(baseballdc_request)
        df_columns = list(df.columns.values)

        expected_columns = ['Tm', '#Fld', 'RA/G', 'DefEff', 'G', 'GS', 'CG', 'Inn', 'Ch', 'PO', 'A', 'E', 'DP', 
                            'Fld%', 'Rtot', 'Rtot/yr', 'Rdrs', 'Rdrs/yr', 'Rgood']
        self.assertEqual(df_columns, expected_columns)  

    def test_major_league_baseball_wins_above_avg_by_position(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'SEASON',
                'table': 'Major League Baseball Wins Above Avg By Position',
                'league': 'NL',
                'year': '2021'
            }
        }

        df = baseballdc.get_data(baseballdc_request)
        df_columns = list(df.columns.values)

        expected_columns = ['Rk', 'Total', 'All P', 'SP', 'RP', 'Non-P', 'C', '1B', '2B', '3B', 'SS', 'LF', 
                            'CF', 'RF', 'OF (All)', 'DH', 'PH']
        self.assertEqual(df_columns, expected_columns)  

if __name__ == '__main__':
        unittest.main()


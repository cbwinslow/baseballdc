import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import baseballdc
import unittest

class TestBaseballReferenceIndividualPlayer(unittest.TestCase):

    def test_standard_batting(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'INDIVIDUAL_PLAYER',
                'table': 'Standard Batting',
                'first_name': 'Shohei',
                'last_name': 'Ohtani'
            }
        }

        df = baseballdc.get_data(baseballdc_request)

        df_columns = list(df.columns.values)
        expected_columns = ['Year', 'Age', 'Tm', 'Lg', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR',
                            'RBI', 'SB', 'CS', 'BB', 'SO', 'BA', 'OBP', 'SLG', 'OPS', 'OPS+', 'TB',
                            'GDP', 'HBP', 'SH', 'SF', 'IBB', 'Pos', 'Awards']

        self.assertEqual(df_columns, expected_columns)


    def test_value_batting(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'INDIVIDUAL_PLAYER',
                'table': 'Player Value—Batting',
                'first_name': 'Shohei',
                'last_name': 'Ohtani'
            }
        }

        df = baseballdc.get_data(baseballdc_request)

        df_columns = list(df.columns.values)

        expected_columns = ['Year', 'Age', 'Tm', 'Lg', 'G', 'PA', 'Rbat', 'Rbaser', 'Rdp', 'Rfield', 
                            'Rpos', 'RAA', 'WAA', 'Rrep', 'RAR', 'WAR', 'waaWL%', '162WL%', 'oWAR', 
                            'dWAR', 'oRAR', 'Salary', 'Pos', 'Awards']

        self.assertEqual(df_columns, expected_columns)

        
    def test_advanced_batting(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'INDIVIDUAL_PLAYER',
                'table': 'Advanced Batting',
                'first_name': 'Shohei',
                'last_name': 'Ohtani'
            }
        }

        df = baseballdc.get_data(baseballdc_request)

        df_columns = list(df.columns.values)

        expected_columns = [('Unnamed: 0_level_0', 'Year'), ('Unnamed: 1_level_0', 'Age'), ('Unnamed: 2_level_0', 'Tm'), 
                            ('Unnamed: 3_level_0', 'Lg'), ('Batting', 'rOBA'), ('Batting', 'Rbat+'), ('Batting', 'BAbip'), 
                            ('Batting', 'ISO'), ('Batting Ratios', 'HR%'), ('Batting Ratios', 'SO%'), ('Batting Ratios', 'BB%'), 
                            ('Batted Ball', 'EV'), ('Batted Ball', 'HardH%'), ('Batted Ball', 'LD%'), ('Batted Ball', 'GB%'), 
                            ('Batted Ball', 'FB%'), ('Batted Ball', 'GB/FB'), ('Batted Ball', 'Pull%'), ('Batted Ball', 'Cent%'), 
                            ('Batted Ball', 'Oppo%'), ('Win Probability', 'WPA'), ('Win Probability', 'cWPA'), ('Win Probability', 'RE24'), 
                            ('Baserunning', 'RS%'), ('Baserunning', 'SB%'), ('Baserunning', 'XBT%')]

        self.assertEqual(df_columns, expected_columns)
    
    def test_standard_fielding(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'INDIVIDUAL_PLAYER',
                'table': 'Standard Fielding',
                'first_name': 'Shohei',
                'last_name': 'Ohtani'
            }
        }

        df = baseballdc.get_data(baseballdc_request)

        df_columns = list(df.columns.values)

        expected_columns = ['Year', 'Age', 'Tm', 'Pos', 'Lg', 'G', 'GS', 'CG', 'Inn', 'Ch', 'PO', 'A', 'E', 'DP', 'Fld%', 
                            'Rtot', 'Rdrs', 'Rtot/yr', 'Rdrs/yr', 'RF/9', 'RF/G', 'lgFld%', 'lgRF9', 'lgRFG', 'SB', 'CS', 
                            'CS%', 'lgCS%', 'PO.1', 'Awards']

        self.assertEqual(df_columns, expected_columns)

    def test_appearances(self):

        baseballdc_request = {
            'data_source': 'BASEBALL_REFERENCE',
            'query_params': {
                'scope': 'INDIVIDUAL_PLAYER',
                'table': 'Appearances',
                'first_name': 'Shohei',
                'last_name': 'Ohtani'
            }
        }

        df = baseballdc.get_data(baseballdc_request)

        df_columns = list(df.columns.values)

        print(df_columns)

        expected_columns = ['Year', 'Age', 'Tm', 'Lg', 'G', 'GS', 'Batting', 'Defense', 'P', 'C', '1B', '2B', '3B', 'SS', 'LF', 
                            'CF', 'RF', 'OF', 'DH', 'PH', 'PR']

        self.assertEqual(df_columns, expected_columns)

if __name__ == '__main__':
        unittest.main()


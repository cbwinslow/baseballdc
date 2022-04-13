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

if __name__ == '__main__':
        unittest.main()


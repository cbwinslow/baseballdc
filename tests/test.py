import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import baseballdc

baseballdc_request_player = {
	'data_source': 'BASEBALL_REFERENCE',
	'query_params': {
        'scope': 'INDIVIDUAL_PLAYER',
        'table': 'Standard Batting',
        'first_name': 'Justin',
        'last_name': 'Verlander'
	}
}

df = baseballdc.get_data(baseballdc_request_player)

print("**********************")
print("**********************")
print("**********************")
print("**********************")

print(df);


# # EXAMPLE REQUEST
# baseballdc_request = {
# 	'data_source': 'BASEBALL_REFERENCE',
# 	'query_params': {
#         'scope': 'TEAM',
#         'table': 'Year-by-Year Team Pitching Ranks',
#         'team': 'DET',
#         'year': 2002
# 	}
# }

# baseballdc_request_season = {
# 	'data_source': 'BASEBALL_REFERENCE',
# 	'query_params': {
#         'scope': 'SEASON',
#         'table': 'Player Standard Pitching',
#         # 'team': 'DET',
#         'year': 2003,
#         'league': 'NL'
# 	}
# }

# baseballdc_request_player = {
# 	'data_source': 'BASEBALL_REFERENCE',
# 	'query_params': {
#         'scope': 'INDIVIDUAL_PLAYER',
#         'table': 'Standard Batting',
#         'first_name': 'Miguel',
#         'last_name': "Cabrera"
# 	}
# }

# baseballdc_request_player = {
# 	'data_source': 'BASEBALL_REFERENCE',
# 	'query_params': {
#         'scope': 'INDIVIDUAL_PLAYER',
#         'table': 'Standard Batting',
#         'first_name': 'Justin',
#         'last_name': 'Verlander'
# 	}
# }


# get_data(baseballdc_request_player)
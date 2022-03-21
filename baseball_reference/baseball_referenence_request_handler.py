import baseball_reference.team.baseball_reference_team_request_handler as team_request_handler
import baseball_reference.season.baseball_referenece_season_request_handler as season_request_handler
import baseball_reference.individual_player.baseball_reference_individual_player_request_handler as individual_player_request_handler

import baseball_reference.baseball_reference_scope as baseball_reference_scope

def get_baseball_reference_data(baseballdc_request):

    baseball_reference_params = baseballdc_request.get('baseballReferenceParams');

    validate_baseball_reference_params(baseball_reference_params);

    if(baseball_reference_params.get('scope').upper() == baseball_reference_scope.INDIVIDUAL_PLAYER):
        df = individual_player_request_handler.get_baseball_reference_individual_player_data(baseball_reference_params)

    elif(baseball_reference_params.get('scope').upper() == baseball_reference_scope.TEAM):
        df = team_request_handler.get_baseball_reference_team_data(baseball_reference_params)
        
    elif(baseball_reference_params.get('scope').upper() == baseball_reference_scope.SEASON):
        df = season_request_handler.get_baseball_reference_season_data(baseball_reference_params)

    return df

def validate_baseball_reference_params(baseball_reference_params):
    if(baseball_reference_params.get('scope').upper() not in baseball_reference_scope.BASEBALL_REFERENCE_SCOPE_LIST):
        print('***** Baseball Reference Scope Not Valid *****')

import util.const.data_source as data_source 

import baseball_reference.baseball_referenence_request_handler as baseball_referenence_request_handler

def get_data(baseballdc_request):
    # Validate that the incoming data request has a valid data source.
    validate_get_data_request(baseballdc_request)

    # Route the request to the correct data source handler, and create the requested dataframe
    df = route_get_data_request(baseballdc_request)
    print(df)


def validate_get_data_request(baseballdc_request):    
    if(baseballdc_request.get('dataSource').upper() not in data_source.DATA_SOURCE_LIST):
        print('***** Data Source Not Valid *****')

def route_get_data_request(baseballdc_request):
    if(baseballdc_request.get('dataSource').upper() == data_source.BASEBALL_REFERENCE.upper()):
        df = baseball_referenence_request_handler.get_baseball_reference_data(baseballdc_request)

    return df

# EXAMPLE REQUEST
baseballdc_request = {
	'dataSource': 'BASEBALL_REFERENCE',
	'baseballReferenceParams': {
        'scope': 'TEAM',
        'table': 'Team Batting',
        'team': 'CHW',
        'year': '2002'
	}
}

get_data(baseballdc_request)
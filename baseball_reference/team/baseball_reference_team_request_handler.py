import pandas as pd

import baseball_reference.team.team_table_config_service as team_table_config_service
import baseball_reference.team.team_url_service as team_url_service
import baseball_reference.team.team_table_request_service as team_table_request_service
import baseball_reference.team.team_table_format_service as team_table_format_service

def get_baseball_reference_team_data(query_params):

    table_config = team_table_config_service.get_table_config(query_params)

    url = team_url_service.construct_url(table_config, query_params)

    table = team_table_request_service.get_table(table_config, url, query_params)

    df = pd.read_html(str(table))[0]

    formatted_df = team_table_format_service.format_df(df, table_config)

    return formatted_df

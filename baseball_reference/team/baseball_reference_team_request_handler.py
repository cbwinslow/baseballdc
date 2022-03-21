import requests
from bs4 import BeautifulSoup, Comment
import pandas as pd

import baseball_reference.team.baseball_reference_team_tables as baseball_reference_team_tables

def get_baseball_reference_team_data(baseball_reference_params):

    table_config = get_table_config(baseball_reference_params)

    url = construct_table_url(table_config, baseball_reference_params)

    response = requests.get(url, headers = {
        'accept-language':'en-US,en;q=0.8',
    })


    if(table_config['table_commented'] == True):
        table = get_commented_table(response, table_config)
    else: 
        table = get_table(response, table_config)

    df = pd.read_html(str(table))[0]

    # Remove rows where Rk is Rk
    # df = df.drop(df[df['Rk'] == 'Rk'].index)

    # Remove rows where Rk is NaN (should make this optional in config)
    # df = df.drop(df[pd.isna(df['Rk'])].index)

    return df

def get_table_config(baseball_reference_params):
    configs = baseball_reference_team_tables.baseball_reference_team_table_configs

    for config in configs:
        if(config['table'].upper() == baseball_reference_params['table'].upper()):
            table_config = config
    
    return table_config

def construct_table_url(table_config, baseball_reference_params):

    url_prefix = table_config['url_prefix']

    url_team = ''
    if(table_config['team_required'] == True):
        url_team = '/' + baseball_reference_params['team']

    url_year = ''
    if(table_config['year_required'] == True):
        url_year = '/' + baseball_reference_params['year']

    # todo: pre_shtml

    shtml_postfix = ''
    if(table_config['shtml_postfix_required'] == True):
        shtml_postfix = '.shtml'

    url = url_prefix + url_team + url_year + shtml_postfix

    print('url: ')
    print(url)
    return url


def get_table(response, table_config):

    soup = BeautifulSoup(response.content, 'html5lib')

    table = soup.find('table', {'id': table_config['table_identifier']})

    return table


def get_commented_table(response, table_config):

    soup = BeautifulSoup(response.content, 'html5lib')

    id_plus_table_name = "".join(['id="', table_config['table_identifier'], '"'])


    for comment in soup.findAll(text=lambda text:isinstance(text, Comment)):

        if(id_plus_table_name in comment):
            commented_table = comment

    soup = BeautifulSoup(commented_table , 'html5lib')

    table = soup.find('table', {'id': table_config['table_identifier']})

    return table


# baseballdc
## Baseball Data Center (v1.0.0)

Baseball Data Center was created with the goal of making the data retrieval process for baseball statistics simple.

The baseballdc library exposes one function to it's end user, the `get_data` function. By calling this function with the required parameter object, you can retrieve baseball statistics in a Pandas DataFrame to use in your Python project.

## How to install baseballdc:

Use pip to install baseballdc:

```bash
pip install baseballdc
```

## How to use baseballdc:


To retrieve data with baseballdc, you need to pass a Python dictionary as a parameter into the `get_data` function. (If you are not familiar with Python dictionaries, [here](https://www.w3schools.com/python/python_dictionaries.asp) is a quick overview.)


The format of the dictionary that the `get_data` function requires is: 

```python
{
	'data_source': string,
	'query_params': {
		'scope': string,
		'table': string
	}
}
```

## How to configure the request dictionary:


### 'data_source'

baseballdc currently only scrapes data from Baseball Reference, so the data_source should be set to BASEBALL_REFERENCE

```python
'data_source': 'BASEBALL_REFERENCE',
```
### 'query_params'

The query params object is itself a dictionary, with two required values, and multiple optional values.

### 'query_params' - Required Values
The two required values are the scope, and table.

The scope of the data you can retreieve is split into three categories. 

* INDIVIDUAL_PLAYER
* TEAM
* SEASON

The table is the name of the table on Baseball Reference

For example the request: 

```python
{
        'data_source': 'BASEBALL_REFERENCE',
        'query_params': {
                'scope': 'TEAM',
                'table': 'Active Franchises',
        }
}
```

will retrieve the Active Franchises table, that can be found [here](https://www.baseball-reference.com/teams/) on Baseball Reference. 

### 'query_params' - Optional Values
There are also optional values that can be passed into the query_params, to further specify which table you request. The list of accepted optional parameters are

* first_name
* last_name
* team
* league
* year


## Examples
A few example requests you could make are:

	
	- Retrieve Shohei Otani's pitching stats table from Baseball Reference

```python
{
	'data_source': string,
	'query_params': {
		'scope': string,
		'table': string
	}
}
```
	- Retrieve Juan Soto's batting stats from Baseball Reference

```python
{
	'data_source': string,
	'query_params': {
		'scope': string,
		'table': string
	}
}
```

	- Retrieve the Detroit Tigers from 2021 from Baseball Reference

```python
{
	'data_source': string,
	'query_params': {
		'scope': string,
		'table': string
	}
}
```

	- Retrieve the National League's standings for 2021 from Baseball Reference
```python
{
	'data_source': string,
	'query_params': {
		'scope': string,
		'table': string
	}
}
```


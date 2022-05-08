# baseballdc
## Baseball Data Center

Baseball Data Center was created with the goal of making the data retrieval process for baseball statistics simple.

The baseballdc library exposes one function to it's end user, the "get_data" function. By calling this function with the required parameters, you can retrieve baseball statistics in a Pandas DataFrame to use in your Python project.

### How to install baseballdc:

Use pip to install baseballdc:

```bash
pip install baseballdc
```

### How to use baseballdc:

baseballdc currently scrapes data from Baseball Reference. To pull a Baseball Reference data table into your project, you will need to pass a  object into the ___ function, specifying which table you are requesting.


The format of the required object is: 

{
	'data_source': string,
	'query_params': {
		'scope': string,
		'table': string
	}
}

baseballdc currently scrapes data from Baseball Reference, so the data_source should be 

'data_source': 'BASEBALL_REFERENCE',


Nested in the request object is a query_params object. This object has two required values, the scope, and table.


The scope of the data you can retreieve is split into three categories. 

	- INDIVIDUAL_PLAYER
	- TEAM
	- SEASON


The table is the name of the table on Baseball Reference


There are also optional parameters that can be passed into the query_params, to further specify which table you request. The list of accepted optional parameters are

	- first_name
	- last_name
	- team
	- league
	- year


### Examples
A few example requests you could make are:

	
	- Retrieve Shohei Otani's pitching stats table from Baseball Reference

	- Retrieve Juan Soto's batting stats from Baseball Reference

	- Retrieve the Detroit Tigers from 2021 from Baseball Reference

	- Retrieve the National League's standings for 2021 from Baseball Reference


